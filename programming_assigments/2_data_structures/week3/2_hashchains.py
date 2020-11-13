# python3

## Naive implementation

#class Query:
#
#    def __init__(self, query):
#        self.type = query[0]
#        if self.type == 'check':
#            self.ind = int(query[1])
#        else:
#            self.s = query[1]

#class QueryProcessor:
#    _multiplier = 263
#    _prime = 1000000007
#
#    def __init__(self, bucket_count):
#        self.bucket_count = bucket_count
#        # store all strings in one list
#        self.elems = []
#
#    def _hash_func(self, s):
#        ans = 0
#        for c in reversed(s):
#            ans = (ans * self._multiplier + ord(c)) % self._prime
#        return ans % self.bucket_count
#
#    def write_search_result(self, was_found):
#        print('yes' if was_found else 'no')
#
#    def write_chain(self, chain):
#        print(' '.join(chain))
#
#    def read_query(self):
#        return Query(input().split())
#
#    def process_query(self, query):
#        if query.type == "check":
#            # use reverse order, because we append strings to the end
#            self.write_chain(cur for cur in reversed(self.elems)
#                        if self._hash_func(cur) == query.ind)
#        else:
#            try:
#                ind = self.elems.index(query.s)
#            except ValueError:
#                ind = -1
#            if query.type == 'find':
#                self.write_search_result(ind != -1)
#            elif query.type == 'add':
#                if ind == -1:
#                    self.elems.append(query.s)
#            else:
#                if ind != -1:
#                    self.elems.pop(ind)
#
#    def process_queries(self):
#        n = int(input())
#        for i in range(n):
#            self.process_query(self.read_query())
            
# Faster implementation
class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        """Hash function."""
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        """Insert string into the table.
        If there is already such string in the hash table,
        then the query is ignored.
        """
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket

    def delete(self, string):
        """Removes string from the table.
        If there is no such string in the hash table,
        then the query is ignored.
        """
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    def find(self, string):
        """Looks up for the string in the table.
        Returns “yes” or “no” (without quotes) depending on whether
        the table contains string or not.
        """
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"

    def check(self, i):
        """Returns the content of the i-th list in the table."""
        return self.buckets[i]
    
def process_queries(queries):
    """Helper function which reads queries from standard input,
    runs query processor and sends the results to standard output.
    """
    for query in queries:
        command, arg = query.split()
        if command == "add":
            qp.add(arg)
        elif command == "del":
            qp.delete(arg)
        elif command == "find":
            print(qp.find(arg))
        elif command == "check":
            arg = int(arg)
            print(" ".join(qp.check(arg)))
            
            
## Test case 1
#queries = [
#        'add world',
#        'add HellO', 
#        'check 4',
#        'find World',
#        'find world',
#        'del world',
#        'check 4',
#        'del HellO',
#        'add luck',
#        'add GooD',
#        'check 2',
#        'del goodv'
#]
#
#qp = QueryProcessor(bucket_count=5)
#process_queries(queries)
            
            
## Testing code pieces    
#word = 'world'
#[ord(x) for x in word]
#
#_multiplier = 263
#_prime = 1000000007
#bucket_count = 5
#
#ans = 0
#for c in reversed(word):
#    ans = (ans * _multiplier + ord(c)) % _prime
#ans % bucket_count
#    
#_hash = 0
#for idx, c in enumerate(word):
#    if idx == 0:
#        _hash += ord(c) 
#    else:
#        _hash += ord(c) * _multiplier**idx
#    _hash = _hash % _prime
#
#_hash % bucket_count



if __name__ == '__main__':
    bucket_count = int(input())
    n = int(input())

    qp = QueryProcessor(bucket_count)
    queries = [input() for i in range(n)]
    process_queries(queries)
