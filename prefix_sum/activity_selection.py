def activitySelection(start, finish):
    #code here
    
    def sort(start , finish):
        for i in range(len(start)):
            for j in range(i + 1,len(finish)):
                
                if finish[i] > finish[j]:
                    
                    finish[i] , finish[j] = finish[j] , finish[i]
                    start[i] , start[j] = start[j] , start[i]
    
    count = 1
    
    sort(start, finish)

    print(start, finish)
    
    prev_start = start[0]
    
    for i in range(1,len(start)):
        
        if start[i] > prev_start:
            count += 1
            prev_start = start[i]
    
    return count

start= [1, 3, 0, 5, 8, 5] 
finish = [2, 4, 6, 7, 9, 9]

print(activitySelection(start,finish))
                        