from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Group

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import OnlyAuthorEdit


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, OnlyAuthorEdit]

    def perform_create(self, serializer):
        """При создании поста указать пользователя как автора"""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, OnlyAuthorEdit]

    def get_queryset(self):
        """Получаем комментарии конкретного поста"""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments

    def perform_create(self, serializer):
        """При создании комментария указать пользователя как автора"""
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user, post_id=post_id)
