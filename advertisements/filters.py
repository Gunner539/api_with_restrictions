from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # created_at = DateTimeFromToRangeFilter()
    created_at = DateFromToRangeFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        # fields = ['created_at']
        fields = ['creator', 'created_at', 'status']
