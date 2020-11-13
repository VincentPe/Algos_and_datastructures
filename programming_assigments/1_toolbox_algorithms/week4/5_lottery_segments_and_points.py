# Uses python3
import sys
import numpy as np
import collections

def fast_count_segments1(starts, ends, points):
    cnt = [0] * len(points)
    
    points_idx = list(np.argsort(points))
    sort_points = sorted(points)
    sort_starts = sorted(starts)
    sort_ends = [x for _,x in sorted(zip(starts, ends))]
    
    for x in range(len(sort_points)):       
        
        if len(sort_starts) > 0:
            i = 0
            while sort_points[x] >= sort_starts[i]:
                print('check if points {} is in interval {}-{}'.format(sort_points[x], sort_starts[i], sort_ends[i]))
                if sort_starts[i] <= sort_points[x] <= sort_ends[i]:
                    cnt[x] += 1
                elif sort_points[x] > sort_starts[i]:
                    print('Removed segment {}-{} from segments'.format(sort_starts[i], sort_ends[i]))
                    sort_starts = sort_starts[1:]
                    sort_ends = sort_ends[1:]
                    break
                if i < len(sort_starts)-1:
                    i += 1
                else:
                    break

    return [cnt[x] for x in points_idx]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def fast_count_segments2(starts, ends, points):
    """
    The idea is to set labels for each of the arrays, sort them and apply
    counting of coverage technique.
    
    Explanation:
    https://www.coursera.org/learn/algorithmic-toolbox/discussions/all/threads/QJ1jK9wNEeWdPBL2iFTrAw/replies/Ihiw4txhEeWK5g7mfcS2Xw/comments/oyAMaeIiEeWyqwpvChh66Q
    """
    # The labels actually doesnt matter, they are just to recognize the start/end of segment or a point
    left_label, point_label, right_label = (1, 2, 3)
    count = [0] * len(points)
    
    # Regular dict object cannot be used here, because points are not unique.
    points_map = collections.defaultdict(set)
    
    # Create pairs between the events (left, point and right) and the event moment
    # e.g. a segment starts at 3 so one pair is [3, 1]
    pairs = []
    for i in starts:
        pairs.append((i, left_label))
    for i in ends:
        pairs.append((i, right_label))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        points_map[point].add(i)
        
    # Sort the events by the start time of the event
    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))
    
    # Coverage is the number of segments that you are currently in when you loop through the events
    coverage = 0
    # Loop through all of the event pairs and check what kind of event it is
    for pair in sorted_pairs:
        # If the event is a start of a segment increase nr of segments with 1
        if pair[1] == left_label:
            coverage += 1
        # If the event is the end of a segment decrease nr of segments with 1
        if pair[1] == right_label:
            coverage -= 1
        # If the event is a point, get all the indices from the points and give them the number of segments you are currently at
        if pair[1] == point_label:
            indices = points_map[pair[0]]
            for i in indices:
                count[i] = coverage

    return count
    
    

## Example 1
#s = 2
#p = 3
#
#s1 = [0,1,2,3,4,5]
#s2 = [7,8,9,10]
#
#points = [1, 6, 11]
#starts = [0, 7]
#ends = [5, 10]
## Output 1 0 0
#fast_count_segments(starts, ends, points)
#
## Example 2
#s = 1
#p = 3
#
#points = [-100, 100, 0]
#starts = [-10]
#ends = [10]
## Output 0 0 1
#fast_count_segments(starts, ends, points)
#
## example 3
#s = 3
#p = 2
#
#points = [1, 6]
#starts = [0, -3, 7]
#ends = [5, 2, 10]
## Output 2 0
#fast_count_segments2(starts, ends, points)
    

## Self made example
#points = [1, 6, 12, 16, 22, 29]
#starts = [0, 13, 19]
#ends = [2, 14, 22]
## output 1 0 0 0 1 0
#fast_count_segments(starts, ends, points)




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments2(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
