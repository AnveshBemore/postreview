from django.urls import path
from . import views
urlpatterns=[
    path("review",views.review,name="review"),
    path("review_signup",views.signup,name="review_signup"),
    path("review_verifylogin",views.verifylogin,name="review_verifylogin"),
    path("review_signupdb",views.signupdb,name="review_signupdb"),
    path("new_review",views.new_review,name="new_review"),
    path("add_review",views.add_review,name="add_review"),
    path("my_reviews",views.my_reviews,name="my_reviews"),
    
]