""" code 1 solution"""

from enigma import *

for reflector in ['A', 'B', 'C']:
    enigma_machine1 = EnigmaMachine(rotors=['Beta', 'Gamma', 'V'],
                                    reflector=reflector,
                                    ring_setting=[4, 2, 14],
                                    initial_position=['M', 'J', 'M'],
                                    plug_board=['KI', 'XN', 'FL'])
    decode = enigma_machine1.encoding(
            'DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ')
    if "SECRETS" in decode:  # cross check each decode against the crib
        print('Possible decode:', decode, '\nReflector:', reflector)
