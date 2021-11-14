from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import *
# Create your views here.
from blog.models import  BlogComment
from django.contrib import messages
from blog.templatetags import extras
def blogHome(request):
    allPosts=BlogModel.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/temp.html',context)


def blogPost(request, slug): 
    post=BlogModel.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):   
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= BlogModel.objects.get(sno=postSno)
        parentSo=request.POST.get('parentSno')
        if parentSo=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent=BlogComment.objects.get(sno=parentSo)
            comment=BlogComment(comment= comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")


def add_blog(request): 
    context={'form':BlogForm}
    try:
        if request.method== 'POST':
            form=BlogForm(request.POST)
            image=request.FILES['image']
            title=request.POST.get('title')
            user=request.user
            print(image,title,user)
            if form.is_valid():
                content=form.cleaned_data['content']
            blog_obj= BlogModel(user=user,title=title,content=content,image=image)
            blog_obj.save()
            messages.success(request, "Your blog has been posted successfully")
            return redirect('/blog/addBlog')
    except Exception as e:
        print(e)
    return render(request,'blog/addBlog.html',context)

def seeBlog(request):
    context={}
    try:
        blog_objs=BlogModel.objects.filter(user=request.user)
        context['blog_objs']=blog_objs
    except Exception as e:
        print(e)
    return render(request,'blog/seeBlog.html',context)

def blogEdit(request,slug):
    context={}
    try:
        blog_obj=BlogModel.objects.get(slug=slug)
        if blog_obj.user!=request.user:
            messages.error(request, "You do not have permission to delete this.")
            return redirect('/blog/seeBlog')
        initial_dict={'content':blog_obj.content}
        form=BlogForm(initial=initial_dict)
        context['blog_obj']=blog_obj
        context['form']=form
        if request.method== 'POST':
            form=BlogForm(request.POST)
            image = request.FILES['image']
            title=request.POST.get('title')
            user=request.user
            if form.is_valid():
                content=form.cleaned_data['content']
            # blog_obj= BlogModel(user=user,title=title,content=content,image=image)
            # blog_obj.save()
            blog_obj.title=title
            blog_obj.content=content
            blog_obj.image=image
            blog_obj.save()
            messages.success(request, "Your blog has been Updated successfully")
            return redirect('/blog/seeBlog')
    except Exception as e:
        print(e,)
    return render(request,'blog/editBlog.html',context)
def blogDelete(request,sno):
    try:
        blog_obj=BlogModel.objects.get(sno=sno)
        if blog_obj.user==request.user:
            blog_obj.delete()
            messages.success(request, "Your blog has been deleted successfully")

    except Exception as e:
        print(e)
    return redirect('/blog/seeBlog')