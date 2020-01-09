from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity,Comment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin  
from .forms import CommentForm



def ActivityDetails(request,slug):
	activity = get_object_or_404(Activity,Slug = slug)
	comments = activity.comments.filter(active = True , Parent__isnull=True)
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			pass

	return render(request,'activity_of_nss/activity_details_comment.html',{activity : 'activity'})



class Show_activity(ListView):
	model = Activity
	context_object_name='activity'
	template_name = 'activity_of_nss/show_all_activity.html'
	ordering = ['-date_of_activity']
	paginate_by = 4
   
class New_activity_create(CreateView,LoginRequiredMixin):
	model = Activity
	fields =['title','description','date_of_activity','time_of_activity','address','image']
	def form_valid(self,form):
		form.instance.created_by=self.request.user
		return super().form_valid(form)   

class ActivityDetailView(DetailView):
	model =Activity	
 
class ActivityUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model =Activity	
	fields =['title','description','date_of_activity','time_of_activity','address','image']
	def form_valid(self,form):
		form.instance.created_by=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.created_by:
			return True	
		return False

class ActivityDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Activity	
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.created_by:
			return True	
		return False

