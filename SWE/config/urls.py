from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from limbo.forms import CustomAuthForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(
         template_name='registration/login.html', authentication_form=CustomAuthForm)),
    
    path('', include('limbo.urls')),

]
