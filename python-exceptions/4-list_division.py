#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    results = []
    while (i < list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except IndexError:
            result = 0
            print("out of range")
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        finally:
            results.append(result)
        i += 1
    return(results)
