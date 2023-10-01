
from django.urls import path

from . import views

urlpatterns = [
    path('',views.add_task,name='add_task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('listview/',views.TaskListView.as_view(),name='listview/'),
    path('detailview/<int:pk>/',views.TaskDetailView.as_view(),name='detailview/'),
    path('updateview/<int:pk>/', views.TaskUpdateView.as_view(), name='updateview/'),
    path('deleteview/<int:pk>/', views.TaskDeleteView.as_view(), name='Deleteview/'),


]
