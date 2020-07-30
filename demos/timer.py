import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.perf_counter

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, *kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def best_of(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps run.
    Returns (best time, last result)
    """
    best = 2**16
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        best = min(best, elapsed)
    return (best, ret)

def best_of_total(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return best_of(reps1, total, reps2, func, *pargs, **kargs) 
