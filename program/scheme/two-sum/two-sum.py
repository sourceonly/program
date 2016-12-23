def get_two_sum(list,target):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[i]+list[j+1]==target:
                return [i,j+1];


print get_two_sum([2,7,11,15],9)
