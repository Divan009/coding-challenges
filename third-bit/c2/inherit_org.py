def square_perimeter(thing):
    return 4 * thing["side"]


def square_area(thing):
    return thing["side"] ** 2


Square = {"perimeter": square_perimeter, "area": square_area, "_classname": "Square"}
Circle = {"perimeter": square_perimeter, "area": square_area, "_classname": "Circle"}


def square_new(name, side):
    return {"name": name, "side": side, "_class": Square}


def circle_new(name, side):
    return {"name": name, "side": side, "_class": Circle}


def call(thing, method_name):
    return thing["_class"][method_name](thing)


examples = [square_new("sq", 3), circle_new("ci", 2)]
for ex in examples:
    n = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex, "area")
    c = ex["_class"]["_classname"]
    print(f"{n} is a {c}: {p:.2f} {a:.2f}")
