import django_filters
import storemodels.models
from django.db.models import Q


class Product_filter(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Диапазон цен')
    available = django_filters.BooleanFilter(method='filter_available', label= 'В наличии' )
    term = django_filters.CharFilter(method='filter_term', label='Поиск по названию и описанию')
    ordering = django_filters.OrderingFilter(fields=(('price', 'price'),),label='Сортировка по цене',field_labels={'price': 'Цена',},choices=(('price', 'По возрастанию цены'),('-price', 'По убыванию цены'),),)

    class Meta:
        model = storemodels.models.Product
        fields = ['category']


    def filter_available(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock=0)


    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(name__icontains=term) | Q(description__icontains=term)

        return queryset.filter(criteria).distinct()

