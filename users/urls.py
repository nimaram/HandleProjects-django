from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('login',views.view_login,name='login'),
    path('register',views.view_register,name='register'),
    path('logout',views.view_logout,name='logout'),

]
