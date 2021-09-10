from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Item, Comment
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    owner = NestedUserSerializer()

class SellerIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined')     

# class BuyerIDSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'date_joined') 

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PopulatedItemSerializer(serializers.ModelSerializer):
    comments = PopulatedCommentSerializer(many=True, read_only=True)
    liked_by = NestedUserSerializer(many=True, read_only=True)
    sold_by = SellerIDSerializer()
    # bought_by = BuyerIDSerializer(read_only=True)
    
    class Meta:
        model = Item
        fields = '__all__'

# class PopulatedSellerSerializer(ItemSerializer):
#     sold_by = SellerIDSerializer()        

# class SoldBySerializer(ItemSerializer):
#     sold_by = SellerIDSerializer        
