from django_filters import rest_framework as filters
from accounts.models import User


class UserFilters(filters.FilterSet):
    date_joined = filters.DateTimeFilter(field_name='date_joined', lookup_expr='date')
    last_login = filters.DateTimeFilter(field_name='last_login', lookup_expr='date')

    class Meta:
        model = User
        fields = (
            'user_permission', 'is_active', 'date_joined', 'last_login',
        )


