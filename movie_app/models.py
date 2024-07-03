from django.db import models
from django.apps import apps

class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.TextField()
    production_year = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    certificate = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'

    def __str__(self):
        return self.title

    @classmethod
    def get_distinct_movies(cls):
        all_movies = list(cls.objects.all())
        unique_movies = []
        seen_titles = set()
        for movie in all_movies:
            if movie.title not in seen_titles:
                unique_movies.append(movie)
                seen_titles.add(movie.title)
        return unique_movies

    @classmethod
    def get_popular_movies(cls):
        distinct_movies = cls.get_distinct_movies()
        scored_movies = [(movie, movie.rating * movie.votes) for movie in distinct_movies if
                         movie.rating is not None and movie.votes is not None]
        scored_movies.sort(key=lambda x: x[1], reverse=True)
        return [movie for movie, score in scored_movies[:3]]

    def get_star_rating(self):
        if self.rating is None:
            return {
                'full_stars': [],
                'half_stars': 0,
                'empty_stars': range(5)
            }
        full_stars = int(self.rating)
        decimal_part = self.rating - full_stars

        # Calculate half star
        if 0.25 <= decimal_part < 0.75:
            half_stars = 1
        else:
            half_stars = 0

        # Calculate empty stars
        empty_stars = 5 - full_stars - half_stars

        return {
            'full_stars': range(full_stars),
            'half_stars': half_stars,
            'empty_stars': range(empty_stars)
        }

    @classmethod
    def get_movie(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def get_movies(cls):
        return cls.objects.all()

    @classmethod
    def get_movie_details(cls, id):
        movie = cls.get_movie(id)
        genres = Genredetails.objects.filter(genre__movie=movie)
        directors = Directorsdetails.objects.filter(directors__movie=movie)
        casts = Moviecastdetails.objects.filter(moviecast__movie=movie)
        movie_details = {
            'movie': movie,
            'genres': genres,
            'directors': directors,
            'casts': casts
        }
        return movie_details

    @classmethod
    def get_movies_details(cls):
        movies = cls.objects.all()

        movies_details = []
        for movie in movies:
            genres = Genredetails.objects.filter(genre__movie=movie)
            directors = Directorsdetails.objects.filter(directors__movie=movie)
            casts = Moviecastdetails.objects.filter(moviecast__movie=movie)
            Reviews = apps.get_model('review_app', 'Reviews')
            reviews = Reviews.get_review_for_movie(movie)
            movie_details = {
                'movie': movie,
                'genres': genres,
                'directors': directors,
                'casts': casts,
                'reviews': reviews,
            }

            movies_details.append(movie_details)
        return movies_details

    @classmethod
    def get_movies_head(cls):
        return cls.get_movies_details()[:100]

    @classmethod
    def query_movies(cls, title=None, genre=None):
        queryset = cls.objects.all()
        if title:
            queryset = queryset.filter(title__icontains=title)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        return queryset

    @classmethod
    def sort_movies(cls, title=None, genre=None, sort_by='rating'):
        movies = cls.query_movies(title=title, genre=genre)
        return movies.order_by(sort_by)


class Directors(models.Model):
    director = models.ForeignKey('Directorsdetails', models.DO_NOTHING)
    movie = models.ForeignKey('Movies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'directors'


class Directorsdetails(models.Model):
    director_id = models.AutoField(primary_key=True)
    display_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'directorsdetails'


class Genre(models.Model):
    genre = models.ForeignKey('Genredetails', models.DO_NOTHING)
    movie = models.ForeignKey('Movies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.genre.display_name


class Genredetails(models.Model):
    genre_id = models.AutoField(primary_key=True)
    display_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'genredetails'

    def __str__(self):
        return self.display_name


class Moviecast(models.Model):
    celebrity = models.ForeignKey('Moviecastdetails', models.DO_NOTHING)
    movie = models.ForeignKey('Movies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'moviecast'


class Moviecastdetails(models.Model):
    celebrity_id = models.AutoField(primary_key=True)
    display_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'moviecastdetails'
