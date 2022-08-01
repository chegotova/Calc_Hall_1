
class RationalFraction:
    def __init__(self, numerator_or_string, denominator=1):
        if isinstance(numerator_or_string, str):
            match = re.findall(r'^(-?\d+)/(\d+)$', numerator_or_string)
            if not match:
                raise ValueError('error')
            numerator_or_string, denominator = match[0]
        self.numerator = int(numerator_or_string)
        self.denominator = int(denominator)
        if self.denominator == 0:
            raise ValueError('Denominator is 0')
        self.reduce()
