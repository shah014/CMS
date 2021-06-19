import django_filters
from .models import *
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):
    end_date = DateFilter(field_name="Created_at", lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
