from django.urls import path
from . import views

urlpatterns = [
         path('show_all_activity/',views.Show_activity.as_view(),name='show-all-activity'),
         path('new_activity/',views.New_activity_create.as_view(),name='new-activity'),
         path('activity/<int:pk>',views.ActivityDetailView.as_view(), name='activity-detail'),
         path('activity/<int:pk>/update/', views.ActivityUpdateView.as_view(), name='activity-update'),
         path('activity/<int:pk>/delete/', views.ActivityDeleteView.as_view(), name='activity-delete'), 
]