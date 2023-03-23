
def move (y, x):
    print("\033[%d;%dH" % (y, x))

def clear (y, x, size_y, size_x):
    move(y, x)
    for i in range(size_y): print(' ' * size_x)
    move(y, x)
