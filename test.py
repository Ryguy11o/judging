import itertools
a = [1]*50
a[20:] = zip(*zip(a[20:],itertools.repeat(0)))[1]