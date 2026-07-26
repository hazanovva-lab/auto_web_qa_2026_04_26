class Rectangle:
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Reactangle sides can't be les than 0")

        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b