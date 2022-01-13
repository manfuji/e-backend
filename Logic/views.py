from django.http import HttpResponse
from rest_framework import serializers,viewsets
from Allmodels.models import Comment, PostModel

from Logic.serializers import CommentSerializer, DetailCommentSerializer, DetailPostSerializer, PostSerializer
# Create your views here.
class ListPost(viewsets.ModelViewSet):
    serializer_class = DetailPostSerializer
    queryset = PostModel.objects.all()

class CreatePost(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def Post(request,self,format=None):
        Title = request.data["title"]
        Description =request.data["description"]
        Link =request.data["link"]
        Level =request.data["level"]
        No_of_videos =request.data["video"]
        if Title !="" and Description != "" and Link !="" and Level != "" and No_of_videos != "":
            PostModel.objects.create(Title=Title,Description=Description,Link=Link,Level=Level,No_of_videos=No_of_videos)
        else:
            return HttpResponse ({"Message":"Post Was not created successfully: Due to Empty field"},status=401)

        return HttpResponse ({"Message":"Post Was created successfully"},status=200)

class ListComment(viewsets.ModelViewSet):
    queryset = Comment.objects.all();
    serializer_class = DetailCommentSerializer

class createComment(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer

    def CreateComment(request,self,format=None):
        Commented_by = request.data["user"]
        Content = request.data["content"]
        Post = request.data["post"]
        if Commented_by !="" and Content !="" and Post != "":
            Comment.objects.create(Commented_by= Commented_by,Content=Content,Post=Post)

        else:
            return HttpResponse ({"Message":"Post Was not created successfully: Due to Empty field"},status=401)

