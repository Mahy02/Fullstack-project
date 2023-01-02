"""django_FS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('login/admin/', admin.site.urls),
    path('login/', user_views.CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', user_views.signup, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/confirm', user_views.request_admin_authority, name='confirm_req'),
    path('edit-database/', user_views.edit_database, name='edit_database'),
    path('', include('FiFa.urls')),

    #path('admin/login', auth_views.LoginView.as_view(template_name='users/login.html'), name='custom_login_page_admin'),
     #path('fifa/', include('FiFa.urls'),
    #path('editdata/', user_views.editdata, name='editdata'),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   #login and logout areclass based views
    
]
admin.site.site_header = "FIFA Admin"
admin.site.site_title = "FIFA QATAR Admin"
admin.site.index_title = "FIFA Admin"
