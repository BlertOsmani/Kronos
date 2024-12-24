import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    priority = django_filters.BaseInFilter(field_name="priority", lookup_expr="in")
    due_date = django_filters.DateFilter(field_name="due_date", lookup_expr='date')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Task
        fields = ['priority', 'due_date', 'created_at']