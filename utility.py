import csv
import Movie


def isolate_movie_variables_and_put_to_object(row):
    """Creates from given row an object of Movie Class"""
    movie = Movie.Movie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
    return movie


def create_list_with_movies_as_objects():
    """Creates list of top250 movies from csv file and adds every movie as an object of Movie Class"""
    list_of_movies = []
    with open('imdb_top250.csv', newline='') as csvfile:
        file = csv.reader(csvfile)
        count = 0
        for row in file:
            if count == 0:
                count += 1
                pass
            else:
                movie = isolate_movie_variables_and_put_to_object(row)
                list_of_movies.append(movie)
    return list_of_movies


def get_list_of_actors_per_movie():
    """Creates list with nested lists. Every nested list represents actors from one of 250 movies"""
    list_of_movies = create_list_with_movies_as_objects()
    result = [i.actors.split(",") for i in list_of_movies]
    return result


def create_pairs_from_list(given_list):
    """Creates list of unique pairs given from given list.
    Every pair is bonded as one string connected with '&' character"""
    paired_list = [[a.lstrip(), b.lstrip()] for index, a in enumerate(given_list) for b in given_list[index+1:]]
    for i in range(len(paired_list)):
        paired_list[i].sort()
        paired_list[i] = paired_list[i][0] + " & " + paired_list[i][1]
    return paired_list


def create_list_of_actors_partnerships(given_list_of_actors):
    """Creates list with actors partnerships"""
    list_of_pairs = []
    for movie_actors in given_list_of_actors:
        list_of_pairs.extend(create_pairs_from_list(movie_actors))
    return list_of_pairs


def get_5_most_partnerships_of_actors():
    """Creates dictionary with top 5 actor partnerships"""
    partners_dict = {}
    only_actors_from_movies = get_list_of_actors_per_movie()
    partnerships = create_list_of_actors_partnerships(only_actors_from_movies)
    for i in partnerships:
        if i not in partners_dict:
            partners_dict[i] = 1
        else:
            partners_dict[i] += 1
    sorted_dict_as_tuples_list = sorted(partners_dict.items(), key=lambda x: x[1], reverse=True)
    top_5_result = sorted_dict_as_tuples_list[0:5]
    top_5_actor_pairs = [i[0] for i in top_5_result]
    return top_5_actor_pairs

def split_duo(actors_duo):
    actors_list = actors_duo.split(" & ")
    return actors_list