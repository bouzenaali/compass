from django.contrib import admin
from django.urls import path, include
from accounts.urls import *
from authentication.urls import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('accounts/', include('accounts.urls')),
    #
    path('courses/',include('courses.urls')),
]
