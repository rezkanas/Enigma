from Plugboard import *
from RotorsnReflector import *
from Fernet import *


class AdvancedEnigmaMachine:
    def __init__(self, rotors, reflector, ring_setting, initial_position,
                 plug_board):
        self.rotor = RotorsReflector(rotors,
                                     reflector,
                                     ring_setting,
                                     initial_position)
        self.plug_board = Plugboard()
        for item in plug_board:
            self.plug_board.add(PlugLead(item))
        self.layer = additional_encrypt_layer()

    def encoding(self, string):
        enigma_output = ""
        for char in string:
            plug_board_output = self.plug_board.encode(char)
            rotor_output = self.rotor.rotor_encode(plug_board_output)
            enigma_output += self.plug_board.encode(rotor_output)
        # additional encryption layer
        output = self.layer.encrypt_message(enigma_output)

        return output

    # a new decoding function start with decrypting the message via
    # Fernet. Note: original EnigmaMachine class has only one
    # method "encoding".
    def decoding(self, string):
        enigma_output = ""
        decrypted = self.layer.decrypt_message(string)
        for char in decrypted:
            plug_board_output = self.plug_board.encode(char)
            rotor_output = self.rotor.rotor_encode(plug_board_output)
            enigma_output += self.plug_board.encode(rotor_output)

        return enigma_output
