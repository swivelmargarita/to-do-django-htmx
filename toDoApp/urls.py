from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('task/create', views.create_task, name="create_task"),
    path('task/<pk>', views.view_task, name='view_task'),
    path('task/<pk>/edit', views.edit_task, name="edit_task"),
    path('task/<pk>/delete', views.delete_task, name="delete_task"),
]
