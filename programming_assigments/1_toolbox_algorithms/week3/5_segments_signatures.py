# Uses python3
import sys
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    starts = np.array([])
    ends = np.array([])
    points = []
    for s in segments:
        starts = np.append(starts, s.start)
        ends = np.append(ends, s.end)   
    while len(starts) > 0:
        points.append(int(min(ends)))
        keep_indxs = starts > min(ends)
        starts = starts[keep_indxs]
        ends = ends[keep_indxs]
    return points

#segments = list([Segment(1, 3), Segment(2, 5), Segment(3, 6)])
#segments = list([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)])


#points = optimal_points(segments)
#print(*points)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

