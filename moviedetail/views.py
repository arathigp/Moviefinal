from moviedetail.forms import MdetailForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm

def add_movie(request):
    if request.method == 'POST':
        form = MdetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('movieapp:uhome')
            # Redirect to the movie list page
    else:
        form = MdetailForm()
    return render(request, 'addmovie.html', {'form': form})


def movie_detail(request):
   movie =Movie.objects.filter(user=request.user)
   return render(request, "mdetail.html", {'movie': movie})


def movie_list(request):
    category = request.GET.get('category', '')
    search_query = request.GET.get('search_query', '')

    if category:
        movies = Movie.objects.filter(category=category)
    elif search_query:
        movies = Movie.objects.filter(movie_title__icontains=search_query)
    else:
        movies = Movie.objects.all()

    movie_reviews = {}
    for movie in movies:
        reviews = Review.objects.filter(movie=movie)
        movie_reviews[movie.id] = reviews

    return render(request, 'movie_list.html', {'movies': movies, 'category': category, 'search_query': search_query,
                                                   'movie_reviews': movie_reviews})


def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('moviedetail:movie_list')
    else:
        form = ReviewForm()

    return render(request, 'addreview.html', {'form': form, 'movie': movie})


def movie_update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    # Check if the current user is the one who added the movie
    if request.user != movie.user:
        # You can handle unauthorized access here (redirect, show an error message, etc.)
        return redirect('uhome')

    if request.method == 'POST':
        form = MdetailForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('moviedetail:movie_detail')
    else:
        form = MdetailForm(instance=movie)

    return render(request, 'mupdate.html', {'form': form, 'movie': movie})



def movie_delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    # Check if the current user is the one who added the movie
    if request.user != movie.user:
        # You can handle unauthorized access here (redirect, show an error message, etc.)
        return redirect('uhome')

    if request.method == 'POST':
        movie.delete()
        return redirect('moviedetail:movie_detail')

    return render(request, 'mdelete.html', {'movie': movie})





