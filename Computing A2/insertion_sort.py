def InsertionSort(list, first, last):
    for count in range(first + 1, last + 1):
        current_value = list[count]
        pointer = count - 1
        while list[pointer] > current_value and pointer >= 0:
            list[pointer + 1] = list[pointer]
            pointer = pointer - 1
        list[pointer + 1] = current_value
    print(list)

list = ["Williams", "Smith", "Jones", "Nelson", "Peters", "King", "Adams", "Bond"]

InsertionSort(list, 0, len(list) - 1)

                 
