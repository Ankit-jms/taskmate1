
from django.urls import path
from todolist import views
from user_app import views as my_views
urlpatterns = [
    path('' ,views.todolist,name='todolist'),
    path('delete/<task_id>' ,views.delete_task,name='delete_task'),
    path('edit/<task_id>' ,views.edit_task,name='edit_task'),
    path('complete/<task_id>' ,views.complete_task,name='complete_task'),
    path('register',my_views.register,name='register'),
    
    path('home' ,views.home,name='home'),
    path('pending/<task_id>' ,views.pending_task,name='pending_task'),
    
]