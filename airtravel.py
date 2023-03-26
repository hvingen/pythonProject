"""Model voor passagiersvluchten
"""


class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("NO airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number

    def number(self):
        return self._number

    def airlin(self):
               return self._number[:2]


class Aircraft:

        def __init__(self, registration, model, num_rows, num_seats_per_row):
            self.registration = registration
            self.model = model
            self.num_rows = num_rows
            self.num_seats_per_row = num_seats_per_row

        def registration(self):
            return self._registration

        def model(self):
            return self._model



