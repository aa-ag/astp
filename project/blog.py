class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = list()

    def json_function(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': list(),
        }
