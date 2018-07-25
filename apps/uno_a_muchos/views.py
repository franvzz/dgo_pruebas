from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.uno_a_muchos.models import Pet, Vaccine, Owner

# Create your views here.
class UnoAMuchosList(ListView):
    model = Pet
    template_name = 'uno_a_muchos/list.html'
    context_object_name = 'pets'
    ordering = ['name']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UnoAMuchosList, self).get_context_data(**kwargs)
        if 'OneToMany_menu' not in context:
            context['OneToMany_menu'] = 'current'
        if 'totalPets' not in context:
            context['totalPets'] = Pet.objects.all().count()
        return context

class UnoAMuchosCreate(CreateView):
    pass

class UnoAMuchosDetail(DetailView):
    pass

class UnoAMuchosUpdate(UpdateView):
    pass

class UnoAMuchosDelete(DeleteView):
    pass
