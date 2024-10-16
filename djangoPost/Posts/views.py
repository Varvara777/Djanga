
from django.shortcuts import render
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