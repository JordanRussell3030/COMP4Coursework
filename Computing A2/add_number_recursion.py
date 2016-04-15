def AddNumbers(number):
    if number == 0:
        return 0
    else:
        return number + AddNumbers(number - 1)
    
print(AddNumbers(993))



