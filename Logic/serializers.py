
from rest_framework import serializers

from Allmodels.models import Comment, PostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
    
        model = PostModel
        fields = ("Title","Description","Link","Level","No_of_videos")

class DetailPostSerializer(serializers.ModelSerializer):
    class Meta:
        depth =1
        model = PostModel
        fields = ("__all__")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Comment
        fields = ("Commented_By","Content","Post")
class DetailCommentSerializer(serializers.ModelSerializer):
    class Meta:
        depth =1
        model = Comment
        fields = ("Commented_By","Content","Post")
