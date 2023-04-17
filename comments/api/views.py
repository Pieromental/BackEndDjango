from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsAdminOrReadAndCreateOnly
from django_filters.rest_framework import DjangoFilterBackend

class CommentApiView(ModelViewSet):
    permission_classes=[IsAdminOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends=[OrderingFilter,DjangoFilterBackend]
    ordering=['-created_at']
    filterset_fields=['post']
