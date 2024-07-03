from django.shortcuts import render, redirect
from .models import Users, Favouritemovies
from review_app.models import Reviews
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def display_users_page(request):
    users = Users.get_users_head()
    reviews = Reviews.get_reviews_head()
    return render(request, 'users.html',
                  {'users': users, 'reviews': reviews})

@login_required(login_url='user_app:login')
def display_user_details_page(request, user_id):
    user = Users.get_user(user_id)
    user_favorite_movies = user.get_user_favorite_movies()
    user_reviews = user.get_user_reviews()
    context = {'user': user, 'user_favorite_movies': user_favorite_movies,
               'user_reviews': user_reviews}
    return render(request, 'user_details.html', context=context)


@login_required(login_url='user_app:login')
def display_sample_user_details_page(request):
    user = Users.get_user(1)
    user_favorite_movies = user.get_user_favorite_movies()
    user_reviews = user.get_user_reviews()
    context = {'user': user, 'user_favorite_movies': user_favorite_movies,
               'user_reviews': user_reviews}
    return render(request, 'user_details.html', context=context)


def display_login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("username: ", username, "password: ", password, "user: ", user)
        if user is not None:
            login(request, user)
            return redirect('user_app:user_details', user_id=user.user_id)
        else:
            context['error'] = "Invalid username or password"
    else:
        form = AuthenticationForm()
        context['form'] = form
    return render(request, 'login.html', context=context)




def display_logout_page(request):
    logout(request)
    if request.method == 'POST':
        return redirect('user_app:login')
    else:
        return render(request, 'logout.html')


def display_register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('user_app:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context=context)
