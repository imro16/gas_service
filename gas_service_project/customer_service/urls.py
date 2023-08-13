from django.urls import path
from . import views

app_name = 'customer_service'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('track-request/', views.track_request, name='track_request'),
    path('submit-request/', views.submit_request_view, name='submit_request'),
    path('request-tracking/', views.request_tracking_view, name='request_tracking'),

]
