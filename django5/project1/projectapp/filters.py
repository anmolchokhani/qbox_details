import django_filters
from .models import ClientData

class ClientDataFilter(django_filters.FilterSet):

    class Meta:
        name= django_filters.CharFilter(lookup_expr='contains')
        model=ClientData
        fields={

            'name':['contains'],
        }

