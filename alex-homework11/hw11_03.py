def counts(n):
    count = 0
    n = abs(n)
    while n > 0:
        n //= 10
        count += 1
    return count


class Comparison:
    def __init__(self, value):
        self.value = value
        if isinstance(value, str) or isinstance(value, list):
            self.comp_value = len(value)
        elif isinstance(value, int):
            self.comp_value = counts(value)
        elif isinstance(value, dict):
            self.comp_value = len(value) * 2

    def __lt__(self, other):
        return self.comp_value < other.comp_value

    def __le__(self, other):
        return self.comp_value <= other.comp_value

    def __eq__(self, other):
        return self.comp_value == other.comp_value

    def __gt__(self, other):
        return self.comp_value > other.comp_value

    def __ge__(self, other):
        return self.comp_value >= other.comp_value
