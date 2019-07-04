# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if segments[j][1]<segments[i][1]:
                segments[i], segments[j] = segments[j], segments[i]
    for i in range(len(segments)):
        if i == 0:
            points.append(segments[i][1])
        else:
            if segments[i][0]<=points[-1] and points[-1]<=segments[i][1]:
                pass
            else:
                points.append(segments[i][1])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
