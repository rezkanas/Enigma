""" code 5 solution"""

import itertools
from enigma import *

number_of_possibilities = 0
possible_solutions = {}
crib = ['FACEBOOK', 'TWITTER', 'YOUTUBE', 'INSTAGRAM', 'LINKEDIN', 'SNAPCHAT']


# define a function that get permutations of a list whose all elements are in
# a different place than the original. e.g. valid combinations for
# ('E', 'J', 'M', 'Z') are ('J', 'E', 'Z', 'M'), ('M', 'Z', 'E', 'J'),
# ('Z', 'M', 'J', 'E') while ('E', 'J', 'Z', 'M'), ('J', 'J', 'E', 'Z')
# are not.
def get_permutations(original_elements):
    for permutation in itertools.permutations(original_elements):
        if any(left == right for left, right in
               zip(permutation, original_elements)):
            continue
        else:
            yield permutation


# starting a for loop with all three original reflectors as we are not aware
# which was modified.
A = [i for i in 'EJMZALYXVBWFCRQUONTSPIKHGD']
B = [i for i in 'YRUHQSLDPXNGOKMIEBFZCWVJAT']
C = [i for i in 'FVPJIAOYEDRZXWGCTKUQSBNMHL']
for reflector in [A, B, C]:
    dicts = {}
    # copy reflector to a new list that would evolve in a separate path to
    # original reflector list hence does not override original reflector.
    modified = reflector.copy()
    # as wire has two ends and they are connected both ways, then if I fill a
    # dictionary with the wires end that comes first in alphabet_list
    # and appear later in the modified reflector then remove these values
    # from modified list, e.g. modified A is
    # ['E', 'J', 'M', 'Z', 'L', 'Y', 'X', 'V', 'W', 'R', 'Q', 'U', 'T']
    for i, item in enumerate(modified):
        if item in alphabet_list[:i]:
            dicts[i] = item
    for value in dicts.values():
        modified.remove(value)
    # I build permutations of 4 letters from the modified list and convert
    # it to list as I generators are exhausted with one-time looping.
    unique_4_letters_combination = list(itertools.permutations(modified, 4))
    for unique_letters in unique_4_letters_combination:
        dicts2 = {}
        modified2 = modified.copy()
        # e.g. unique_letters combination = (['E','J','M','Z'])
        # same what I applied on line 38, as I need to preserve the order of
        # the modified list so I can bring back the combinations to their
        # elements' original indices.
        for element in unique_letters:
            dicts2[modified2.index(element)] = element
        for value in dicts2.values():
            modified2.remove(value)
        # calling the function I define above and getting permutations of a
        # list whose all elements are in a different place to the original
        wire_ends_changes = list(get_permutations(unique_letters))
        for comb in wire_ends_changes:
            # restoring the elements of the list
            wires = []
            temp = 0
            modified3 = modified2.copy()
            for key, value in dicts2.items():
                modified3.insert(key, comb[temp])
                temp += 1
            for key, value in dicts.items():
                modified3.insert(key, value)
            # changing the other end of the wire following the combination
            for item in comb:
                modified3[alphabet_list.index(item)] =\
                    alphabet_list[modified3.index(item)]

            # inject the modified reflector 'modified3' and build and
            # enigma machine object
            enigma_machine1 = EnigmaMachine(rotors=['V', 'II', 'IV'],
                                            reflector=modified3,
                                            ring_setting=[6, 18, 7],
                                            initial_position=['A', 'J', 'L'],
                                            plug_board=['UG', 'IE', 'PO',
                                                        'NX', 'WT'])
            decode = enigma_machine1.encoding('HWREISXLGTTBYVXRC'
                                              'WWJAKZDTVZWKBDJPVQYNEQIOTIFX')
            for social_media in crib:
                if social_media in decode:
                    possible_solutions[decode] = modified3
            number_of_possibilities += 1
print("\nNumber of studied possibilities is: ", number_of_possibilities,
      '\n******************************************\n')
temp = 1
for key, value in possible_solutions.items():
    print("\nPossible decode", temp, ":\n\n", key,
          '\n\ncorresponds to non-standard modified', value,
          ' reflector. The basis of this reflector is:', reflector)
    temp += 1
