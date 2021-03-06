dataset = {
    0: [
        (6.413, 0.148),
        (2.328, 0.093),
        (2.371, 0.093),
        (3.288, 0.153),
        (3.164, 0.173),
        (2.491, 0.129),
        (2.222, 0.092),
        (4.514, 0.154),
        (3.007, 0.140),
        (5.038, 0.143),
    ],

    10: [
        (2.323, 0.122),
        (2.281, 0.120),
        (2.243, 0.127),
        (2.188, 0.118),
        (2.271, 0.124),
        (2.254, 0.122),
        (3.478, 0.166),
        (2.358, 0.122),
        (2.323, 0.122),
        (2.202, 0.120),
    ],

    100: [
        (2.298, 0.322),
        (3.160, 0.593),
        (2.345, 0.322),
        (2.321, 0.323),
        (4.891, 0.489),
        (3.522, 0.495),
        (2.296, 0.324),
        (2.266, 0.319),
        (4.448, 0.498),
        (2.276, 0.321),
    ],

    1000: [
        (2.333, 2.538),
        (2.364, 2.016),
        (2.857, 3.552),
        (2.282, 2.025),
        (3.152, 3.632),
        (3.485, 3.206),
        (3.449, 2.039),
        (3.143, 3.614),
        (2.301, 2.010),
        (2.480, 2.078),
    ],

    10000: [
        (2.212, 21.194),
        (2.228, 18.101),
        (2.265, 17.958),
        (2.490, 18.347),
        (2.336, 18.200),
        (3.250, 34.320),
        (2.778, 33.451),
        (2.940, 18.875),
        (2.865, 35.151),
        (3.982, 33.106),
    ],
}


def compute_avg(array):
    x = [t[0] for t in array]
    y = [t[1] for t in array]
    return (round(sum(x) / len(x), 3) * 1000, round(sum(y) / len(y), 3) * 1000)


avgs = [(offset, *compute_avg(dataset[offset])) for offset in dataset]
for e in avgs:
    print("%7d %6.0f %6.0f" % (e[0], e[1], e[2]))
