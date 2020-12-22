#--- CONSTANTS ---#
MENU_PROMPT = '"c" to create a blog "l" to list blogs, "r" ro read one, "q" to quit'

# mapping of blog_name to Blog object
blogs = dict()


#--- FUNCTIONS ---#
def menu():
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for k, v in blogs.items():
        print('- {}'.format(v))
