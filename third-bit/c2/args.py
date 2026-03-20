def show_args(title, *args, **kwargs):
    print(f"{title} args '{args}' and kwargs '{kwargs}'")


# show_args("nothing")
# show_args("one unnamed argument", 1)
# show_args("one named argument", second="2")
# show_args("one of each", 3, fourth="4")
# show_args("one of each", 3, 4, 5, fourth="4", fifth="8")


def show_spread(left, middle, right):
    print(f"left {left} middle {middle} right {right}")


all_in_list = [1, 2, 3]
show_spread(*all_in_list)

all_in_dict = {"right": 30, "left": 10, "middle": 20}
show_spread(**all_in_dict)
