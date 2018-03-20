
from django.contrib import admin
from django.urls import path, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),  # browseable API support
]
