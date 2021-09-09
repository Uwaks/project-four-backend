from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Item
from .serializers import CommentSerializer, ItemSerializer

class ItemListView(ListCreateAPIView):
    '''List View for /items INDEX CREATE'''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(RetrieveUpdateDestroyAPIView):
    '''Detail View for /items/id SHOW UPDATE DELETE'''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CommentListView(APIView):
    ''' List View for /characters/characterId/comments CREATE comments'''

    def post(self, request, item_pk):
        request.data['item'] = item_pk
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
