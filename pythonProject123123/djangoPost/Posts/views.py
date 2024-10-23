
from django.shortcuts import render,redirect,get_object_or_404
from .models import Posts
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'Posts/postshome.html', context)



@login_required
def about(request):
    return render(request, 'Posts/about.html')

# Create your views here.
@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'Posts/post_form.html', context)
    elif request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'Posts/post_form.html',{'form':form})
@login_required
def edit_post(request, id):
   post = get_object_or_404(Posts, id=id)
   if request.method == 'GET':
       context = {'form': PostForm(instance=post), 'id': id}
       return render(request,'Posts/post_form.html',context)
   elif request.method == 'POST':
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
           form.save()
           messages.success(request, 'The post has been updated successfully.')
           return redirect('home')
       else:
           messages.error(request, 'Please correct the following errors:')
           return render(request,'Posts/post_form.html',{'form':form})
@login_required
def delete_post(request,id):
    post=get_object_or_404(Posts,id=id)
    context={'post':post}
    if request.method == 'GET':
        return render(request, 'Posts/post_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'Пост успешно удален.')
        return redirect('home')