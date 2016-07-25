
def count_ones(n):
    mid = len(n)//2
    if len(n)==1:
        return n[0]

    if len(n)== 2:
        if n[0] == 0:
            return n[1]
        else:
            return n[1]+1
    else:
        if n[mid] == 0 and n[mid+1] ==1:
            return len(n)-mid-1
        elif n[mid] == 0 and n[mid+1] == 0:
            return count_ones(n[mid+1:])
        elif n[mid] ==1:
            return count_ones(n[:mid]) + len(n)-mid


def most_ones(array):
    max_ones = 0
    max_index = 0
    for i,n in enumerate(array):
        num_ones = count_ones(n)
        if  num_ones > max_ones:
            max_ones = num_ones
            max_index = i

    return  max_index



if __name__ == "__main__":

    a = [
        [0,0,0,1],
        [0,1,1,1],
        [0,0,1,1],
        [0,1,1,1],
        [0,0,0,0],
    ]

    print(most_ones(a))

