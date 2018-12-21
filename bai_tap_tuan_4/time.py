task = int(input("Moi nhap vao so nhiem vu: "))
max_time = int(input("thoi gian toi da la : "))
list_time = []
for i in range (task):
    time_1task = int(input("thoi gian thuc hien nhiem vu thu {0} la : ".format(i+1)))
    list_time.append(time_1task)
print(", ".join(str(x) for x in list_time))
count = 0
sum_time = list_time[0]
for i in range (task):   
    if sum_time <= max_time:
        sum_time += list_time[i+1]
        count +=1
    else:
        break          
print(count)