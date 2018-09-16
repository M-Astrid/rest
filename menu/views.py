from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Dish

# Create your views here.

class DishList(ListView):

    template_name = 'index.html'
    model = Dish
    paginate_by = 2

    def dispatch(self, request, *args, **kwargs):
        self.for_vegan = request.GET.get('for_vegan')
        self.sort_field = request.GET.get('sort_field')
        return super(DishList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Dish.objects.all()
        if self.for_vegan:
            queryset = queryset.filter(vegan=True)
        if self.sort_field:
            queryset = queryset.order_by(self.sort_field)
        return queryset
