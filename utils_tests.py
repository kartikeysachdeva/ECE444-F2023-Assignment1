from utils import utils

# Test the reversed function
def test_reversed():
    util = utils()
    reversed_result = util.reversed(12345)
    if reversed_result == 54321:
        print("reversed test for integer passed")
    else:
        print("reversed test for integer failed")

    reversed_result = util.reversed("12345")
    if reversed_result is None:
        print("reversed test for string passed")
    else:
        print("reversed test for string failed")

    reversed_result = util.reversed(12.345)
    if reversed_result is None:
        print("reversed test for float passed")
    else:
        print("reversed test for float failed")

# Test the formatter function
def test_formatter():
    util = utils()
    formatter_result = util.formatter(10)
    if formatter_result == ('0b1010', '0o12'):
        print("formatter test for integer passed")
    else:
        print("formatter test for integer failed")

    formatter_result = util.formatter("10")
    if formatter_result is None:
        print("formatter test for string passed")
    else:
        print("formatter test for string failed")

    formatter_result = util.formatter(12.345)
    if formatter_result is None:
        print("formatter test for float passed")
    else:
        print("formatter test for float failed")

if __name__ == '__main__':
    test_reversed()
    test_formatter()
