from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RoomBooking
from datetime import datetime

def index(request):
    context = {
        'title': 'Devki & Krishna Temple',
        'subtitle': 'About Devasthan',
    }
    return render(request, 'about/index.html', context)

def book_room(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            room_type = request.POST.get('room_type')
            check_in = datetime.strptime(request.POST.get('check_in'), '%Y-%m-%d').date()
            check_out = datetime.strptime(request.POST.get('check_out'), '%Y-%m-%d').date()
            guests = int(request.POST.get('guests'))
            special_requests = request.POST.get('special_requests', '')

            # Create booking
            booking = RoomBooking.objects.create(
                name=name,
                email=email,
                phone=phone,
                room_type=room_type,
                check_in=check_in,
                check_out=check_out,
                guests=guests,
                special_requests=special_requests
            )

            # Render confirmation page
            return render(request, 'about/confirmation.html', {'booking': booking})
        except Exception as e:
            messages.error(request, f'Booking failed: {str(e)}')
            return redirect('about:index')

    return redirect('about:index')