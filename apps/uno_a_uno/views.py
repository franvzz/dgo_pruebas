from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.uno_a_uno.models import Restaurant, Place, Waiter

# Create your views here.
class UnoAUnoList(ListView):
    model = Place
    template_name = 'uno_a_uno/list.html'
    context_object_name = 'places'
    ordering = ['place']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UnoAUnoList, self).get_context_data(**kwargs)
        if 'OneToOne_menu' not in context:
            context['OneToOne_menu'] = 'current'
        if 'totalPlaces' not in context:
            context['totalPlaces'] = Place.objects.all().count()
        return context

class UnoAUnoCreate(CreateView):
    pass

class UnoAUnoDetail(DetailView):
    pass

class UnoAUnoUpdate(UpdateView):
    pass

class UnoAUnoDelete(DeleteView):
    pass
