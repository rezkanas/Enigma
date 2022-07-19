""" code 4 solution"""

import itertools
from enigma import *

possible_solutions = {}
number_of_possibilities = 0
config = []
# taking out the letters already used by plug leads
letters_left = ['D', 'E', 'K', 'L', 'M', 'O', 'Q', 'T', 'U', 'X', 'Y', 'Z']
# permutations of letters left using itertools.permutations
# as there are no replacement and ordering matters.
lead_leg_combination = itertools.permutations(letters_left, 2)

for x1, x2 in lead_leg_combination:
    enigma_machine1 = EnigmaMachine(rotors=['V', 'III', 'IV'],
                                    reflector='A',
                                    ring_setting=[24, 12, 10],
                                    initial_position=['S', 'W', 'U'],
                                    plug_board=['WP', 'RJ', f'A{x1}', 'VF',
                                                f'I{x2}', 'HN', 'CG', 'BS'])
    decode = enigma_machine1.encoding(
        'SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHC'
        'QGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW')
    if "TUTOR" in decode:
        possible_solutions[decode] = [x1, x2]
    number_of_possibilities += 1
print("\nNumber of studied possibilities is: ",
      number_of_possibilities, '\n*******\n')
temp = 1
for key, value in possible_solutions.items():
    print("\nPossible decode,", temp, ":\n\n", key,
          '\n\ncorresponds to (A ,', value[0],
          ') plug lead and (I ,', value[1], ') plug lead.')
    print('*******\n')
    temp += 1
