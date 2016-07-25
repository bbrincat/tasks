
def binary_search(list, value):

    # Complexity O(logn)
    midpoint = len(list)//2
    if not len(list):
        return  False
    if list[midpoint] ==  value:
        return True
    else:
        if value < list[midpoint]:
            return binary_search(list[:midpoint],value)
        else:
            return binary_search(list[midpoint+1:], value)

if __name__ == "__main__":
    test = [1,2,3,4,5,6,7,8,9,10,11,15,45,68,102]
    print(binary_search(test, 133))
    print(binary_search(test, 102))