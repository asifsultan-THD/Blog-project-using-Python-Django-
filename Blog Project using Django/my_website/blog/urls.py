from django.urls import path
from .views import (
    search,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
   )
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('traveltips/', views.traveltips, name='traveltips'),
    path('famdes/', views.famdes, name='famdes'),
    path('search/', search, name='search'),
    path('tagsfilter/', views.TagsFilterView, name='tagsfilter'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('post/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('exploreindia/', views.exploreindia, name='exploreindia'),
    path('exploregermany/', views.exploregermany, name='exploregermany'),
    path('exploreegypt/', views.exploreegypt, name='exploreegypt'),
    path('explorecolombia/', views.explorecolombia, name='explorecolombia'),
    path('explorenewyork/', views.explorenewyork, name='explorenewyork'),
    path('exploreparis/', views.exploreparis, name='exploreparis'),
]





