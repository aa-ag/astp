############------------ IMPORTS ------------############
import blog

############------------ GLOBAL VARIABLE(S) ------------############
blogs = dict()
MENU_PROMPT = '''Press "b" to create a blog 
"l" to list all blogs
"p" to create a post
"q" to quit the program
go ahead:  '''

############------------ FUNCTION(S) ------------############
def menu():
    list_blogs()

    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'b':
            ask_create_blog()
        elif selection == 'l':
            list_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def ask_create_blog():
    '''
     creates a blog with input from user
     for title & author
    '''
    title = input('Enter Blog\'s name: ')
    author = input('Enter Blog\'s author name:\n')
    blogs[title] = blog.Blog(title, author)


def list_blogs():
    '''
     print all available blogs
    '''
    for blog_name, blog_object in blogs.items():
        print(str(blog_object))


def ask_read_blog():
        title = input('Enter the blog title you want to read: ')
        print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(f"{post.title}... {post.content}")


def ask_create_post():
    blog_name  = input('Blog title where you want to write a post:\n')
    title = input('Your post\'s title:\n')
    content = input('Your post\'s content:\n')

    blogs[blog_name].create_post(title, content)

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    menu()