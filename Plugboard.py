"""
Plug board section
"""


class PlugLead:
    def __init__(self, mapping):
        # check for valid plug leads and raise value error message if condition
        # is not fulfilled. Below conditions check if input is two unique
        # alphabetical letters.
        if mapping.isalpha() and len(mapping) == 2 \
                and len(set(mapping)) == len(mapping):
            self.mapping = mapping
        else:
            raise ValueError("Invalid Plug lead")

    def encode(self, character):
        assert isinstance(character, str), 'entry character to be encoded ' \
                                           'should be a string'
        # when connected through the plug lead, return the connected letter
        # corresponding to the character otherwise leave character as is
        return ''.join([char for char in self.mapping if character != char]) \
            if character in self.mapping else character

    def lead_component(self):
        return self.mapping[0], self.mapping[1]

    def display(self):
        return self.mapping


class Plugboard:
    def __init__(self):
        self.plugboard = []
        self.__head = 0

    def is_full(self):
        return self.__head >= 10

    def is_empty(self):
        return self.__head == 0

    def evaluate_leads_before_adding(self, lead):
        x, y = lead.lead_component()
        if self.is_full():
            # when plug board capacity has been reached(10 leads are plugged),
            # an error message pops asking to remove a lead
            raise ValueError(
                f"plugboard is full, remove an existing lead before adding "
                f"new ones. The plug board has {plugboard.show()} leads "
                f"plugged at the moment")

        for item in self.plugboard:
            # validate that adding PlugLead("SZ") after PlugLead("TZ") won't be
            # allowed due to physical limitation, also conditions cover
            # PlugLead("SZ") and PlugLead("ZS"), otherwise, error message
            x1, y1 = item.lead_component()
            if x == y1 and y == x1:
                raise ValueError("plug lead is already there")
            elif x == x1 or x == y1 or y == x1 or y == y1:
                raise ValueError(
                    f"impossible to plug two leads, ('{x + y}','{x1 + y1}') "
                    f"into the same letter slot, be attention to physical "
                    f"limitation")
        return True

    def add(self, lead):
        if self.evaluate_leads_before_adding(lead):
            self.plugboard.append(lead)
            self.__head += 1

    def remove(self, lead):
        # check if the plug board is empty
        if self.is_empty():
            return
            # check if lead (asked to be removed) is plugged at the first place
        x, y = lead.lead_component()
        for item in self.plugboard:
            x1, y1 = item.lead_component()
            if x + y == x1 + y1 or x + y == y1 + x1:
                self.plugboard.remove(item)
                self.__head -= 1
                return print(f"plug board has {plugboard.show()} leads "
                             f"plugged at the moment")
        raise ValueError(
            f"{lead.display()} lead is not yet plugged, choose another "
            f"lead to be removed!, plug board has {plugboard.show()} leads "
            f"plugged at the moment")

    def encode(self, string):
        assert isinstance(string, str), 'entry character to be encoded should' \
                                        ' be a string'
        assert string.isupper(), 'entry character to be encoded should ' \
                               'be in uppercase'

        for item in self.plugboard:
            if item.encode(string) != string:
                return item.encode(string)
        return string

    def show(self):
        return [item.display() for item in self.plugboard]


if __name__ == "__main__":
    plugboard = Plugboard()

    plugboard.add(PlugLead("SZ"))
    plugboard.add(PlugLead("GT"))
    plugboard.add(PlugLead("DV"))
    plugboard.add(PlugLead("KU"))

    assert (plugboard.encode("K") == "U")
    assert (plugboard.encode("A") == "A")
