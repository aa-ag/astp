############------------ IMPORTS ------------############


############------------ GLOBAL VARIABLE(S) ------------############
blogs = dict()


############------------ FUNCTION(S) ------------############
def menu():
    print_blogs()


def print_blogs():
    '''
     print all available blogs
    '''
    for blog_name, blog_object in blogs.items():
        print(blog_object)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    menu()