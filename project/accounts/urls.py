from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
path('register/', views.SignUp.as_view(), name='register'),
path('login/', LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True,), name='login'),
path('logout/', login_required(LogoutView.as_view(template_name='accounts/logout.html')),name='logout'),
path('update_profile/<int:pk>/', login_required(views.ProfileUpdateView.as_view()), name='update_profile'),
path('show_profile/', login_required(views.ShowProfileView.as_view()), name='show_profile'),
path('create_profile/', login_required(views.CreateProfileView.as_view()), name='create_profile')
]