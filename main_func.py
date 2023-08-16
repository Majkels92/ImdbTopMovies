import utility
import itertools


# Returns list of the movies (only titles) directed (or co-directed) by a given director
def give_title_by_director(director):
    result = []
    list_of_movies = utility.create_list_with_movies_as_objects()
    for i in list_of_movies:
        if director in i.directors:
            result.append(i.title)
    return result


# Returns list of the movies (only titles) in which an actor played
def give_title_by_actor(actor):
    result = []
    list_of_movies = utility.create_list_with_movies_as_objects()
    for i in list_of_movies:
        if actor in i.actors:
            result.append(i.title)
    return result


# Returns dictionary with the number of movies per director
def number_of_movies_per_director():
    d_dict = dict()
    list_of_movies = utility.create_list_with_movies_as_objects()
    for i in list_of_movies:
        if "," in i.directors:
            trimmed_txt = i.directors.split(",")
            for d in trimmed_txt:
                d = d.lstrip()
                if d in d_dict:
                    d_dict[d] += 1
                else:
                    d_dict[d] = 1
        else:
            if i.directors in d_dict:
                d_dict[i.directors] += 1
            else:
                d_dict[i.directors] = 1
    return d_dict


# Returns list of the 10 directors with the most films on the list
def give_10_directors_with_most_films():
    d_dict = number_of_movies_per_director()
    sorted_dict_as_tuples_list = sorted(d_dict.items(), key=lambda x: x[1], reverse=True)
    top_10_result = sorted_dict_as_tuples_list[0:10]
    result = [i[0] for i in top_10_result]
    return result


# Returns list of the movies (only titles) made by each of the 10 directors found in previous
def give_titles_from_directors_with_most_films():
    top_10_direct = give_10_directors_with_most_films()
    top_10_director_movies = [give_title_by_director(i) for i in top_10_direct]
    return list(itertools.chain.from_iterable(top_10_director_movies))


# Returns dictionary with the number of movies per actor
def number_of_movies_per_actor():
    a_dict = dict()
    list_of_movies = utility.create_list_with_movies_as_objects()
    for i in list_of_movies:
        if "," in i.actors:
            trimmed_txt = i.actors.split(",")
            for a in trimmed_txt:
                a = a.lstrip()
                if a in a_dict:
                    a_dict[a] += 1
                else:
                    a_dict[a] = 1
        else:
            if i.actors in a_dict:
                a_dict[i.actors] += 1
            else:
                a_dict[i.actors] = 1
    return a_dict


# Returns list of the 9 actors with the most films on the list
def give_9_actors_with_most_films():
    a_dict = number_of_movies_per_actor()
    sorted_dict_as_tuples_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    top_9_result = sorted_dict_as_tuples_list[0:9]
    result = [i[0] for i in top_9_result]
    return result


# Returns list of the movies (only titles) of each of the 9 actors
def give_titles_for_9_actors_with_most_films():
    top_9_actors = give_9_actors_with_most_films()
    top_9_actors_movies = [give_title_by_actor(i) for i in top_9_actors]
    return list(itertools.chain.from_iterable(top_9_actors_movies))


# Returns set the movies (only titles) of each of the 5 most frequent actor partnerships
def titles_for_most_5_actor_partnership():
    result = set()
    actors_partnerships = utility.get_5_most_partnerships_of_actors()
    for duo in actors_partnerships:
        actors = utility.split_duo(duo)
        result.update(set(give_title_by_actor(actors[0])).intersection(set(give_title_by_actor(actors[1]))))
    return result


if __name__ == '__main__':
    # print(give_title_by_director('Guy Ritchie'))
    # print(give_title_by_actor('Tom Hanks'))
    # print(number_of_movies_per_director())
    # print(give_10_directors_with_most_films())
    # print(give_titles_from_directors_with_most_films())
    # print(number_of_movies_per_actor())
    # print(give_9_actors_with_most_films())
    # print(give_titles_for_9_actors_with_most_films())
    print(titles_for_most_5_actor_partnership())
