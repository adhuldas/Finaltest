from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, DeleteView, ListView

from projectapp.models import product


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
            user.save()
            print('user created')

        else:
            print("password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')


class ProductUpdateView(UpdateView):
    model = product
    template_name = 'update.html'
    fields = ['name', 'img', 'desc','Category']

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class ProductDetailView(DetailView):
    model = product
    template_name = 'detail.html'
    context_object_name = 'i'


class ProductDeleteView(DeleteView):
    model = product
    template_name = 'delete.html'
    success_url = "/"


class ProductListView(ListView):
    model = product
    template_name = 'base.html'
