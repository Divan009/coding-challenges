from abc import ABC, abstractmethod

from behavior import FlyWithWings, Quack, FlyNoWay, Squeak, MuteQuack
from interface import FlyBehavior, QuackBehavior


class Duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None
        self.initialized = True  # Added attribute to indicate proper initialization

    def perform_fly(self):
        if not hasattr(self, 'initialized'):
            print("Duck not properly initialized")
            return
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    def swim(self):
        print("All ducks float, even decoys!")

    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        # the following line actually initliazes the parent class
        # super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a Mallard Duck!")
        print()
        print()
        print("=======================")


class RedheadDuck(Duck):
    def __init__(self):
        # always call super().__init__() in the constructor of the subclass:
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a Redhead Duck!")
        print()
        print()
        print("=======================")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a Rubber Duck!")
        print()
        print()
        print("=======================")


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a Decoy Duck!")
        print()
        print()
        print("=======================")
