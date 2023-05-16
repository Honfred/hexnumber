class hexadecimal():
    def __init__(self, hex_string: str):
        if len(hex_string) >= 64:
            raise OverflowError("Длина числа не должна превышать 64 символов")
        self.hex_digits = list(hex_string.upper())

    # преобразование из 16-ричной в 10-тичную
    def to_int(self) -> int:
        return int(''.join(self.hex_digits), 16)

    # нормальный вывод 16-ричного числа
    def __str__(self) -> str:
        return '0x' + ''.join(self.hex_digits)
