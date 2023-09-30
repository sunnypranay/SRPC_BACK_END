from django.urls import path

from .views import home, populate_round_1_table, populate_round_2_table, validate_token

app_name = 'home'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('populate_round_1_table/', populate_round_1_table.as_view(), name='populate_round_1_table'),
    path('populate_round_2_table/', populate_round_2_table.as_view(), name='populate_round_2_table'),
    path('validate_token/', validate_token.as_view(), name='validate_token')
]
