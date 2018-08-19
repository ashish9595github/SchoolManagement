from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
from Login.forms import UserForm
from SchoolManagement.decorators import  admin_only

class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        django_login(request,user)
        token.created=Token.objects.get_or_created(user=user)
        return Response({"token":token.key},status=200)

class LogoutView(APIView):
    authentication_classes=(TokenAuthentication)
    def post(self,request):
        django_logout(request)
        return Response(status=204)

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
            #return Response(status=400)
    else:
        return render(request, "auth/login.html", context)
        # return Response(status=204)
@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)
    #return Response(status=204)
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
def parent_list(request):
    print(request.role)
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Parents'
    return render(request, 'parent/index.html', context)

@login_required(login_url="/login/")
def parent_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'parent/details.html', context)

@login_required(login_url="/login/")
@admin_only
def parent_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('parent_list'))
        else:
            return render(request, 'parent/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'parent/add.html', context)

@login_required(login_url="/login/")
def parent_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('parent_list'))
        else:
            return render(request, 'parent/edit.html', {"user_form": user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'parent/edit.html', {"user_form": user_form})


@login_required(login_url="/login/")
def parent_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('parent_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'parent/delete.html', context)



@login_required(login_url="/login/")
def teacher_list(request):
    print(request.role)
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'teacher'
    return render(request, 'teacher/index.html', context)

@login_required(login_url="/login/")
def teacher_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'teacher/details.html', context)


@login_required(login_url="/login/")
@admin_only
def teacher_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('teacher_list'))
        else:
            return render(request, 'teacher/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'teacher/add.html', context)

@login_required(login_url="/login/")
def teacher_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('parent_list'))
        else:
            return render(request, 'teacher/edit.html', {"user_form": user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'teacher/edit.html', {"user_form": user_form})
        #return Response(status=201)



@login_required(login_url="/login/")
def teacher_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('teacher_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'teacher/delete.html', context)

