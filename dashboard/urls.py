from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home, name="home"),
   path('register', views.register, name="register"),
   path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html', redirect_authenticated_user=True), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('password_change/', auth_views.PasswordChangeView.as_view(template_name='dashboard/change_password.html'), name='password_change'),
   path('config/password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='dashboard/password_change_done.html'), name='password_change_done'),
   path('profile/<int:pk>', views.profile, name='profile'),
   path('employee/', views.employee, name='employee'),
   path('add/', views.addProfile, name='add'),
   path('edit/', views.editProfile, name='edit'),
   path('edit/<str:username>', views.editProfileAdmin, name='edit'),
   path('delete/<int:pk>', views.deleteProfile, name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






