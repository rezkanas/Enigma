""" code 2 solution"""

import itertools
from enigma import *

possible_solutions = {}
final_starting_position = []
number_of_possibilities = 0

# cartesian product of ring setting with itself provides all possible
# combinations setting for the 3 ring with help of itertools.product()
Starting_positions_product = itertools.product(alphabet_list, repeat=3)

# looping through the itertools generator
for starting_position in Starting_positions_product:
    enigma_machine1 = EnigmaMachine(rotors=['Beta', 'I', 'III'],
                                    reflector='B',
                                    ring_setting=[23, 2, 10],
                                    initial_position=list(starting_position),
                                    plug_board=['VH', 'PT', 'ZG', 'BJ',
                                                'EY', 'FS'])
    decode = enigma_machine1.encoding(
        'CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH')
    if "UNIVERSITY" in decode:
        possible_solutions[starting_position] = decode
    number_of_possibilities += 1
print("\nNumber of studied possibilities is: ",
      number_of_possibilities, '\n*******\n')

for key, value in possible_solutions.items():
    print("\nPossible decodes:\n\n", value, '\n\ncorresponds to',
          key, ' initial rotor positions')
    print('*******\n')
