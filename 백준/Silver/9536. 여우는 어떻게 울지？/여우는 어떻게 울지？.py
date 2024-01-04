"""
간단한 입출력 문제
"""

import sys

f = sys.stdin.readline


def whatDoesTheFoxSay():
    SoundWords = f().split()
    AnimalSounds = []

    while 1:
        words = f().split()

        if words[1] == "goes":
            AnimalSounds.append(words[2])
        else:
            break

    answer = []

    for sound in SoundWords:
        if sound not in AnimalSounds:
            print(sound, end=" ")

    return 0


if __name__ == "__main__":
    n = int(f())

    for i in range(n):
        whatDoesTheFoxSay()
