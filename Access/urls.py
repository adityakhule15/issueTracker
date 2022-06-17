from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('add/', views.IssusList.add, name="add"),
        path('login/', views.IssusList.login, name="login"),
        path('view/', views.IssusList.view, name="view"),
        path('postSave/<str:Email>', views.IssusList.postSave, name="postSave"),
        path('edit/<str:Email>/<str:ID>', views.IssusList.edit, name="edit"),
        path('delete/<str:ID>', views.IssusList.delete, name="delete"),
    ]