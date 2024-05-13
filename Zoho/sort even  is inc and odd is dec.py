def sort_even_odd_alternate(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    for i in range(len(evens)):
        for j in range(i+1,len(evens)):
            if evens[i]>evens[j]:
                evens[i],evens[j]=evens[j],evens[i]
    print(evens)
    for i in range(len(odds)):
        for j in range(i+1,len(odds)):
            if odds[i]<odds[j]:
                odds[i],odds[j]=odds[j],odds[i]
    print(odds)

    result = []
    i = 0
    for index in range(len(arr)):
        if index % 2 == 0:
            result.append(evens[i])
        else:
            result.append(odds[i])
            i += 1

    return result
# Example usage
arr = [0,1,2,3,4,5,6,7]
sorted_arr = sort_even_odd_alternate(arr)
print(sorted_arr)
