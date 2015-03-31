import agstd.main as main
from agstd.cli import ProgressBar
import eikonal.solver as esolver
import eikonal.data as data
import numpy as np
import cPickle as pickle
from scipy.ndimage.interpolation import map_coordinates

import logging
log = logging.getLogger("Eikonal Solver")

from IPython.core.debugger import Tracer


def eikonalSolver(velocity, seed, second_order=True, traveltime=None):
    """
    :param velocity: velocity grid
    :type velocity: uQuake.core.data.grid.GridData
    :param seed: numpy array location of the seed or origin of seismic wave in
    model coordinates (usually location of a station or an event)
    :type seed: numpy array
    :param second_order: second_order eikonal equation solving (default: True)
    :type second_order: bool
    :param traveltime: traveltime grid
    :type traveltime: uQuake.core.data.grid.GridData
    """

    vel = velocity.copy()

    spacing = vel.spacing[0]
    shape = vel.shape

    vel.data = vel.data.copy(order='C')

    viscosity = np.zeros(np.array(shape) + 4, dtype='float64')
    viscosity.__setitem__([slice(2, -2)] * len(shape), 1.0
                          / vel.data.astype('float64'))

    tag = np.zeros(viscosity.shape, dtype='int32')
    tag.fill(2)
    tag.__setitem__([slice(2, -2)] * len(shape), 0)

    if not traveltime:
        traveltime = np.empty_like(viscosity)
        traveltime.fill(np.inf)

    if seed.ndim == 1:
        seed = seed[np.newaxis, :]
    seed = seed.astype('float64')

    seed = vel.transform_to(seed)

    esolver.SFMM(seed + 2.0, np.zeros(len(seed)).astype('float64'), tag, viscosity, traveltime,
                 spacing, second_order=second_order)

    traveltime = traveltime.__getitem__([slice(2, -2)] * len(shape))

    return traveltime


def esolve(velocity, rname, second_order=True, eventFile=None, stationFile=None):
    """
    :param velocity: A velocity grid in EKImageData or simply a pickled grid.
    :param seeds: Either a list of stations or a list of events
    :type seeds: EKStationTable or EKEventTable
    :param rname: root name for output file
    :type rname: str
    :param second_order: Boolean determining the order of the eikonal solver \
        used. 1st or 2nd order.

    :return: EKImageData reprenting the arrival grid.
    """
    seeds = np.load(stationFile)
    events = np.load(eventFile)
    pb = ProgressBar(max=len(seeds.data))
    ttid = 0
    for seed, k in zip(seeds.data['position'], seeds.data['id']):
        pb()
        fname = '%s%0.2d.pickle' % (rname, k)
        traveltime = eikonalSolver(velocity, np.array(seed))
        tt_table = []
        tts = map_coordinates(traveltime, velocity.transform_to(events.data['position']).T)
        for tt, ev_id in zip(tts, events.data['id']):
            tt_table.append((ttid, ev_id, tt))
            ttid += 1
        tt_table = np.array(tt_table, dtype=data.tt_dtype)
        tt = data.EKTTTable(tt_table, k, evnfile=eventFile, stafile=stationFile)
        pickle.dump(tt, open(fname,'w'))


if __name__ == "__main__":
    main.main(esolve, velocity=np.load, rname=str,
              second_order=bool, eventFile=str, stationFile=str)
