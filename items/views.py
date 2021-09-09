
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Item
from .serializers import ItemSerializer

class ItemListView(ListCreateAPIView):
    '''List View for /items INDEX CREATE'''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(RetrieveUpdateDestroyAPIView):
    '''Detail View for /items/id SHOW UPDATE DELETE'''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    