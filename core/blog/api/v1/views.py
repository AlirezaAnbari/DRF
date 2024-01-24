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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, id=id, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)
