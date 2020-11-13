# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

## Deltere later
#def read_queries2(query_list):
#    return [Query(x.split()) for x in query_list]

def write_responses(result):
    print('\n'.join(result))

## Naive implementation
#def process_queries(queries):
#    result = []
#    # Keep list of all existing (i.e. not deleted yet) contacts.
#    contacts = []
#    for cur_query in queries:
#        if cur_query.type == 'add':
#            # if we already have contact with such number,
#            # we should rewrite contact's name
#            for contact in contacts:
#                if contact.number == cur_query.number:
#                    contact.name = cur_query.name
#                    break
#            else: # otherwise, just add it
#                contacts.append(cur_query)
#        elif cur_query.type == 'del':
#            for j in range(len(contacts)):
#                if contacts[j].number == cur_query.number:
#                    contacts.pop(j)
#                    break
#        else:
#            response = 'not found'
#            for contact in contacts:
#                if contact.number == cur_query.number:
#                    response = contact.name
#                    break
#            result.append(response)
#    return result

# Faster implementation
class PhoneBook:

    def __init__(self):
        self.book = [None] * 10000000

    def add(self, number, name):
        """Adds a person with name and phone number to the phone book.
        If there exists a user with such number already, then manager overwrites
        the corresponding name.
        """
        self.book[number] = name

    def delete(self, number):
        """Erases a person with number from the phone book.
        If there is no such person, then the query is ignored.
        """
        if self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        """Looks for a person with phone number.
        Replies with the person's name, or with string “not found”
        (without quotes) if there is no such person in the book.
        """
        if self.book[number] is None:
            return "not found"
        return self.book[number]
    
def process_queries(queries):
    """Helper function which reads queries from standard input,
    runs phonebook manager and sends the results to standard output.
    """
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.add(number, q[2])
        elif cmd == "find":
            print(phonebook.find(number))
        elif cmd == "del":
            phonebook.delete(number)


## Test case 1
#query_list = [
#    'add 911 police',
#    'add 76213 Mom',
#    'add 17239 Bob',
#    'find 76213',
#    'find 910',
#    'find 911',
#    'del 910',
#    'del 911',
#    'find 911',
#    'find 76213',
#    'add 76213 daddy',
#    'find 76213'
#]
#
#test = read_queries2(query_list)
#
#print(test[0].name)
#print(test[0].number)
#print(test[0].type)
#
#phonebook = PhoneBook()
#process_queries(query_list)





if __name__ == '__main__':
    phonebook = PhoneBook()
    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)
    
    #write_responses(process_queries(read_queries()))

