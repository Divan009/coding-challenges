# Method Resolution Order (MRO)

class A:
    def __init__(self):
        print("Initializing A")
        super().__init__()

class B:
    def __init__(self):
        print("Initializing B")
        super().__init__()

class C(A):
    def __init__(self):
        print("Initializing C")
        # super().__init__()

class D(C, B):
    def __init__(self):
        print("Initializing D")
        super().__init__() # initializes the parent


if __name__ == "__main__":
    d = D()
    print(D.__mro__)