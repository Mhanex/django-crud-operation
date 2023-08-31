
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Admin page honeypot URL
    path('admin/', include('admin_honeypot.urls')),

    #Actual admin page URL
    path('globalprotect/', admin.site.urls),
    
    #Apps URL
    path('', include('crud.urls')),
    path('auths/', include('auths.urls')),
]
