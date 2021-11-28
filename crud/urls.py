from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='Home'),
    path('form/', views.form,  name='Form'),
    path('send', views.send,  name='send'),
    path('show', views.show,  name='show'),
    path('edit', views.edit,  name='edit'),
    path('update', views.update, name='update'),
    path('profile', views.profile, name='profile'),
]