from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Dish
from .forms import SortingForm

# Create your views here.

class DishList(ListView):

    template_name = 'index.html'
    model = Dish
    paginate_by = 6

    def dispatch(self, request, *args, **kwargs):
        self.form = SortingForm(request.GET)
        self.form.is_valid()
        return super(DishList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Dish.objects.all()
        if self.form.cleaned_data.get('for_vegan'):
            queryset = queryset.filter(vegan=self.form.cleaned_data.get('for_vegan'))
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data.get('sort_field'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DishList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context
