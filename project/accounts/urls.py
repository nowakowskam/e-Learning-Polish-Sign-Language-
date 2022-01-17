from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
path('register/', views.SignUp.as_view(), name='register'),
path('login/', LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True,), name='login'),
path('logout/', LogoutView.as_view(template_name='accounts/logout.html'),name='logout')
# path('login', views.SignIn.as_view(), name='login')
]