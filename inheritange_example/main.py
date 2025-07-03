from behavior import FlyWithWings
from duck import MallardDuck, RubberDuck, DecoyDuck, RedheadDuck


def main():
    mallard = MallardDuck()
    redhead = RedheadDuck()
    rubber = RubberDuck()
    decoy = DecoyDuck()

    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()

    redhead.display()
    redhead.perform_fly()
    redhead.perform_quack()

    rubber.display()
    rubber.perform_fly()
    rubber.perform_quack()

    decoy.display()
    decoy.perform_fly()
    decoy.perform_quack()

    # Change behaviors at runtime
    decoy.set_fly_behavior(FlyWithWings())
    decoy.perform_fly()


if __name__ == "__main__":
    main()
