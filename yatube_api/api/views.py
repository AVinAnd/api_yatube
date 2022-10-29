from django.core.exceptions import PermissionDenied
from rest_framework import viewsets

from posts.models import Post, Group, Comment

from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """При создании поста указать пользователя как автора"""
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        """Проверка доступа пользователя к удалению поста"""
        if self.request.user != instance.author:
            raise PermissionDenied('Удаление чужих постов запрещено')
        super(PostViewSet, self).perform_destroy(instance)

    def perform_update(self, serializer):
        """Проверка доступа пользователя к изменению поста"""
        if self.request.user != serializer.instance.author:
            raise PermissionDenied('Изменение чужих постов запрещено')
        super(PostViewSet, self).perform_update(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получаем комментарии конкретного поста"""
        post_id = self.kwargs.get('post_id')
        comments_queryset = Comment.objects.filter(post=post_id)
        return comments_queryset

    def perform_create(self, serializer):
        """При создании комментария указать пользователя как автора"""
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user, post_id=post_id)

    def perform_destroy(self, instance):
        """Проверка доступа пользователя к удалению комментария"""
        if self.request.user != instance.author:
            raise PermissionDenied('Удаление чужих комментариев запрещено')
        super(CommentViewSet, self).perform_destroy(instance)

    def perform_update(self, serializer):
        """Проверка доступа пользователя к изменению комментария"""
        if self.request.user != serializer.instance.author:
            raise PermissionDenied('Изменение чужих комментариев запрещено')
        super(CommentViewSet, self).perform_update(serializer)
