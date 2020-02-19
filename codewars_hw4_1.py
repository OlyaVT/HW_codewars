arr = [10,12,19,-7,-8]

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        a = len([x for x in arr if x>0])
        b = sum([x for x in arr if x<0])
        return [a,b]

print(count_positives_sum_negatives(arr))