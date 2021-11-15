def split_and_join(line):
    li = line.split(" ")
    l = "-".join(li)
    # write your code here
    return l

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
