# Description: A script that calculates the resistance of a 4-band resistor based on their colors
# Author: cedricouellet
# Date: 5 September 2020


# Color codes of a resistor's bands
COLOR_CODES = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'white': 9,

    # Colors that generally have more than one name
    'violet': 7, 'purple': 7,
    'gray': 8, 'grey': 8,
 }


class Resistor:
    """
    `color1` 1st Significant Value

    `color2` 2nd Significant Value

    `color3` Decimal Multiplier"""
    def __init__(self, color1, color2, color3):

        self.color1 = color1.lower()
        self.color2 = color2.lower()
        self.color3 = color3.lower()

    # Returns resistance (int)
    def get_resistance(self):

        value1 = COLOR_CODES.get(self.color1)
        value2 = COLOR_CODES.get(self.color2)

        multiplier = 10 ** COLOR_CODES.get(self.color3)

        # {color1}{color2} * 10 ** {color3}
        resistance = int(str(value1) + str(value2)) * int(multiplier)

        return resistance

    # Returns resistance followed by 'omh' (string)
    def show_resistance(self):

        resistance = self.get_resistance()
        suffix = ' ohm'

        result = str(resistance) + suffix

        return result


# Show each resistor in the resistor list
def show_resistors(resistors):

    i = 1

    print('--------------------------------------------------------------')

    for r in resistors:
        try:
            print(f'Resistor #{str(i)} : {r.show_resistance()}')
        except:
            print()
            print(f"Resistor #{str(i)} of {str(len(resistors))} has incorrect value(s).")

        i += 1

    print('--------------------------------------------------------------')


def main():
    resistors = []

    # Add resistors here
    resistors.append(Resistor('brown','blue','green'))

    show_resistors(resistors)


if __name__ == '__main__':
    main()
