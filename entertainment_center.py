import media
import fresh_tomatoes

# initializing movie variables
avengers = media.Movie(
    "Avengers",
    "A team of superheros unite to fight evil",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # Noqa
    "https://www.youtube.com/watch?v=eOrNdBpGMv8"
                       )

hunger_games = media.Movie(
    "Hunger Games", 
    "Totalitarian society forces people to fight to the death",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",  # Noqa
    "https://www.youtube.com/watch?v=4S9a5V9ODuY")

inglorious_bastards = media.Movie(
    "Inglorious Bastards", 
    "Team of U.S. soldiers on the hunt for Nazis",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",  # Noqa
    "https://www.youtube.com/watch?v=lb-9_4lGVmc")

deadpool = media.Movie(
    "Deadpool", 
    "Misfit hero fights evil",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",  # Noqa
    "https://www.youtube.com/watch?v=ONHBaC-pfsk")

walking_tall = media.Movie(
    "Walking Tall", 
    "Vet returns from war to be town sheriff",
    "https://upload.wikimedia.org/wikipedia/en/e/e9/Walking_Tall_%282004_film%29.jpg",  # Noqa
    "https://www.youtube.com/watch?v=edR_niqKp1Q")

iron_man = media.Movie(
    "Iron Man", 
    "Billionaire makes super soldier suite",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",  # Noqa
    "https://www.youtube.com/watch?v=8hYlB38asDY")



movies = [
    avengers, 
    hunger_games, 
    inglorious_bastards, 
    deadpool, 
    walking_tall, 
    iron_man
    ]
# use fresh_tomatoes.py to set up web page
fresh_tomatoes.open_movies_page(movies)
                          
# end of file