from django.urls import path, include  # Add this line
from . import views

app_name = 'hotel_your_choice'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('accounts/', include('allauth.urls')),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
]
