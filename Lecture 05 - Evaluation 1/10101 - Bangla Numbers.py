import sys
import io

#Problem 5

txt = """23764
45897458973958"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def convert(number):
    words = []
    if number >= 10000000:
        # This is very useful (and it's actually the reason why I'm using an array
        # instead of a string)
        words.extend(convert(number // 10000000))
        words.append("kuti")
        number %= 10000000
    if number >= 100000:
        words.extend(convert(number // 100000))
        words.append("lakh")
        number %= 100000
    if number >= 1000:
        words.extend(convert(number // 1000))
        words.append("hajar")
        number %= 1000
    if number >= 100:
        words.extend(convert(number // 100))
        words.append("shata")
        number %= 100
    if number > 0:
        words.append(str(number))
    return words


def P6():
    while(True):
        number = stdin.readline()
        if not number:
            break
        number = int(number)
        words = convert(number)
        print(" ".join(words))
    
P6()