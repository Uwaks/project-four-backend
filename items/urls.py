from django.urls import path
from .views import CommentListView, ItemDetailView, ItemListView

urlpatterns = [
    path('', ItemListView.as_view()),
    path('<int:pk>/', ItemDetailView.as_view()),
    path('<int:item_pk>/comments/', CommentListView.as_view())
]