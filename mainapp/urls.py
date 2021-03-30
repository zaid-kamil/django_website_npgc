from django.urls.conf import path
from .views import index
from .views import show_data

urlpatterns = [
    path('', index, name='home'),
    path('view/', show_data, name='show_data'),
]