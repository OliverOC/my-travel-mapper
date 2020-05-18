from django.shortcuts import render, redirect
from .models import Country, Trip
from .forms import AddTrip
from django.contrib.auth.decorators import login_required


def home_view(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'scratch_map/home.html', context)


@login_required
def test_view(request):
    country_list = Country.objects.all()
    trip_list = Trip.objects.all()
    context = {
        'title': 'Test',
        'country': trip_list,
    }
    return render(request, 'scratch_map/test.html', context)


@login_required
def add_trip_form_view(request):
    form = AddTrip()

    if request.method == 'POST':
        form = AddTrip(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home_view(request)

        else:
            print("ERROR: FORM INVALID")

    context = {
        'title': 'Add Trip',
        'form': form,
    }
    return render(request, 'scratch_map/add_trip.html', context)

