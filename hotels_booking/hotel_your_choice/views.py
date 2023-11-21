# hotel_your_choice/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            # Redirect to the home page or another desired page
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to the home page or another desired page
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def password_reset_view(request):
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        # Process the form submission if needed
        pass

    return render(request, 'password_reset.html', {'form': form})


def home(request):
    return render(request, 'base_generic.html')


def book_hotel(request, hotel_id):
    # Add your logic for booking a hotel
    return render(request, 'hotel_your_choice/book_hotel.html', {'hotel_id': hotel_id})


def registration_view(request):
    return render(request, 'registration.html')


def login_view(request):
    return render(request, 'login.html')


def password_reset_view(request):
    return render(request, 'password_reset.html')


@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'hotel_your_choice/dashboard.html', {'bookings': bookings})


@login_required
def book_hotel(request, hotel_id):
    if request.method == 'POST':
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        guests = request.POST['guests']

        hotel = Hotel.objects.get(pk=hotel_id)

        Booking.objects.create(
            user=request.user,
            hotel=hotel,
            check_in=check_in,
            check_out=check_out,
            guests=guests
        )

        return redirect('dashboard')

    return render(request, 'hotel_your_choice/booking.html', {'hotel_id': hotel_id})
