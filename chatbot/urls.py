from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('signup/', views.authView, name='signup'),
    path('', views.home_view, name='home'),
    path('chat/', views.home_view, name='chat'),
   
]

