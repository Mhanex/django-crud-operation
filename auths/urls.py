
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.createAccount, name='signup'),
    path('signin/', views.memberLogin, name='signin'),
    path('dashboard/', views.userDashboard, name='dashboard'),
    path('logout/', views.logUserOut, name='signout'),
]


