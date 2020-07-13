from django.urls import path
from . import views

app_name = 'scratch_map'

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('home/', views.home_view, name='home'),
    path('photo-cards/', views.TripListView.as_view(), name='photo_cards'),
    path('map/', views.MapListView.as_view(), name='map'),
    path('add-trip/', views.CreateTripView.as_view(), name='add_trip'),
    path('edit-trip/<int:pk>/', views.EditTrip.as_view(), name='edit_trip'),
    path('delete-trip/<int:pk>/', views.DeleteTrip.as_view(), name='delete_trip'),
]