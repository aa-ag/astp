class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = list()

    def __repr__(self):
        return "Test by Test Author (0 posts)."
        
    def json_function(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': list(),
        }
