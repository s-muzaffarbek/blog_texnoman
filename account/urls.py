from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
urlpatterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', LoginBlogView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>', MyUserView.as_view(), name='user_profile'),
    path('edit/<int:pk>', UserEditView.as_view(), name='user_edit'),
]