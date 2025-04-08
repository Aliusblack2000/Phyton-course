def everithing_upper(ls):
    new_ls = []
    for i in ls:
        if i != " " and ord(i) >= 97:
            new_ls.append(chr(ord(i) - 32))
        else:
            new_ls.append(i)
    return new_ls
    
def my_ls(ls):
    lst = everithing_upper(ls)
    count = 0 
    maximum = 0
    minimum = 90
    for i in range(len(lst)):
        if ord(lst[i]) >=65 and ord(lst[i]) <= 90:
            count += 1
            if maximum < ord(lst[i]):
                maximum = ord(lst[i])
            if minimum > ord(lst[i]):
                minimum = ord(lst[i])
    if count == 0:
        return print ("There were no letters")
    return print("Largest and smallest letters are: ",chr(maximum), chr(minimum))

def main():
    ls = input("Enter your sentence: ")
    my_ls(ls)
main()
    