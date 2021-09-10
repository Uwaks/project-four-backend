from rest_framework.fields import ReadOnlyField
from items.serializers import ItemSerializer, CommentSerializer, NestedUserSerializer, PopulatedItemSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
# import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})

        # try:
        #     validation.validate_password(password=password)
        # except ValidationError as err:
        #     raise ValidationError({'password': err.messages})

        data['password'] = make_password(password)

        return data


    class Meta:
        model = User
        fields ='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    liked_items = ItemSerializer(many=True)
    comments_made = CommentSerializer(many=True)
    item_to_sell = ItemSerializer(many=True)
    item_bought = PopulatedItemSerializer(many=True)
    followed_by = NestedUserSerializer(many=True)


    class Meta:
        model = User
        # fields = ('username', 'email', 'profile_image', 'liked_items', 'comments_made', 'item_to_sell')    
        fields = ('username', 'email', 'profile_image', 'liked_items', 'comments_made', 'item_to_sell', 'item_bought', 'followed_by')    