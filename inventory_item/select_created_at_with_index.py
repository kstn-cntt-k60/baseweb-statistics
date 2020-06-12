dataset = {
    0: [
        (1.887, 0.275),
        (1.430, 0.265),
        (2.538, 0.263),
        (1.364, 0.172),
        (1.179, 0.158),
        (2.083, 0.316),
        (2.508, 0.294),
        (1.672, 0.213),
        (1.645, 0.211),
        (1.387, 0.141),
    ],
    10: [
        (1.537, 0.263),
        (1.620, 0.291),
        (3.099, 0.476),
        (1.523, 0.319),
        (1.980, 0.321),
        (1.376, 0.266),
        (2.329, 0.497),
        (2.106, 0.332),
        (1.402, 0.254),
        (1.114, 0.221),
    ],
    100: [
        (1.539, 0.767),
        (1.398, 0.562),
        (1.850, 1.195),
        (1.539, 0.784),
        (1.870, 0.814),
        (3.218, 1.079),
        (3.754, 1.394),
        (3.763, 1.654),
        (1.751, 0.787),
        (2.002, 1.035),
    ],
    1000: [
        (2.535, 9.657),
        (1.576, 4.267),
        (2.846, 7.744),
        (1.903, 7.710),
        (1.853, 4.466),
        (1.859, 6.921),
        (2.334, 6.057),
        (2.096, 6.806),
        (2.136, 8.413),
        (1.537, 4.945),
    ],
    10000: [
        (3.192, 37.776),
        (1.780, 41.543),
        (1.913, 34.042),
        (2.020, 37.783),
        (1.606, 34.735),
        (1.480, 38.796),
        (2.233, 39.617),
        (1.676, 36.512),
        (1.653, 38.105),
        (1.404, 43.196),
    ],
}

def compute_avg(array):
    x = [t[0] for t in array]
    y = [t[1] for t in array]
    return (round(sum(x) / len(x), 3), round(sum(y) / len(y), 3))

avgs = [(offset, *compute_avg(dataset[offset])) for offset in dataset]
for e in avgs:
    print("%7d %6.3f %6.3f" % (e[0], e[1], e[2]))