from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('signup/',RegisterPage.as_view(), name='signup'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/',TaskUpdate.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete'),
]
