from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from .models import Country, Trip
from .forms import TripForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()


def landing_page_view(request):
    context = {
        'title': '',
    }
    return render(request, 'scratch_map/landing_page.html', context)


def home_view(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'scratch_map/home.html', context)


class MapListView(LoginRequiredMixin, ListView):
    model = Trip
    context_object_name = 'trips'
    template_name = 'scratch_map/map_list.html'

    def get_queryset(self):
        try:
            self.trips_user = User.objects.prefetch_related('trips').get(username__iexact=self.request.user.username)
        except User.DoesNotExist:
            raise Http404
        else:
            return self.trips_user.trips.order_by('year_visited').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Map'
        return context


class TripListView(LoginRequiredMixin, ListView):
    model = Trip
    context_object_name = 'trips'

    def get_queryset(self):
        try:
            self.trips_user = User.objects.prefetch_related('trips').get(username__iexact=self.request.user.username)
        except User.DoesNotExist:
            raise Http404
        else:
            return self.trips_user.trips.order_by('year_visited').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Photos'
        return context


class CreateTripView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'scratch_map/home.html'
    success_url = "/photo-cards/"

    form_class = TripForm

    model = Trip

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class EditTrip(UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'scratch_map/trip_update.html'


class DeleteTrip(DeleteView):
    model = Trip
    template_name = 'scratch_map/trip_confirm_delete.html'
    success_url = reverse_lazy('scratch_map:photo_cards')


