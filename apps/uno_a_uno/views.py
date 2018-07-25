from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.uno_a_uno.models import Owner, Pet

# Create your views here.
class UnoAUnoList(ListView):
    model = Pet
    template_name = 'uno_a_uno/list.html'
    context_object_name = 'pets'
    ordering = ['name']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UnoAUnoList, self).get_context_data(**kwargs)
        if 'OneToOne_menu' not in context:
            context['OneToOne_menu'] = 'current'
        if 'totalPets' not in context:
            context['totalPets'] = Pet.objects.all().count()
        return context

class UnoAUnoCreate(CreateView):
    pass

class UnoAUnoDetail(DetailView):
    pass

class UnoAUnoUpdate(UpdateView):
    pass

class UnoAUnoDelete(DeleteView):
    pass
