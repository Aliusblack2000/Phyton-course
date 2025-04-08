def my_avg(list_time,num_of_run):
    sum = 0 
    for x in list_time:
        sum += x
    time_avg = sum / num_of_run
    print("Time average is %.2f"%(time_avg))
    return time_avg

def main():
    counter = 0
    time_avg = 0
    num_of_run = 0
    num_of_run = int(input("Enter number of runners: "))
    list_time = []
    for i in range(num_of_run):
        list_time.append(float(input("%d. Enter time: "%(i+1))))
    time_avg = my_avg(list_time, num_of_run)
    for i in list_time:
        if i < time_avg:
            counter += 1
    print("The number of runners, running below average time is %d."%(counter))    
            
main()