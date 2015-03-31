import agstd.main as main
import eikonal.data as data
import numpy as np

import logging

# from IPython.core.debugger import Tracer
log = logging.getLogger("Random station generator")
# Defining the model parameters


def createRandomEvents(nbEvents, randomSeed, velocity, buffer=0.05):
    """
    Create a list of station randomly distributed in the volume
    emcompassed by the velocity model

    :param nbEvent: number of station add in the volume or surface
    encompassed by the velocity model
    :type nbEvent: int
    :param randomSeed: number to seed the random number generator
    :type randomSeed: int
    :param velocity: A velocity grin in EKImageData in pickle format
    :type velocity: EKImageData
    :param buffer: fraction of the volume on the edge where no station
    will be positioned
    :type buffer: float
    :rtype: EKEventTable
    """
    extent = [(a - 1) * b for a, b in zip(velocity.shape, velocity.spacing)]

    # creating event location

    np.random.seed(seed=randomSeed)
    loc = np.random.rand(nbEvents, 3)  # 3 dimensions

    for k in range(0, 3):
        loc[:, k] = loc[:, k] * (extent[k] - 2 * buffer * extent[k]) \
            + buffer * extent[k]

    stationLst = np.array([(k, l, 0) for k, l in enumerate(loc)],
                          dtype=data.st_dtype)

    stations = data.EKEventTable(data=stationLst)

    return stations


if __name__ == "__main__":
    main.main(createRandomEvents, nbEvents=int, randomSeed=int,
              velocity=np.load, buffer=float)
