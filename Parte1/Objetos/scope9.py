count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    global count
    count = c


def id_count():
    global count
    return id(count)
