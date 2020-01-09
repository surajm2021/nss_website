from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import( 
                 PostListView,
                 PostDetailView,
                 PostCreateView,
                 PostUpdateView,
                 PostDeleteView,
                 model_form_upload,
                 ReportListView,
                 ReportCreateView,
                 ReportDetailView,
                 ReportDeleteView,
                 showthis
                 )


urlpatterns = [
         path('nss_login/',views.user_login,name='login'),
         path('senior_register/',views.register,name='user-senior-register'),
         path('junior_register/',views.junior_register,name='user-junior-register'), 
         path('teacher_register/',views.teacher_register,name='user-teacher-register'), 
         path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'), 
         path('profile/',views.profile,name='profile'), 
         path('login/',auth_views.LoginView.as_view(template_name='user/user_login.html'),name='login2'),
         path('', PostListView.as_view() ,name="nss-team"), 
         path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
         path('post/new/', PostCreateView.as_view(), name='post-create'),
         path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
         path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
         path('nss_team_2017_18/',views.Nss_team_2017_18.as_view(),name='nss-team-2017-18'),
         path('nss_team_2016_17/',views.Nss_team_2016_17.as_view(),name='nss-team-2016-17'),
         path('upload/',views.ReportCreateView.as_view(),name='simple'),
         path('special_camp_report/', ReportListView.as_view() ,name="special-camp"), 
         path('report_delete/<int:pk>/delete/', ReportDeleteView.as_view() ,name="report-delete"), 
         path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'), 
         path('all_active_user/',views.showthis,name='active-user'),                    
]
