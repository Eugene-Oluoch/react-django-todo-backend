from django.urls import path
from . import views


urlpatterns = [
    path('all/',views.TodoAll.as_view()),
    path('single/<int:pk>/',views.TodoSingle.as_view()),
    path('add/',views.TodoAdd.as_view()),
    path('update/<int:pk>/',views.TodoUpdate.as_view()),
    path('delete/<int:pk>/',views.TodoDelete.as_view()),
]