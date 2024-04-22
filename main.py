import pysnooper

@pysnooper.snoop()
def test():
    a = 99
    b = 32
    result = a + b
    return result


if __name__ == "__main__":
    print(test())