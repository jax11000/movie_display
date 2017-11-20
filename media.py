import webbrowser


class Movie():
    # defines what a movie object should be
    def __init__(self, title, storyline, image, youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.youtube_url = youtube_url

    def show_trailer(self):

        webbrowser.open(self.youtube_url)
# end of file