from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, detail_product, add_product, home_1, home_2

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('1/', home_1, name='home_1'),
    path('contacts/', contacts, name='contacts'),
    path('detail/<int:pk>/', detail_product, name='detail_product'),
    path('add_product/', add_product, name='add_product'),
    path('2/', home_2, name='home_2'),
]
