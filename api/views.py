from .models import Blog
from rest_framework import generics
from .Serialazers import BlogSerializer


class ListCreateBlogs(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


list_blogs = ListCreateBlogs.as_view()


class RetrieveBlog(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


retrieve_blog = RetrieveBlog.as_view()


class UpdateBlog(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


update_blog = UpdateBlog.as_view()


class DeleteBlog(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


delete_blog = DeleteBlog.as_view()
