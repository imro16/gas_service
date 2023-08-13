from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views module from your project's directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default_view, name='default_view'),  # Default view for root URL
    path('customer-service/', include('customer_service.urls')),
]
