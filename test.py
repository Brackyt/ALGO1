import numpy
import time
from parcours import parcours

if __name__ == "__main__":
    house_list = numpy.random.normal(0, 1000, 1000).tolist()
    start = time.time()
    parcours(house_list)
    stop = time.time()
    print(house_list)
    print(f"Parcours function took {stop - start} seconds.")