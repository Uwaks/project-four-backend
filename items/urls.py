from django.urls import path
from .views import CommentListView, ItemListView, ItemDetailView, ItemCreateView, CommentDetailView, ItemLikeView  

urlpatterns = [
    path('', ItemListView.as_view()),
    path('new/', ItemCreateView.as_view()),
    path('<int:pk>/', ItemDetailView.as_view()),
    path('<int:item_pk>/comments/', CommentListView.as_view()),
    path('<int:item_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
    path('<int:item_pk>/like/', ItemLikeView.as_view())
]