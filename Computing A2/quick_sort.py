list = [2, 4, 6, 1, 7, 3, 9, 5, 8, 0]

def Quicksort(list, first, last):
    if first > last:
        pivot_value = list[first]
        left_pointer = first + 1
        right_pointer = last
        while left_pointer <= right_pointer:
            while list[left_pointer] < pivot_value and left_pointer <= right_pointer:
                left_pointer += 1
            while list[right_pointer] > pivot_value and left_pointer <= right_pointer:
                right_pointer -= 1
            if left_pointer < right_pointer:
                temp = list[left_pointer]
                list[left_pointer] = list[right_pointer]
                list[right_pointer] = temp
        pivot = right_pointer
        temp_2 = list[first]
        list[first] = list[pivot]
        list[pivot] = temp_2
        Quicksort(list, first, pivot - 1)
        Quicksort(list, pivot + 1, last)
    print(list)
        
Quicksort(list, 0, len(list) - 1)
