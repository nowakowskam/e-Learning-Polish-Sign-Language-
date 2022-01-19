from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns=[
path('register/', views.SignUp.as_view(), name='register'),
path('login/', LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True,), name='login'),
path('logout/', LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
path('update_profile/<int:pk>/', views.ProfileUpdateView.as_view(), name='update_profile'),
path('show_profile/', views.ShowProfileView.as_view(), name='show_profile'),
path('create_profile/', views.CreateProfileView.as_view(), name='create_profile')
]