from importlib.resources import contents
from telnetlib import AUTHENTICATION
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required 
from .models import POST, Topic, comment
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.http import HttpResponse
from .forms import UserCreationForm, PostForm,CommentForm,TopicForm



def LoginPage(request):
    page ='login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')


       try:
           user = User.objects.get(username=username)
       except:
           messages.error(request, 'User does not exist')

       user = authenticate(request, username= username, password =password)

       if user is not None:
           login(request,user)
           return redirect('home')
       else:
           messages.error(request, 'Username OR password is not right/does not exist')


    context={'page':page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post = POST.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
    )
    Topics = Topic.objects.all()
    context = {'POST': post,'Topics':Topics}
    return render(request, 'home.html', context)


def updatepost(request,pk):
    post = POST.objects.get(id=pk)
    form =PostForm(instance=post)
    topics = Topic.objects.all()
   
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.topic = request.POST.get('Topic')
        post.body = request.POST.get('body')
        post.background_image = request.POST.get('background_image')
        post.save()
        return redirect('home')
    context = {'form': form, 'topics': topics, 'post':post}
    return render (request, 'edit-post.html',context)

def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, user=request.user)

        if not form.is_valid():
             return render(request, 'create-post.html', {
                'form': form
            })
        
        form.save()
        return redirect('home')
    
    return render(request, 'create-post.html', {
       'form': PostForm()
    })

def createtopic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)

        if not form.is_valid():
             return render(request, 'create-topic.html', {
                'form': form
            })
        
        form.save()
        return redirect('home')
    return render(request, 'create-topic.html', {
       'form': TopicForm()
    })



def createcomment(request,pk):
    if request.method == 'POST':
        form = CommentForm(request.POST,user=request.user)

        if not form.is_valid():
             return render(request, 'create-comment.html', {
                'form': form
            })
        
        form.save()
        return redirect('home')
    
    return render(request, 'create-comment.html', {
       'form': CommentForm() ,
    })




def knowpage(request):
    post = POST.objects.all()
    Topics = Topic.objects.all()
    users = User.objects.all()
    comments = comment.objects.all()
    comment_count = comments.count()
    user_count = users.count()
    post_count = post.count()
    topic_count = Topics.count()
    context = {'POST': post ,'comment_count': comment_count, 'user_count':user_count ,'post_count': post_count,'Topics':Topics,'topic_count':topic_count}
    return render(request, 'know.html',context)


def topicpage(request):
    Topics = Topic.objects.all()
    context = { 'Topics':Topics }
    return render(request, 'topics.html', context)
    


def seemore(request, pk: int):
    return render(request, 'seemore.html', {
        'POST': get_object_or_404(POST, pk=pk)
    })


def profile(request,pk ):
    user = User.objects.get(id=pk)
    context= {'user' : user}
    return render(request,'profile.html',context)

def error(request):
    return render (request, 'error.html')