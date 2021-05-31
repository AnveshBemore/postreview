from django.shortcuts import render,redirect
from .models import udetails
from .models import curntUser
from .models import postdb
from .form import ImageForm
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    msg={
        "msg_review":"",
        "msg_post":"",
    }
    return render(request,"index.html",msg)
def post(request):
    cuname=str(curntUser.objects.first())
    pdb=postdb.objects.all().exclude(uname=cuname)
    
    msg={
        "unam":cuname,
        "postsall":pdb,
    }
    return render(request,"post_post.html",msg)
    
def signup(request):
    return render(request,"post_signup.html")

def verifylogin(request):
    curntUser.objects.all().delete()
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
                crnt=curntUser(uname=un)
                crnt.save()
                print("hellllllllllooooooooooo thiiiiiiis     iiiiiiiiiiissssss "+un)
                print(str(un)+"]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                return redirect("post_post")
        msg={
            "msg":"not a user please signup",
        }
        return render(request,"post_signup.html",msg)
    return redirect("post_post")


def signupdb(request):
    curntUser.objects.all().delete()
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
            crnt=curntUser(uname=unam)
            crnt.save()
            print("signup login------------------- uname"+unam+"  pasw "+password)
            ude.save()
        else:            
            user={
                "msg_post":"*already user please login",
                "msg_review":"",
                "unam":unam

            }
            return render(request,"post_post.html",user)
        return redirect("post_post")

    return redirect("post_post")
    # return redirect("")
def new_post(request):
    cuname=curntUser.objects.first()
    # for i in cuname:
    print("unameee  "+str(cuname)+" -----------------------")
    msg={
        "unam":str(cuname),
    }
    return render(request,"new_post.html",msg)

def new_post_add_db(request):
    if request.method=="POST" and request.FILES["img-choose-file"]:
        cuname=str(curntUser.objects.first())
        imgp=request.FILES["img-choose-file"]
        capt=request.POST["caption"] 
        fs = FileSystemStorage()
        filename = fs.save(imgp.name, imgp)
        pdb=postdb(uname=cuname,post_img=imgp.name,post_caption=capt)
        pdb.save()
        return redirect("post_post")

def my_posts(request):
    cuname=str(curntUser.objects.first())
    print(cuname+" ----------------------------")
    pdball=postdb.objects.filter(uname=cuname)
    return render(request,"my_posts.html",{"postsall":pdball,"unam":cuname})

def delete_post(request):
    unam=request.GET["uname"]
    img=request.GET["img"]
    cap=request.GET["caption"]
    pdb=postdb.objects.filter(post_img=img,post_caption=cap).delete()
    return redirect("new_post")

def update_post(request):
    unam=request.GET["uname"] 
    img=request.GET["img"]
    cap=request.GET["caption"]
    id=request.GET["id"]
    
    print(cap+" -------------")
    return render(request,"update_post.html",{"capval":cap,"id":id,"unam":unam})
def update_post_db(request):
    if request.method=="POST" and request.FILES["img-choose-file"]:
        cuname=str(curntUser.objects.first())
        imgp=request.FILES["img-choose-file"]
        capt=request.POST["caption"]
        id=request.POST["id"]
        print("id --------------- "+id)
        fs = FileSystemStorage()
        filename = fs.save(imgp.name, imgp)
        # pdb=postdb.objects.get(id=id)
        # pdb.uname=cuname
        # pdb.save()
        # pdb.post_img=imgp.name
        # pdb.save()
        # pdb.post_caption
        # pdb.save()
        pdb=postdb.objects.filter(id=id).update(post_img=imgp.name)
        pdb=postdb.objects.filter(id=id).update(post_caption=capt)

        return redirect("post_post")
    return redirect("post_posts")