import index
import media

eraserhead = media.Movie("Eraserhead",
                         "A man living in an indusrial cityscape experiences vivid dreams and hallucinations",
                         "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Eraserhead.jpg/220px-Eraserhead.jpg",
                         "https://youtu.be/dU7OqGCIcak")

#print(eraserhead.storyline)
#eraserhead.show_trailer()

rockyhorror = media.Movie("Rocky Horror Picture Show",
                          "A stranded young couple is taken in by a mad scientst for the night",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Original_Rocky_Horror_Picture_Show_poster.jpg/220px-Original_Rocky_Horror_Picture_Show_poster.jpg",
                          "https://www.youtube.com/watch?v=_Ov8yLJkknY")

soundofmusic = media.Movie("Pan's Labyrinth",
                           "Dark fantasy film set in Spain after the Spanish Civil War",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Pan%27s_Labyrinth.jpg/220px-Pan%27s_Labyrinth.jpg",
                           "https://www.youtube.com/watch?v=EqYiSlkvRuw")

amelie = media.Movie("Amelie",
                     "A young waitress decides to do good deeds to change the lives of those around her for the better",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o")

vsevil = media.Movie("Tucker & Dale vs Evil",
                     "Two well-meaning hillbillies are mistaken for killers by clueless college students",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/Tucker-and-dale-vs-evil.jpg/220px-Tucker-and-dale-vs-evil.jpg",
                     "https://www.youtube.com/watch?v=l1t8OZn_uhE")

love = media.Movie("The One I Love",
                  "In an effort to save their marriage, a couple spends the weekend at a retreat where things get wierd",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/TOIL_poster.jpg/220px-TOIL_poster.jpg",
                  "https://www.youtube.com/watch?v=jCOvhojlZzQ")

movies = [eraserhead, rockyhorror, soundofmusic, amelie, vsevil, love]
index.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
                  

