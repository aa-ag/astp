############------------ IMPORTS ------------############
import post
from project.app import list_blogs


############------------ CLASS(ES) ------------############
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

    def ask_read_blog(self):
        title = input('Enter the blog title you want to read: ')
        print_posts(blogs[title])

    def print_posts(self):
        for post in blog.posts:
            print_post(post)
        
    def json_function(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [p.json_function() for p in self.posts],
        }


############------------ DRIVER CODE ------------############
