import sys
import io
import math

#Problem 1

txt = """UFRN
contest
AcM"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def letter_value(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def P1():
    while(True):
        word = stdin.readline().split()
        if not word:
            break
        word = word[0]
        if is_prime(sum(letter_value(letter) for letter in word)):
            print("It is a prime word.")
        else:
            print("It is not a prime word.")

P1()