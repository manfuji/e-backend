
from django.urls import path
from rest_framework import routers

from Logic.views import CreatePost, ListComment, ListPost, createComment

app_name = "Logic"

router = routers.DefaultRouter()

router.register("posts",ListPost,"posts")
router.register("createPost",CreatePost,"createPost")
router.register("comment",ListComment,"comments")
router.register("createComment",createComment,"createComment")

urlpatterns = [
    # path("post",ListPost.as_view(),"post"),
]
urlpatterns+= router.urls
