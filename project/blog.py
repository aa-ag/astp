import post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = list()

    def __repr__(self):
        posts_n = len(self.posts)
        return f"{self.title} by {self.author} ({posts_n} posts)."

    def create_post(self, title, content):
        self.posts.append(post.Post(title, content))
        
    def json_function(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': list(),
        }
