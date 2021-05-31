from django.shortcuts import render,redirect
from .models import udetails
from django.apps import apps
postdbr = apps.get_model('post', 'postdb')
cuser=apps.get_model("post","curntUser")
from .models import myreviews
from .models import crntReviewUser
# Create your views here.
def index(request):
    
    msg={
        "msg_post":"",
        "msg_review":"",
    }
    return render(request,"index.html",msg)
def review(request):
    crunam=str(crntReviewUser.objects.first())
    pdb=postdbr.objects.all()
    msg={
        "unam":crunam,
        "postsall":pdb,
    }
    return render(request,"review.html",msg)


def post(request):
    return render(request,"review_post.html")
    
def signup(request):
    return render(request,"review_signup.html")

def verifylogin(request):
    crntReviewUser.objects.all().delete()
    if request.method=="POST":
        unam=request.POST["username"]
        password=request.POST["password"]
        prod=udetails(uname=unam,password=password)
        search=udetails.objects.filter(uname=unam)
        for i in search:
            print("-------------------"+str(i)+"---------")
            if i.password==password:
                print(i.password)
                # un=udetails.objects.filter(uname=unam)

                un=unam
                crtu=crntReviewUser(uname=un)
                crtu.save()
                print("hellllllllllooooooooooo thiiiiiiis     iiiiiiiiiiissssss "+un)
                print(str(un)+"]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                return redirect("review")
        msg={
            "msg":"not a user please signup",
        }
        return render(request,"review_signup.html",msg)
    return redirect("review")


def signupdb(request):
    crntReviewUser.objects.all().delete()
    print(request.method+"------------------")
    if request.method=="POST":
        print("entered post")
        unam=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        search=udetails.objects.filter(uname=unam)
        print(search)
        if not search:
            
            ude=udetails(uname=unam,password=password,email=email)
            print("signup login------------------- uname"+unam+"  pasw "+password)
            ude.save()
            cr=crntReviewUser(uname=unam)
            cr.save()
        else:            
            user={
                "msg_reivew":"*already user please signup",
                "msg_post":"",
                "unam":unam,
            }
            return render(request,"index.html",msg)
        return redirect("review")

    return redirect("review")
    # return redirect("")
def new_review(request):
    crunam=str(crntReviewUser.objects.first())    
    pdb=postdbr.objects.all()
    return render(request,"new_review.html",{"postsall":pdb,"unam":crunam,})
def add_review(request):
    un=request.GET["uname"]
    img=request.GET["img"]
    cap=request.GET["caption"]
    rev=request.GET["reviewimg"]
    print(rev+" ------------------rev")
    id=request.GET["id"]
    # imgd=postdbr.objects.get(post_img=img)

    # x=imgd.post_reviews+" --"+rev 
    # imgd.post_reviews=x
    # imgd.save(updated_fields=["post_reviews"])

    imgd=postdbr.objects.get(id=id)
    print(imgd.post_reviews+" --------------before------------")
    imgd.post_reviews=imgd.post_reviews+" "+rev
    imgd.save()
    imgd=postdbr.objects.get(id=id)
    print(imgd.post_reviews+" --------------asfafgfagderet------------")
    myrev=myreviews(postuname=un,postimg=img,postcaption=cap,review=rev)
    myrev.save()
    # print(x+" --------------------------")
    return redirect("review")
def my_reviews(request):
    crunam=str(crntReviewUser.objects.first())
    myrev=myreviews.objects.all()
    return render(request,"my_reviews.html",{"postsall":myrev,"unam":crunam,})