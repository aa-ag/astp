############------------ IMPORTS ------------############


############------------ GLOBAL VARIABLE(S) ------------############
blogs = dict()
MENU_PROMPT = '''Press "c" to create a blog 
"l" to list all blogs
"p" to create a post
"q" to quit the program
go ahead:  '''

############------------ FUNCTION(S) ------------############
def menu():
    print_blogs()

    selection = input(MENU_PROMPT)

def print_blogs():
    '''
     print all available blogs
    '''
    for blog_name, blog_object in blogs.items():
        print(blog_object)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    menu()