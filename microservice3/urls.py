from django.contrib import admin
from django.urls import path, include

admin.site.site_header='Microservice3-Admin'
admin.site.site_header = "Microservice3-Admin'"
admin.site.site_title = "MS3-Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
]
