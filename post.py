class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def jsonify(self):
        return {
            'title': self.title,
            'content': self.content
        }
