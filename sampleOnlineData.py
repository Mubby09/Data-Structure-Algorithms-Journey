import itertools
import random


def sampleOnlineData(iterable, size):
    running_sample = list(itertools.islice(iterable, size))

    sizeSeenSoFar = size
    for i in iterable:
        sizeSeenSoFar += 1

        indexToReplace = random.randrange(sizeSeenSoFar)

        if indexToReplace < size:
            running_sample[indexToReplace] = i

    return running_sample


print(sampleOnlineData([2, 4, 6, 2, 4, 8, 23, 78, 0, 45, 3, 22,
                        79, 36, 12, 21, 67, 98, 334, 3392], 3))
