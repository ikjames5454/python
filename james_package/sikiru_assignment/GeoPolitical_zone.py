import re
from enum import Enum


class GeoPolitical_Zone(Enum):
    NORTH_CENTRAL = "Benue", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"
    NORTH_EAST = "Adamawa", "bauchi", "borno", "gombe", "taraba", "yobe"
    NORTH_WEST = "kaduna", "katsina", "kano", "kebbi", "sokoto", "jigawa", "zamfara"
    SOUTH_EAST = "Abia", "Anambra", "Ebonyi", "Enugu", "Imo"
    SOUTH_SOUTH = "Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo,Rivers"
    SOUTH_WEST = "Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"


def conditions():

    while True:
        try:
            state = input("Enter the state: ")

            if not re.search(r'^(?!$)\D+$', state):
                print("not a state, try again: ")
                conditions()

            elif state.capitalize() in GeoPolitical_Zone.NORTH_CENTRAL.value:
                print("NORTH CENTRAL")
                break
            elif state.capitalize() in GeoPolitical_Zone.NORTH_EAST.value:
                print("NORTH EAST")
                break
            elif state.capitalize() in GeoPolitical_Zone.NORTH_WEST.value:
                print("NORTH WEST")
                break
            elif state.capitalize() in GeoPolitical_Zone.SOUTH_EAST.value:
                print("SOUTH SOUTH")
                break
            elif state.capitalize() in GeoPolitical_Zone.SOUTH_SOUTH.value:
                print("SOUTH SOUTH")
                break
            elif state.capitalize() in GeoPolitical_Zone.SOUTH_WEST.value:
                print("SOUTH WEST")
                break
            else:
                print("not a state, try again: ")
                conditions()
        except (ValueError, KeyboardInterrupt):
            print("not a right input:")
            conditions()



def main():
    conditions()


if __name__ == "__main__":
    main()
