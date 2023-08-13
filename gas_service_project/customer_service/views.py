from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ServiceRequest


@login_required
def submit_request(request):
    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        request_details = request.POST.get('request_details')
        customer = request.user.customer
        ServiceRequest.objects.create(customer=customer, service_type=service_type, request_details=request_details)
        return render(request, 'customer_service/request_submitted.html')
    return render(request, 'customer_service/submit_request.html')




def submit_request_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})


@login_required
def request_tracking_view(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customer_service/request_tracking.html', {'user_requests': user_requests})


@login_required
def track_request(request):
    customer = request.user.customer
    service_requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'customer_service/track_request.html', {'service_requests': service_requests})


def landing_page(request):
    return render(request, 'customer_service/landing_page.html')


def default_view(request):
    # Your view logic here
    return render(request, 'default.html')