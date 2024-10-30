from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
def sign_in(request):
    if request.method == 'GET':
        form=LoginForm()
        return render(request,'users/login.html',{'form':form})
    elif request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f'Привет{username.title()},Добро пожаловать!')
                return redirect('home')
        messages.error(request,'invalid username/password')
        return render (request,'users/login.html',{'form':form})
def sign_out(request):
    logout(request)
    messages.success(request, f'Вы вышли из аккаунта')
    return redirect('login')
# Create your views here.
def RegisterView(FormView):
    template_name='register.html'
    form_class=RegisterForm
    redirect_authenticated_user = True
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        user=form.save()
        if user:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)
