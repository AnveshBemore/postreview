from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from post import views as vc

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("post.urls")),
    path("",include("review.urls")),    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
