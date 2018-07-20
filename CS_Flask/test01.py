from CS_Flask.src2.functions import square
# from src2.functions import square


x = 28


def squared(x):
    return x * x


for i in range(10):
    print(f"{i} squared is {square(i)}")
    print("{} squared is {}".format(i, squared(i)))
