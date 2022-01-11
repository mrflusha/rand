import string
import random

rand_str = string.punctuation


def main(text):
    rand = "".join(random.choice(rand_str) for i in range(text))
    str2 = str()
    for i in range(text):
        string = " "
        str2 = str2 + string
        print(str2  + rand[i])


main(random.randrange(500))
