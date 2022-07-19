from Plugboard import *
from RotorsnReflector import *


class EnigmaMachine:
    def __init__(self, rotors, reflector, ring_setting, initial_position,
                 plug_board):
        # rotors and plug board are parts of enigma machines. hence they have
        # compositions relationships.
        self.rotor = RotorsReflector(rotors,
                                     reflector,
                                     ring_setting,
                                     initial_position)
        self.plug_board = Plugboard()
        for item in plug_board:
            self.plug_board.add(PlugLead(item))

    def encoding(self, string):
        output = ""
        for char in string:
            # each character will pass first by plug board stage then
            # goes through rotors and reflector just to finish with
            # plug board again before lamp board section.
            plug_board_output = self.plug_board.encode(char)
            rotor_output = self.rotor.rotor_encode(plug_board_output)
            output += self.plug_board.encode(rotor_output)
        return output


if __name__ == "__main__":
    # exercise 1
    enigma_machine1 = EnigmaMachine(rotors=["I", "II", "III"],
                                    reflector="B",
                                    ring_setting=[1, 1, 1],
                                    initial_position=['A', 'A', 'Z'],
                                    plug_board=['HL', 'MO', 'AJ', 'CX',
                                                'BZ', 'SR', 'NI', 'YW',
                                                'DG', 'PK'])
    assert(enigma_machine1.encoding('HELLOWORLD') == "RFKTMBXVVW")

    # exercise 2
    enigma_machine2 = EnigmaMachine(rotors=["IV", "V", "Beta", "I"],
                                    reflector="A",
                                    ring_setting=[18, 24, 3, 5],
                                    initial_position=['E', 'Z', 'G', 'P'],
                                    plug_board=['PC', 'XZ', 'FM', 'QA',
                                                'ST', 'NB', 'HY', 'OR',
                                                'EV', 'IU'])
    print(enigma_machine2.encoding('BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXV'
                                   'HOGCUUIBCVMPUZYUUKHI'))
