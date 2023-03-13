from django.urls import path
from . import views
app_name='clg_app'
urlpatterns = [
    path('',views.clg,name='clg'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('form',views.form,name='form'),
    path('newpage',views.newpage,name='newpage'),
]