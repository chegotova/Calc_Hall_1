
import re
from fractions import Fraction
 
 
if __name__ == '__main__':
    prompt = "Введите пример:"
    while True:
        
        match = re.match(r"^\s*(?P<first>-?\d+)\s*(?P<operator>[+\-*/])\s*(?P<second>-?\d+)\s*$", input(prompt))
        if not match:
            raise ValueError("Некорректное выражение")
        action = match.group("operator")
       
        if match.group("operator") == r"/":
            sup = "⁰¹²³⁴⁵⁶⁷⁸⁹"
            sub = "₀₁₂₃₄₅₆₇₈₉"
            first, second = map(int, match.group("first", "second"))
            div, mod = divmod(first, second)
            fraction = Fraction(mod, second)
            print(*filter(None, (div, "⁄".join((sup[fraction.numerator], sub[fraction.denominator])))))
        else:
            print(eval(action.join(match.group("first", "second"))))
        
