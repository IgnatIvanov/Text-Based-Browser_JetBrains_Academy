n = int(input())
to_read = []
readed_books = []
for _x in range(0, n):
    action = str(input())
    if action[0] == "B":
        to_read.append(action[4:])
    elif action[0] == "R":
        readed_books.append(to_read.pop())

# while len(readed_books) > 0:
#     print(readed_books.pop())
for book in readed_books:
    print(book)
