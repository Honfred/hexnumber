class hexadecimal():
    def __init__(self, hex_string: str):
        if len(hex_string) >= 64:
            raise OverflowError("Длина числа не должна превышать 64 символов")
        self.hex_digits = list(hex_string.upper())

    # преобразование из 16-ричной в 10-тичную
    def to_int(self) -> int:
        hex_digits = self.hex_digits
        decimal_value = 0

        for digit in hex_digits:
            if digit.isdigit():
                decimal_value = decimal_value * 16 + int(digit)
            else:
                decimal_value = decimal_value * 16 + ord(digit.upper()) - 55

        return decimal_value

    # нормальный вывод 16-ричного числа
    def __str__(self) -> str:
        return '0x' + ''.join(self.hex_digits)