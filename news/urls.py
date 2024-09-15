from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from news.views import CommentCreateView, ImageUploadView, PostCreateView, PostList, PostDetail, ToggleFavoriteView, register

urlpatterns = [
    path('register/', register),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
    path('create-post/', PostCreateView.as_view(), name='create-post'),
    path('create-comment/', CommentCreateView.as_view(), name='create-comment'),
    path('toggle-favorite/<int:post_id>/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
]