from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from account.forms import RegisterForm, UserEditForm
from account.models import MyUser


class LoginBlogView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('')

class SignUpView(SuccessMessageMixin ,CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"

class MyUserView(View):
    def get(self, request, pk):
        myuser = MyUser.objects.get(pk=pk)
        context = {
            'myuser': myuser,
        }
        return render(request, 'registration/my_user.html', context)

class UserEditView(UpdateView):
    model = MyUser
    form_class = UserEditForm
    template_name = 'registration/update_user.html'


    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('user_profile', kwargs={'pk': pk})