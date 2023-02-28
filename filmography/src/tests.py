from django.test import TestCase

from src.models.film import Film
from src.models.genre import Genre, Genres
from src.models.human import Human


class FilmTestCase(TestCase):
    def setUp(self):
        self.genre1 = Genre.objects.create(genre=Genres.ACTION)
        self.genre2 = Genre.objects.create(genre=Genres.DRAMA)

        self.producer1 = Human.objects.create(first_name='John', last_name='Doe')
        self.producer2 = Human.objects.create(first_name='Jane', last_name='Doe')
        self.director = Human.objects.create(first_name='Bob', last_name='Smith')
        self.actor = Human.objects.create(first_name='Alice', last_name='Johnson')
        self.voice_actor = Human.objects.create(first_name='Tom', last_name='Hanks')

        self.film = Film.objects.create(
            name='The Shawshank Redemption',
            description='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            plot='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            rating=9.3,
            age_rating=16,
            duration=142,
            announce_date='1994-09-10',
            release_date='1994-10-14',
        )
        self.film.producers.set([self.producer1, self.producer2])
        self.film.directors.set([self.director])
        self.film.actors.set([self.actor])
        self.film.voice_actors.set([self.voice_actor])
        self.film.story_writers.set([self.director])
        self.film.musicians.set([self.actor])
        self.film.screenwriters.set([self.director])
        self.film.genres.set([self.genre1, self.genre2])

    def test_film_save(self):
        self.film.name = 'the shawshank redemption'
        with self.assertRaisesMessage(AssertionError, 'Film name must be capitalized'):
            self.film.save()

    def test_film_key(self):
        self.assertEqual(self.film.key(), 'the-shawshank-redemption')

    def test_film_description_as_list(self):
        self.assertEqual(self.film.description_as_list(), [
            'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'])

    def test_film_plot_as_list(self):
        self.assertEqual(self.film.plot_as_list(), [
            'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'])

    def test_film_str(self):
        self.assertEqual(str(self.film), 'The Shawshank Redemption')
