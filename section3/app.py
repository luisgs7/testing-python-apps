blogs = dict()


def menu():
    # Show the user the avaible blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print("- {}".format(blog))
