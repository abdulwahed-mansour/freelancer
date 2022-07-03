
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('workshop/', include('workshop.urls')),
    path('admin/', admin.site.urls),
]
