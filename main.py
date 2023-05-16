from hexdecimal import hexadecimal as hex

def main():
    while (True):
        try:
            hexnum = hex(input())
            print(hexnum)
            print(hexnum.to_int())

            return False
        except Exception as e:
            print(e)



if __name__ == '__main__':
    main()
