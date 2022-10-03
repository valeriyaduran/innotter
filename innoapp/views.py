from rest_framework import viewsets

from innoapp.models import Page, Post, Tag
from innoapp.serializers import PageSerializer, PostSerializer, TagSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(page=self.kwargs['page_pk'])


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(pages=self.kwargs['page_pk'])

