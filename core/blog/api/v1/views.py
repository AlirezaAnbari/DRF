from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from ...models import Post

@api_view(['GET', 'POST'])
def postList(request):
    
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post.delete()
        x=[m for m in dir(status) if m.startswith('HTTP')]
        print(x)
        return Response({"detail":"Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
