class Movie:
    """Class to store all film variables in order:
    1. rank
    2. rating
    3. title
    4. year
    5. rated
    6. runtime
    7. genre
    8. directors
    9. actors
    10. production"""

    def __init__(self, rank, imdb_rating, title, year, rated, runtime, genre, directors, actors, production):
        self.rank = rank
        self.imdb_rating = imdb_rating
        self.title = title
        self.year = year
        self.rated = rated
        self.runtime = runtime
        self.genre = genre
        self.directors = directors
        self.actors = actors
        self.production = production

    def __repr__(self):
        return f'[{self.rank}: ({self.imdb_rating}, {self.title}, {self.year}, {self.rated},' \
               f' {self.runtime}, {self.genre}, {self.directors}, {self.actors}, {self.production})]'
