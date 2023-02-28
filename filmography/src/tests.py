from django.test import TestCase

from src.models.film import Film
from src.models.genre import Genre
from src.models.human import Human


class FilmTestCase(TestCase):
    def setUp(self):
        self.producer = Human.objects.create(name='John Producer')
        self.director = Human.objects.create(name='Jane Director')
        self.actor = Human.objects.create(name='Alice Actor')
        self.voice_actor = Human.objects.create(name='Bob Voice Actor')
        self.story_writer = Human.objects.create(name='Charlie Story Writer')
        self.musician = Human.objects.create(name='David Musician')
        self.screenwriter = Human.objects.create(name='Eve Screenwriter')
        self.genre = Genre.objects.create(name='Action')
        self.film = Film.objects.create(name='Test Film', rating=5.0)

    def test_film_name_capitalized(self):
        self.film.name = 'test film'
        with self.assertRaises(AssertionError):
            self.film.save()

    def test_film_producers(self):
        self.film.producers.add(self.producer)
        self.assertIn(self.producer, self.film.producers.all())

    def test_film_directors(self):
        self.film.directors.add(self.director)
        self.assertIn(self.director, self.film.directors.all())

    def test_film_actors(self):
        self.film.actors.add(self.actor)
        self.assertIn(self.actor, self.film.actors.all())

    def test_film_voice_actors(self):
        self.film.voice_actors.add(self.voice_actor)
        self.assertIn(self.voice_actor, self.film.voice_actors.all())

    def test_film_story_writers(self):
        self.film.story_writers.add(self.story_writer)
        self.assertIn(self.story_writer, self.film.story_writers.all())

    def test_film_musicians(self):
        self.film.musicians.add(self.musician)
        self.assertIn(self.musician, self.film.musicians.all())

    def test_film_screenwriters(self):
        self.film.screenwriters.add(self.screenwriter)
        self.assertIn(self.screenwriter, self.film.screenwriters.all())

    def test_film_genres(self):
        self.film.genres.add(self.genre)
        self.assertIn(self.genre, self.film.genres.all())

    def test_film_key(self):
        self.assertEqual(self.film.key(), 'test-film')

    def test_film_description_as_list(self):
        self.film.description = 'Line 1\nLine 2\n\nLine 3\n'
        self.assertEqual(self.film.description_as_list(), ['Line 1', 'Line 2', 'Line 3'])

    def test_film_plot_as_list(self):
        self.film.plot = 'Line 1\nLine 2\n\nLine 3\n'
        self.assertEqual(self.film.plot_as_list(), ['Line 1', 'Line 2', 'Line 3'])

    def test_film_starring_list(self):
        self.film.voice_actors.add(self.voice_actor)
        self.film.actors.add(self.actor)
        self.assertIn(self.voice_actor, self.film.starring_list())
        self.assertIn(self.actor, self.film.starring_list())
