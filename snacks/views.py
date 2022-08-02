from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class SnackListView(ListView):
    template_name = 'list_view.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'detail_view.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'create_view.html'
    model = Snack
    fields = ["title", "purchaser", "description"]


class SnackUpdateView(UpdateView):
    template_name = 'update_view.html'
    model = Snack
    fields = ["title", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    template_name = 'delete_view.html'
    model = Snack
    success_url = reverse_lazy('list_view')
