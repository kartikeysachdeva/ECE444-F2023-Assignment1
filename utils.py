class utils:
    def reversed(self, number):
        if isinstance(number, int):
            return int(str(number)[::-1])
        print("Input must be an integer")
        return None

    def formatter(self, number):
        if isinstance(number, int):
            return bin(number), oct(number)
        print("Input must be an integer")
        return None
    