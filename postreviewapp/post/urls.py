from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("post_post",views.post,name="post_post"),
    path("delete_post",views.delete_post,name="delete_post"),    
    path("post_signup",views.signup,name="post_signup"),
    path("post_verifylogin",views.verifylogin,name="post_verifylogin"),
    path("post_signupdb",views.signupdb,name="post_signupdb"),
    path("new_post",views.new_post,name="new_post"),
    path("new_post_add_db",views.new_post_add_db,name="new_post_add_db"),
    path("my_posts",views.my_posts,name="my_posts"),
    path("update_post",views.update_post,name="update_post"),
    path("update_post_db",views.update_post_db,name="update_post_db"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
