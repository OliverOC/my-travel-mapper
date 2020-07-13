from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<slug:slug>/', views.UserDetail.as_view(), name='profile'),
    path('signup/', views.signup, name='signup'),
    path('update/user/<slug:slug>/', views.EditUser.as_view(), name='update'),
    path('update/profile-pic/<slug:slug>/', views.EditUserProfile.as_view(), name='profile_pic'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_update.html'), name='password_update'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
]