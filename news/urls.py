from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('search/', PostSearch.as_view(), name= 'news_search'),
    path('create/', PostCreate.as_view(), name= 'news_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name= 'news_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]