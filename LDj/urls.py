
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Home/', include('Home.urls')),
    path('', include('Home.urls')),
    path('admin/', admin.site.urls),
]

