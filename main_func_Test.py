import unittest
from main_func import *


class TestTop250MoviesMain(unittest.TestCase):

    def test_give_title_by_director(self):
        self.assertEqual(give_title_by_director('Christopher Nolan'), ['The Dark Knight', 'Inception', 'Interstellar',
                                                                       'The Prestige', 'Memento',
                                                                       'The Dark Knight Rises', 'Batman Begins'])
        self.assertEqual(give_title_by_director('Quentin Tarantino'), ['Pulp Fiction', 'Django Unchained',
                                                                       'Reservoir Dogs', 'Inglourious Basterds',
                                                                       'Kill Bill: Vol. 1', 'Sin City'])
        self.assertNotEqual(give_title_by_director('Quentin Tarantino'),
                            ['The Dark Knight', 'Inception', 'Interstellar',
                             'The Prestige', 'Memento',
                             'The Dark Knight Rises', 'Batman Begins'])
        self.assertIsInstance(give_title_by_director('Quentin Tarantino'), list)
        self.assertNotIsInstance(give_title_by_director('Quentin Tarantino'), dict)

    def test_give_title_by_actor(self):
        self.assertEqual(give_title_by_actor('Carrie Fisher'), ['Star Wars: Episode V - The Empire Strikes Back',
                                                                'Star Wars: Episode IV - A New Hope',
                                                                'Star Wars: Episode VI - Return of the Jedi',
                                                                'Star Wars: The Force Awakens'])
        self.assertEqual(give_title_by_actor('Morgan Freeman'), ['The Shawshank Redemption', 'Se7en',
                                                                 'Unforgiven', 'Million Dollar Baby'])
        self.assertNotEqual(give_title_by_actor('Leonardo DiCaprio'),
                            ['Forrest Gump', 'Saving Private Ryan', 'The Green Mile', 'Toy Story 3',
                             'Toy Story', 'Catch Me If You Can'])
        self.assertIsInstance(give_title_by_actor('Tom Hanks'), list)
        self.assertNotIsInstance(give_title_by_actor('Tom Hanks'), dict)

    def test_number_of_movies_per_director(self):
        superset_dict = number_of_movies_per_director()
        subdict_dict1 = {'Christopher Nolan': 7}
        self.assertDictEqual(subdict_dict1, {k: superset_dict[k] for k in subdict_dict1})
        subdict_dict2 = {'Peter Jackson': 3}
        self.assertDictEqual(subdict_dict2, {k: superset_dict[k] for k in subdict_dict2})
        self.assertIsInstance(superset_dict, dict)
        self.assertNotIsInstance(superset_dict, list)

    def test_give_10_directors_with_most_films(self):
        self.assertEqual(give_10_directors_with_most_films(), ['Alfred Hitchcock', 'Stanley Kubrick',
                                                               'Christopher Nolan', 'Steven Spielberg',
                                                               'Martin Scorsese', 'Billy Wilder',
                                                               'Quentin Tarantino', 'Charles Chaplin',
                                                               'Frank Capra', 'Ridley Scott'])
        self.assertIsInstance(give_10_directors_with_most_films(), list)
        self.assertNotIsInstance(give_10_directors_with_most_films(), dict)

    def test_give_titles_from_directors_with_most_films(self):
        for title in ["Alien", "The Wolf of Wall Street", 'Psycho']:
            self.assertIn(title, give_titles_from_directors_with_most_films())
        self.assertIsInstance(give_titles_from_directors_with_most_films(), list)
        self.assertNotIsInstance(give_titles_from_directors_with_most_films(), dict)

    def test_number_of_movies_per_actor(self):
        superset_dict = number_of_movies_per_actor()
        subdict_dict1 = {'Morgan Freeman': 4}
        self.assertDictEqual(subdict_dict1, {k: superset_dict[k] for k in subdict_dict1})
        subdict_dict2 = {'Natalie Portman': 2}
        self.assertDictEqual(subdict_dict2, {k: superset_dict[k] for k in subdict_dict2})
        self.assertIsInstance(superset_dict, dict)
        self.assertNotIsInstance(superset_dict, list)

    def test_give_9_actors_with_most_films(self):
        self.assertEqual(give_9_actors_with_most_films(), ['Leonardo DiCaprio', 'Robert De Niro',
                                                               'Harrison Ford', 'James Stewart',
                                                               'Tom Hanks', 'Tom Hardy',
                                                               'William Holden', 'Cary Grant', 'Paul Newman'])
        self.assertIsInstance(give_9_actors_with_most_films(), list)
        self.assertNotIsInstance(give_9_actors_with_most_films(), dict)

    # Returns the movies (only titles) of each of the 9 actors
    def test_give_titles_for_9_actors_with_most_films(self):
        for title in ['Catch Me If You Can', 'Blood Diamond', 'Inception', 'Django Unchained']:
            self.assertIn(title, give_titles_for_9_actors_with_most_films())
        self.assertIsInstance(give_titles_for_9_actors_with_most_films(), list)
        self.assertNotIsInstance(give_titles_for_9_actors_with_most_films(), dict)

    # Returns the movies (only titles) of each of the 5 most frequent actor partnerships
    def test_titles_for_most_5_actor_partnership(self):
        titles_samples = {'Star Wars: The Force Awakens', 'Star Wars: Episode VI - Return of the Jedi',
                          'Star Wars: Episode IV - A New Hope', 'Star Wars: Episode V - The Empire Strikes Back'}
        self.assertTrue(titles_samples.issubset(titles_for_most_5_actor_partnership()))
        self.assertIsInstance(titles_for_most_5_actor_partnership(), set)
        self.assertNotIsInstance(titles_for_most_5_actor_partnership(), dict)
        self.assertNotIsInstance(titles_for_most_5_actor_partnership(), list)
