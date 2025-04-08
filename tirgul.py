def input_list (n):
    list_a = []
    for i in range (n):
        list_a.append(int(input("%d. Enter integer: "%(i+1))))
    return  (list_a)

def create_new_list (list_a, x):
    new_list = []
    for i in list_a:
        if i < x:
            new_list.append(i)
    for i in list_a:
        if i >= x:
            new_list.append(i)
    return new_list

def main():
    list_a = []
    new_list = []
    list_a = input_list(7)
    x = int(input("Enter x: "))
    print("Original list: ",list_a ) 
    new_list = create_new_list(list_a, x)
    print("New list: ", new_list) 
main()