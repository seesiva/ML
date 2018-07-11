"""
Given  names and phone numbers, assemble a phone book that maps friends'
names to their respective phone numbers. You will then be given an unknown 
number of names to query your phone book for. For each  queried, print 
the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for  is not found, print Not found instead.
"""

if __name__=='__main__':
    input_count=input()
    pair = dict()
    result = []
    """
    for i in range (0,T):
        word = raw_input().split()
        key = word [0]
        value = word [1]
        pair[key]=value
    """
    pair = dict((k,v) for k,v in [raw_input().split() for i in range(input_count)])

    while True:  
        try:           # Loop continuously
            inp = raw_input()   # Get the input
            key=inp
            if len(inp.strip())==0:       # If it is a blank line...
                break
            else:
                if key in pair:
                    value = pair[key]
                    result.append(key+"="+value)
                else:
                    result.append("Not found")
        except EOFError:
            break
    
    print('\n'.join(map(str, result)))


""""
Alternative Solution - 1

    #number of entries in phonebook
n = int(input().strip())
phoneBook = {}

#assign in phoneBook
for i in range(n):
    name, num = input().strip().split(' ')
    phoneBook[name] = num

#query phoneBook while there is input, exit when EOF
while(True):
    try:
        qName = input().strip()
        if qName in phoneBook:
            print('{}={}'.format(qName, phoneBook[qName]))
        else:
            print('Not found')
    except EOFError:
        break

"""

"""
Alternative Solution -2  : Looks elegant from the dictionary input stand point
input_count = int(input())
people = dict((k,v) for k,v in [input().split() for i in range(input_count)])
look_for = [input() for i in range(input_count)]

for item in look_for:
    if item in people:
        print("%s=%s" %(item, people[item]))
    else:
        print("Not found")
"""