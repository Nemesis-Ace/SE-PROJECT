from limbo import views
from django.urls import include, path, re_path

app_name='basic'

urlpatterns = [
    path('login/',views.index,name='login'),

]
