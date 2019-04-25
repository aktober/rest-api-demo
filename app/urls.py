from django.urls import path
from django.contrib.auth import views as auth_views
from app.api_views import CreateUserAPIView, ListsPostsAPI, RUDPostAPI, LikePostAPI, UnlikePostAPI
from app.views import SignUpPage, HomePage

urlpatterns = [
    path('api/users/create/', CreateUserAPIView.as_view(), name='user-create'),
    path('api/posts/', ListsPostsAPI.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', RUDPostAPI.as_view(), name='post-rud'),

    path('api/posts/<int:pk>/like/', LikePostAPI.as_view(), name='post-like'),
    path('api/posts/<int:pk>/unlike/', UnlikePostAPI.as_view(), name='post-unlike'),

    path('signup/', SignUpPage.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', HomePage.as_view(), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
