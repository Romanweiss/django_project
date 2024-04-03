from django.urls import path
from . import views


urlpatterns = [
    path('', views.AccountPage.as_view(), name='urlAccountPage'),
    path('auth/', views.AuthPage.as_view(), name='urlAuthPage'),
    path('reg/', views.RegPage.as_view(), name='urlRegPage'),
    path('logout/', views.Logout.as_view(), name='urlLogout'),
    path('logout/', views.Logout.as_view(), name='urlLogout'),
]
