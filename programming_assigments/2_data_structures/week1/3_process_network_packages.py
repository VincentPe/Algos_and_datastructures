# python3
from collections import namedtuple

#S = 2 #buffer_size
#n = 2 #number of incomning packets
#
#arrival_times = [0, 0]
#process_times = [1, 1]

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buff_counter = []
#        self.Q = queue.Queue(maxsize=buffer_size) 
        self.finish_time = [0]
        
    def process_requests(self, requests):
        responses = []
        for request in requests:
            responses.append(self.process(request))
        return responses

    def process(self, request):
        
        if request[0] > (len(self.buff_counter) -1):
            for i in range(len(self.buff_counter), request[0]):
                self.buff_counter.append(0)
            for i in range(request[1]):
                self.buff_counter.append(1)
            self.finish_time.append(request[0] + request[1])
            return Response(False, request[0])
        
        elif self.buff_counter[request[0]] == self.buffer_size:
            return Response(True, -1)
        
        else:
            self.finish_time.append(self.finish_time[-1] + request[1])
            for i in range(request[0], len(self.buff_counter)):
                self.buff_counter[i] += 1
            for i in range(len(self.buff_counter), self.finish_time[-2] + request[1]):
                self.buff_counter.append(1)
            return Response(False, self.finish_time[-2])

class Buffer2:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.finish_time = []
        
    def process_requests(self, requests):
        responses = []
        for request in requests:
            responses.append(self.process(request))
        return responses

    def process(self, request):
        
        while len(self.finish_time) > 0:
            if self.finish_time[0] <= request[0]:
                del(self.finish_time[0])
            else:
                break
            
        if len(self.finish_time) == self.buffer_size:
            return Response(True, -1)
        
        elif len(self.finish_time) == 0:
            self.finish_time.append(request[0] + request[1])
            return Response(False, request[0])
        
        else:
            self.finish_time.append(self.finish_time[-1] + request[1])
            return Response(False, self.finish_time[-2])


#buffer_size, n_requests = S, n
#requests = []
#
#for i in range(n_requests):
#    arrived_at, time_to_process = arrival_times[i], process_times[i]
#    requests.append(Request(arrived_at, time_to_process)) 

#buffer = Buffer(buffer_size)
#responses = buffer.process_requests(requests)
#
#for response in responses:
#    print(response.started_at if not response.was_dropped else -1)
#    
#buffer2 = Buffer2(buffer_size)
#responses2 = buffer2.process_requests(requests)
#
#for response in responses2:
#    print(response.started_at if not response.was_dropped else -1)
#    
#responses == responses2
            
    
## Test solution
#import pandas as pd
#import datetime
#import os
#
#os.chdir('C:\\Users\\u02vpe\\OneDrive - TRANSAVIA AIRLINES C.V\\Documents\\Data Science training\\algos_and_structures_specialization\\' + 
#         '2_data_structures\\' + 'week1_basic_data_structures\\' + '3_network_simulation\\tests')
#    
#testfile_name = "{:02d}".format(21)
#testresult_name = "{:02d}".format(21) + '.a'
#
#f = open(testfile_name, "r")
#buffer_size, n_requests = map(int, f.readline().split())
#requests = []
#for _ in range(n_requests):
#    arrived_at, time_to_process = map(int, f.readline().split())
#    requests.append(Request(arrived_at, time_to_process))
#
#start = datetime.datetime.now()
#buffer = Buffer(buffer_size)
#responses = buffer.process_requests(requests)
#print(datetime.datetime.now() - start)
#
#start = datetime.datetime.now()
#buffer2 = Buffer2(buffer_size)
#responses2 = buffer2.process_requests(requests)
#print(datetime.datetime.now() - start)
#
#print('Same results: {}'.format(responses == responses2))




def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer2(buffer_size)
    responses = buffer.process_requests(requests)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
