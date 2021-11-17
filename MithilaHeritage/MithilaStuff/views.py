from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import BlogModel
# Create your views here.
from MithilaStuff.models import Categories, Contact, Material
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
def index(request):
    return render(request,'MithilaStuff/index.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content) <4:
            messages.error(request,"Please Fill the Form Correctly ")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your Message has been successfully sent. ")


    return render(request,'MithilaStuff/contact.html')



def seeMithilaStuff(request):
    allStuff=Categories.objects.all()
    context={'allStuff':allStuff}
    return render(request,'MithilaStuff/seeMithilaStuff.html',context)

def mithila_World(request,type):
    #allStuff=Categories.objects.all()
    #id=Categories.objects.filter(type=type).values('pk')
    id =Categories.objects.filter(type=type).values('id')[0]['id']
    desc=Categories.objects.filter(type=type).values('desc')[0]['desc']
    type=Categories.objects.filter(type=type).values('type')[0]['type']
    content=Material.objects.filter(type_id=id)
    
    context={'content':content,'desc':desc,'type':type}
    return render(request,'MithilaStuff/mithila_World.html',context)
    
def search(request):
    query=request.GET['query']
    if len(query)>80:
        allPosts=BlogModel.objects.none()
    else:
        allPostsTitle= BlogModel.objects.filter(title__icontains=query)
        #allPostsAuthor= BlogModel.objects.filter(user__icontains=query)
        allPostsContent =BlogModel.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent,allPostsTitle)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    context={'allPosts':allPosts,'query': query}
    return render(request,'MithilaStuff/search.html',context)


def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #----
        if len(username)<6 or len(username)>15 :
            messages.error(request, " Your user name must be under 6 to 15 characters")
            return redirect('MithilaStuffHome')

        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('MithilaStuffHome')
        if User.objects.filter(username=username).exists():
           messages.error(request, "Username Already Taken")
           return redirect('MithilaStuffHome')

        if User.objects.filter(email=email).exists():
           messages.error(request, "Email Already Taken")
           return redirect('MithilaStuffHome')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('MithilaStuffHome')
    else:
        return HttpResponse('404 - Not found')

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, " Successfully Logged In.")
            return redirect('MithilaStuffHome')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('MithilaStuffHome')

    else:
        return HttpResponse('404 - Not found')
def handleLogout(request):
    logout(request)
    messages.success(request, " Successfully Logged Out.")
    return redirect('MithilaStuffHome')
