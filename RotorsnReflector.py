"""
rotors and reflector section
"""

alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]


class rotor_from_name:
    def __init__(self, label):
        # a switcher between rotor and reflector types.
        # In earlier version of this code, I used to have all
        # rotor and reflector types in lists outside the class
        # structure and call them when needed. I change and have them
        # created by a switcher when needed to be more memory efficient
        switcher = {
            'I': self.i(),
            'II': self.ii(),
            'III': self.iii(),
            'IV': self.vi(),
            'V': self.v(),
            'Gamma': self.gamma(),
            'Beta': self.beta(),
            'A': self.a(),
            'B': self.b(),
            'C': self.c()
        }
        try:
            self.label = switcher[label]
            self.label_name = label
        except TypeError:
            if len(label) == 26 and all(isinstance(n, str) for n in label):
                self.label_name = 'modified' # to resolve part 2 - code 5
                self.label = label
            else:
                raise ValueError(
                    f"undefined reflector or rotor, {label}, has been entered "
                    f"please enter one of the following valid rotors "
                    f"['Beta', 'Gamma', 'II', 'III', 'IV', 'V'] "
                    f"or one of the following valid reflector ['A', 'B', 'C']")

    @staticmethod
    def i():
        return [i for i in 'EKMFLGDQVZNTOWYHXUSPAIBRCJ']

    @staticmethod
    def ii():
        return [i for i in 'AJDKSIRUXBLHWTMCQGZNPYFVOE']

    @staticmethod
    def iii():
        return [i for i in 'BDFHJLCPRTXVZNYEIWGAKMUSQO']

    @staticmethod
    def vi():
        return [i for i in 'ESOVPZJAYQUIRHXLNFTGKDCMWB']

    @staticmethod
    def v():
        return [i for i in 'VZBRGITYUPSDNHLXAWMJQOFECK']

    @staticmethod
    def gamma():
        return [i for i in 'FSOKANUERHMBTIYCWLQPZXVGJD']

    @staticmethod
    def beta():
        return [i for i in 'LEYJVCNIXWPBQMDRTAKZGFUHOS']

    @staticmethod
    def a():
        return [i for i in 'EJMZALYXVBWFCRQUONTSPIKHGD']

    @staticmethod
    def b():
        return [i for i in 'YRUHQSLDPXNGOKMIEBFZCWVJAT']

    @staticmethod
    def c():
        return [i for i in 'FVPJIAOYEDRZXWGCTKUQSBNMHL']

    # encode a character by passing it through a rotor from right to left
    def encode_right_to_left(self, char):
        return self.label[alphabet_list.index(char)]

    # encode a character by passing it through a rotor from left to right
    def encode_left_to_right(self, char):
        return alphabet_list[self.label.index(char)]

    def show(self):
        return self.label_name


