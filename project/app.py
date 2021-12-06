############------------ IMPORTS ------------############
import blog

############------------ GLOBAL VARIABLE(S) ------------############
blogs = dict()
MENU_PROMPT = '''Press "c" to create a blog 
"l" to list all blogs
"p" to create a post
"q" to quit the program
go ahead:  '''

############------------ FUNCTION(S) ------------############
def menu():
    list_blogs()

    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            list_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def ask_create_blog():
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
    pass


def ask_create_post():
    pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    menu()