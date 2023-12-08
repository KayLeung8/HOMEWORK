#Question1
file = open('hw3_q1.txt', 'r')

lines = file.readlines()

lst = []
for line in lines:
    line_split = line.split('')
    first_word = line_split[0]
    second_word = line_split[1]
    if first_word == 'JUMP':
        lst.insert(0,second_word)
    elif first_word == 'JION':
        lst.append(second_word)
print(lst)

#time complexity: O(n)
#space complexity: O(n)




#Question2
def num_in_seq(n):
    if n == 1:
        return 8
    else:
        return num_in_seq(n-1)+7




#Question3
base_url ='https://codefirstgirls.com/'
url = base_url
while True:
    print('You are currently on the URL %s' % url)
    print('Where are you clicking?')
    cur_location = url[url.rindex('/')+1: len(url)]
    if cur_location == '':
        options = ' Courses, Opportunities'
    elif cur_location == 'courses':
        options = ' CFGDegree, Back'
    elif cur_location == 'opportunities':
        options = '  Ambassadors, Back'
    else:
        options = ' Back'
    print('Options: %s' % options)
    option = input()
    if option == 'Back':
        url = url[0:url.rindex('/')]
        if url+'/' == base_url:
            url = url+'/'
    else:
        url = url.strip('/') + '/'+option.lower()
# time complexity: O(n)
# space complexity: O(1)
