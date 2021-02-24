import random


def sampleOfflineData(k, array):
    for i in range(k):
        randomNumber = random.randint(i, len(array) - 1)
        array[i], array[randomNumber] = array[randomNumber], array[i]
