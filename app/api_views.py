from django.contrib.auth.hashers import make_password
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from app.models import Post
from app.serializers import UserSerializer, PostSerializer


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data.dict()
        hash_pwd = make_password(user['password'])
        user['password'] = hash_pwd
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListsPostsAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RUDPostAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def retrieve(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs['pk'])
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        snippet = self.get_object(pk)
        if snippet.author != request.user.id:
            return Response({"error": "only author can update post"}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.dict()

        if not data.get('title'):
            data['title'] = snippet.title

        if not data.get('text'):
            data['text'] = snippet.title

        data['author'] = snippet.author.id
        data['liked'] = snippet.liked
        data['liked'] = snippet.unliked
        data['liked'] = snippet.total_liked

        serializer = PostSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        snippet = self.get_object(kwargs['pk'])
        if snippet.author == request.user.id:
            snippet.delete()
            return Response({"message": 'post deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class LikePostAPI(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        print(pk)
        try:
            post = Post.objects.get(id=pk)
            post.like()
        except Exception as e:
            return Response({"message": 'post liked'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)


class UnlikePostAPI(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            post = Post.objects.get(id=pk)
            post.unlike()
        except Exception as e:
            return Response({"message": 'post unliked'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)
