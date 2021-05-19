from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Tag
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def is_valid_queryparam(param):
    return param != '' and param is not None

def TagsFilterView(request):
    qs = Post.objects.all()
    tags = Tag.objects.all()
    tag = request.GET.get('tag')

    if is_valid_queryparam(tag) and tag != 'Choose...':
        qs = qs.filter(tags__title=tag)

    context = {
        'queryset': qs,
        'tags': tags
    }
    return render(request, "tags_filter.html", context)



#Search Section Program
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)



def get_tag_count():
    queryset = Post.objects.values('tags__title').annotate(Count('tags__title'))

    return queryset


def index(request):
    posts = Post.objects.order_by('-date_posted')
    latest = Post.objects.order_by('-date_posted')[:3]
    tag_count = get_tag_count()
    paginator = Paginator(posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'posts': paginated_queryset,
        'latest': latest,
        'page_request_var': page_request_var,
        'tag_count': tag_count,
    }
    return render(request, 'blog/index.html', context)

class PostListView(ListView):
      model = Post
      template_name = 'blog/index.html'# <app>/<model>_<viewtype>.html
      context_object_name = 'posts'
      ordering = ['-date_posted']

class PostDetailView(DetailView):
    model=Post
    tag_count = get_tag_count()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'tags']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title', 'content', 'image', 'tags']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
          post= self.get_object()
          if self.request.user == post.author:
              return True
          return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post
        success_url = '/'

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False


def aboutus(request):
    return render(request, 'blog/aboutus.html')

def traveltips(request):
    return render(request, 'blog/traveltips.html')

def famdes(request):
    return render(request, 'blog/famdes.html')

def exploreindia(request):
    return render(request, 'blog/exploreindia.html')

def exploregermany(request):
    return render(request, 'blog/exploregermany.html')

def exploreegypt(request):
    return render(request, 'blog/exploreegypt.html')

def explorecolombia(request):
    return render(request, 'blog/explorecolombia.html')

def explorenewyork(request):
    return render(request, 'blog/explorenewyork.html')

def exploreparis(request):
    return render(request, 'blog/exploreparis.html')

def famousdestinations(request):
    return render(request, 'blog/famdes.html')

#Comment section program for just the registered users to make comment

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm
    return render(request,'blog/add__comment.html',{'form': form})


@login_required
def comment_approve(request,pk) :
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk = comment.post.pk)

@login_required
def comment_remove(request,pk) :
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post-detail', pk = post_pk)





