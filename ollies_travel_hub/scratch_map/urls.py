from django.urls import path
from . import views

app_name = 'scratch_map'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('test/', views.test_view, name='test'),
    path('add-trip/', views.add_trip_form_view, name='add_trip'),
]