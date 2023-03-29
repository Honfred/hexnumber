class hexadecimal():
    def __init__(self, int_number=[]):
        self.int_number = int_number  # массив из чисел для преобразования в 16-ричную систему
        self.hex_num = []  # массив из чисел в 16-ричной системе

        # перевод из десятичной в шестнадцатеричную систему
        for x in int_number:
            dec_hex = hex(int(x))[2:].upper()
            self.hex_num.append(dec_hex)

    # преобразование из 16-ричной в 10-тичную
    def to_int(self):
        int_num = []
        for num in self.hex_num:
            decimal_num = int(num, 16)
            int_num.append(decimal_num)
        return int_num

    # нормальный вывод 16-ричного числа
    def __str__(self):
        data = ""
        for num in self.hex_num:
            data += "0x" + ''.join(num) + ' '
        return data
