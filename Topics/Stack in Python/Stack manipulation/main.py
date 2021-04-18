n = int(input())
my_stack = []
for _x in range(0, n):
    operation = str(input()).split()
    if operation[0] == 'PUSH':
        my_stack.append(operation[1])
    elif operation[0] == 'POP':
        my_stack.pop()

while len(my_stack) > 0:
    print(my_stack.pop())
