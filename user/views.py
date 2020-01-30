from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserUpdateForm, ProfileUpdateForm, DocumentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid input or Your account not yet approval')
            return redirect('login')
    else:
        return render(request, 'user/nss_login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, f'Username already exist')
                return redirect('user-senior-register')
            elif User.objects.filter(email=email).exists():
                messages.success(request, f'Email already exist')
                return redirect('user-senior-register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.is_active = False
                user.save()
                return redirect('login')
        else:
            messages.success(request, f'password not match')
            return redirect('user-senior-register')
    else:
        return render(request, 'user/register.html')


@staff_member_required
def senior_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'your account is activated within 24 hours')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/user_register.html', {'form': form})


@staff_member_required
def junior_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Registration successfully for Junior Student please Contact your Senior')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/user_register.html', {'form': form})


@staff_member_required
def teacher_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created successfull now we are able login')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('nss-senior-register')
    else:
        form = UserRegisterForm()
    return render(request, 'user/user_register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)


from django.shortcuts import render
from django.http import HttpResponse
from .models import Nss_team_member, Document
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Nss_team_member
    template_name = 'user/nss_team.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Nss_team_member


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Nss_team_member
    fields = ['name', 'batch', 'achievement', 'branch', 'sex', 'status', 'image']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Nss_team_member
    fields = ['name', 'batch', 'achievement', 'branch', 'sex', 'status', 'image']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.added_by:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Nss_team_member
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.added_by:
            return True
        return False


class Nss_team_2017_18(ListView):
    model = Nss_team_member
    template_name = 'user/nss_team_2017-18.html'
    context_object_name = 'posts'


class Nss_team_2016_17(ListView):
    model = Nss_team_member
    template_name = 'user/nss_team_2016-17.html'
    context_object_name = 'posts'


from django.core.files.storage import FileSystemStorage


@staff_member_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'user/upload.html', {
        'form': form
    })


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Document
    fields = ['description', 'document']
    template_name = 'user/upload.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class ReportListView(ListView):
    model = Document
    template_name = 'user/special_camp_report.html'
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Document


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Document
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.added_by:
            return True
        return False


from django.contrib.auth import get_user_model


@staff_member_required
def showthis(request):
    all_users = get_user_model().objects.all()

    context = {'allusers': all_users}
    return render(request, 'user/active_user_show.html', context)
