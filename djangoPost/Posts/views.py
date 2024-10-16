
from django.shortcuts import render,redirect
from .models import Posts
from .forms import PostForm




def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'Posts/postshome.html', context)




def about(request):
    return render(request, 'Posts/about.html')

# Create your views here.
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
            return render(request,'post/post_form.html',{'form':form})
