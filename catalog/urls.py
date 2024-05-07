from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, detail_product, add_product, home_2

app_name = CatalogConfig.name

urlpatterns = [
    path('1/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', detail_product, name='detail_product'),
    path('add_product/', add_product, name='add_product'),
    path('2/', home_2, name='home_2'),
]
