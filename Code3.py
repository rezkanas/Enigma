""" code 3 solution"""

import itertools
from enigma import *

possible_solutions = {}
number_of_possibilities = 0

# cartesian product of the 4 rotors types
RoToRs4 = ['II', 'IV', 'Beta', 'Gamma']
# convert to list to iterate multiple time
rotor_combination_3 = list(itertools.product(RoToRs4, repeat=3))
# combining two range of even ring settings then take the
# cartesian product of possible ring setting.
combine = itertools.chain(range(2, 9, 2), range(20, 27, 2))
ring_setting_combination = itertools.product(combine, repeat=3)
reflectors = ['A', 'B', 'C']

for item3 in ring_setting_combination:
    for item2 in reflectors:
        for item1 in rotor_combination_3:
            enigma_machine1 = EnigmaMachine(rotors=list(item1),
                                            reflector=item2,
                                            ring_setting=list(item3),
                                            initial_position=['E', 'M', 'Y'],
                                            plug_board=['FH', 'TS', 'BE',
                                                        'UQ', 'KD', 'AL'])
            decode = enigma_machine1.encoding(
                'ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTH'
                'LCDRZRFZHKNRSDLNPFPEBVESHPY')
            if "THOUSANDS" in decode:
                possible_solutions[decode] = [item1, item2, item3]
            number_of_possibilities += 1
# display the results
print("\nNumber of studied possibilities is: ",
      number_of_possibilities, '\n*******\n')
for key, value in possible_solutions.items():
    print("\nPossible decodes:\n\n", key, '\n\ncorresponds to',
          value[0], 'rotors, ', value[1], 'reflector, ',
          value[2], 'ring setting.')
    print('*******\n')
