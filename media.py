"""
Module to display movie object, attributes and instances
"""
import webbrowser


class Movie():
    # defines what a movie object should be
    """ 
    Class object stores movie info
    """
    def __init__(self, title, storyline, image, youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.youtube_url = youtube_url
        """
        :param title: string
        :param storyline: string
        :param image: string
        :param youtube_url: string
        """

    def show_trailer(self):

        """
        Initializing instance for opening youtube video

        :return: webbrowser to play trailer
        """

        webbrowser.open(self.youtube_url)
# end of file