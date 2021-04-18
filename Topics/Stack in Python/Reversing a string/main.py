n = int(input())

my_stack = [input() for x in range(0, n)]
while len(my_stack) != 0:
    print(my_stack.pop())
