############------------ IMPORTS ------------############


############------------ GLOBAL VARIABLE(S) ------------############
blogs = dict()


############------------ FUNCTION(S) ------------############
def menu():
    print_blogs()

    selection = input(
        'Press "c" to create a blog\n' +
        '"l" to list all blogs\n' +
        '"p" to create a post\n' +
        '"q" to quit the program\n\n--> go ahead:  '
    )

    print(selection)

def print_blogs():
    '''
     print all available blogs
    '''
    for blog_name, blog_object in blogs.items():
        print(blog_object)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    menu()