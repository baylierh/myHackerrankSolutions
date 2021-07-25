# You are given a string. Split the string on a " " (space)
#  delimiter and join using a - hyphen.

def split_and_join(line):
    line = line.split(" ")
    new = ""
    count = 0
    for i in line:
        if count != len(line) - 1:
            new = new + i + "-"
            count += 1
        else:
            new = new + i
    return new

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)