def estimate(time, observations, k):
    distance = lambda x: abs(time - x[0])
    sorted_observations = sorted(observations, key=lambda x: distance(x))
    i = 0
    while i < len(observations) and (i < k or
                                     distance(sorted_observations[i-1]) == 
                                     distance(sorted_observations[i])):
        i += 1
    return sum(obs[1] for obs in sorted_observations[:i]) / i

def main():
    observations = [
        (-1, 1),
        (0, 0),
        (-1, 1),
        (5, 6),
        (2, 0),
        (2, 3),
    ]

    for time in [-1, 1, 3, 3.5, 6]:
        print(estimate(time, observations, 2))

if __name__ == '__main__':
    main()