def list_func(n, command):
    lis = []
    for i in range(n):
        split_cmd = command[i].split(" ")
        cmd = split_cmd[0]
        if cmd == "insert":
            lis.insert(int(split_cmd[1]), int(split_cmd[2]))
            # print(lis)
        elif cmd == "print":
             print(lis)
             return lis
        elif cmd == "remove":
            lis.remove(int(split_cmd[1]))
        elif cmd == "append":
            lis.append(int(split_cmd[1]))
        elif cmd == "sort":
            lis.sort()
        elif cmd == "pop":
            lis.pop()
        elif cmd == "reverse":
            lis.reverse()