class RotorsReflector:
    def __init__(self, rotors, reflector, ring_setting, initial_position):
        # build instants of each rotor and fill them up in a list of objects
        # following the composition relationship
        self.rotor = []
        for item in rotors:
            self.rotor.append(rotor_from_name(item))
        # add initial position, reflector and ring settings
        self.reflector = rotor_from_name(reflector)
        self.position = initial_position
        self.ring_setting = ring_setting
        # find the notch of each rotor
        self.rotor_notch = self.notch(self.rotor)

    def rotor_encode(self, char):
        assert isinstance(char, str), 'entry character to be encoded should ' \
                                      'be a string'
        assert char.isupper(),      'entry character to be encoded should' \
                                    ' be in uppercase'
        # find the new position after entering the character
        self.position = self.new_position(self.rotor_notch, self.position)
        encoded_character_position = alphabet_list.index(char)
        # building a list with the alphabetical indices of the actual
        # rotor positions after the event of keyboard's key press
        alphabetical_indices_of_rotor_positions = []
        for item in map(alphabet_list.index, self.position):
            alphabetical_indices_of_rotor_positions.append(item)
        # off-set previous indices by the ring setting
        alphabetical_indices_of_rotor_position_after_ring_offset = []
        for index, ring in zip(
                alphabetical_indices_of_rotor_positions, self.ring_setting):
            alphabetical_indices_of_rotor_position_after_ring_offset.append(
                index-ring+1)
        # go through the multiple encoding stages of 3 rotor from right
        # to left, ending by a reflector
        j_temp = encoded_character_position
        for indexz, rotorz in zip(
                alphabetical_indices_of_rotor_position_after_ring_offset[::-1],
                self.rotor[::-1]):
            temp = self.alphabet_list_in_range_keeper(j_temp, indexz, '+')
            encoded_char = rotorz.encode_right_to_left(temp)
            index_encoded_char = alphabet_list.index(encoded_char)
            j_temp = self.alphabet_list_in_range_keeper(index_encoded_char,
                                                        indexz, '-')

        char_entering_reflector = alphabet_list[j_temp]
        char_exiting_reflector = self.reflector.encode_right_to_left(
            char_entering_reflector)
        # go back through multiple encoding stages of rotors from left
        # to right then return the output
        j2_temp = alphabet_list.index(char_exiting_reflector)
        for indexz1, rotorz1 in zip(
                alphabetical_indices_of_rotor_position_after_ring_offset,
                self.rotor):
            x = self.alphabet_list_in_range_keeper(j2_temp, indexz1, '+')
            char = rotorz1.encode_left_to_right(x)
            x = alphabet_list.index(char)
            j2_temp = self.alphabet_list_in_range_keeper(x, indexz1, '-')
        return alphabet_list[j2_temp]

    @staticmethod
    def alphabet_list_in_range_keeper(char_input, num, arithmetic_operator):
        if arithmetic_operator == '-':
            if abs(char_input-num) < 26:
                return alphabet_list.index(alphabet_list[char_input - num])
            else:
                return alphabet_list.index(
                    alphabet_list[char_input - num - 26])
        elif arithmetic_operator == '+':
            if abs(char_input + num) < 26:
                return alphabet_list[char_input + num]
            else:
                return alphabet_list[char_input + num - 26]

    @staticmethod
    def notch(rotor):
        notch = []
        for item in rotor:
            if item.label_name == 'I':
                notch.append("Q")
            elif item.label_name == 'II':
                notch.append("E")
            elif item.label_name == 'III':
                notch.append("V")
            elif item.label_name == 'IV':
                notch.append("J")
            elif item.label_name == 'V':
                notch.append("Z")
            else:
                notch.append(" ")  # when rotors/reflector are notch-less
        return notch

    def new_position(self, notch, position):
        alphabetical_indices_of_rotor_positions = []
        for item in map(alphabet_list.index, position):
            alphabetical_indices_of_rotor_positions.append(item)
        # double step, i.e. when 2nd rotor to right on its notch
        if alphabet_list[
            alphabetical_indices_of_rotor_positions[-2]] == notch[-2] \
                and notch[-1] != ' ':
            position[-2] = self.alphabet_list_in_range_keeper(
                alphabetical_indices_of_rotor_positions[-2], 1, '+')
            if notch[-2] != ' ':
                position[-3] = self.alphabet_list_in_range_keeper(
                    alphabetical_indices_of_rotor_positions[-3], 1, '+')
        # rightmost rotor reach its notch and push 2nd rotor to right a step
        if position[-1] == notch[-1] and notch[-1] != ' ':
            position[-2] = self.alphabet_list_in_range_keeper(
                alphabetical_indices_of_rotor_positions[-2], 1, '+')

        # regular rightmost rotor rotation
        position[-1] = self.alphabet_list_in_range_keeper(
            alphabetical_indices_of_rotor_positions[-1], 1, '+')
        return position

    def show(self):
        return [item.show() for item in self.rotor]


if __name__ == "__main__":
    # 1st case
    rotors1 = RotorsReflector(rotors=["I", "II", "III"],
                              reflector="B",
                              ring_setting=[1, 1, 1],
                              initial_position=['A', 'A', 'Z'])
    assert (rotors1.rotor_encode('A') == "U")
    # 2nd case
    rotors1 = RotorsReflector(rotors=["I", "II", "III"],
                              reflector="B",
                              ring_setting=[1, 1, 1],
                              initial_position=['A', 'A', 'A'])
    assert (rotors1.rotor_encode('A') == "B")
    # 3rd case
    rotors1 = RotorsReflector(rotors=["I", "II", "III"],
                              reflector="B",
                              ring_setting=[1, 1, 1],
                              initial_position=['Q', 'E', 'V'])
    assert (rotors1.rotor_encode('A') == "L")
    # 4th case
    rotors1 = RotorsReflector(rotors=["IV", "V", "Beta"],
                              reflector="B",
                              ring_setting=[14, 9, 24],
                              initial_position=['A', 'A', 'A'])
    assert (rotors1.rotor_encode('H') == "Y")
    # 5th case
    rotors1 = RotorsReflector(rotors=["I", "II", "III", 'IV'],
                              reflector="C",
                              ring_setting=[7, 11, 15, 19],
                              initial_position=['Q', 'E', 'V', 'Z'])
    assert (rotors1.rotor_encode('Z') == "V")
