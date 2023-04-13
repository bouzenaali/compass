from django.contrib import admin
from django.urls import path, include
from accounts.urls import *
from auth.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth.urls)),
    path('accounts', include(accounts.urls))
]
