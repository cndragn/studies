import webbrowser

class Movie():
    """ This class provides a way to store movie relted information """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline,
                 movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_url = movie_poster
        self.trailer_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
