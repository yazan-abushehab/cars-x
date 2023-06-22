from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Car


class CarListView(ListView):
    template_name = "car/car-list.html"
    model = Car


class CarDetailView(DetailView):
    template_name = "car/car-detail.html"
    model = Car


class CarCreateView(CreateView):
    template_name = "car/car-create.html"
    model = Car
    fields = ['name', 'purchaser', 'description']


class CarUpdateView(UpdateView):
    template_name = "car/car-update.html"
    model = Car
    fields = ['name', 'purchaser', 'description']


class CarDeleteView(DeleteView):
    template_name = "car/car-delete.html"
    model = Car
    success_url = reverse_lazy("car_list")  