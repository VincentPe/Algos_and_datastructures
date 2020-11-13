# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def SiftDown(data, idxs):
    size = len(data)
    i = 0
    while True:
        smallest = i
        left = 2*i+1
        right = 2*i+2
        
        if (left < size) and (data[left] < data[smallest]):
            smallest = left
        
        if (right < size) and (data[right] < data[smallest]):
            smallest = right
            
        if (smallest != i): 
            swap = data[i]
            data[i] = data[smallest]
            data[smallest] = swap
            
            swap_idx = idxs[i]
            idxs[i] = idxs[smallest]
            idxs[smallest] = swap_idx
            
            i = smallest
            
        else:
            break
        
    return data, idxs
        
#data = [1,2,3,4,5,6,7]
#data[0] += 5
#idxs = [x for x in range(len(data))]
#
#SiftDown(data, idxs)


#def assign_jobs_naive(n_workers, jobs):
#    # TODO: replace this code with a faster algorithm.
#    result = []
#    next_free_time = [0] * n_workers
#    for job in jobs:
#        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#        next_free_time[next_worker] += job
#
#    return result


def assign_jobs_heap(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    idxs = [x for x in range(n_workers)]
    for job in jobs:
        next_worker = idxs[0]
        start_time_worker = next_free_time[0]
        result.append(AssignedJob(next_worker, start_time_worker))
        next_free_time[0] += job
        next_free_time, idxs = SiftDown(next_free_time, idxs)

    return result
    

## Test case 1
#n_workers = 2
#jobs = [1, 2, 3, 4, 5]
#assign_jobs_heap(n_workers, jobs)
#
## test case 2
#n_workers = 4
#jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#result = assign_jobs_heap(n_workers, jobs)
#result.sort(key=lambda tup: (tup[1],tup[0]))







def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_heap(n_workers, jobs)
    assigned_jobs.sort(key=lambda tup: (tup[1],tup[0]))

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
