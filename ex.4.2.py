def main():
    num = int(input("Please enter a 4-digits natural number:"))

    if num < 0:
        print("%d isn't a natural number."% num)
    elif num<1000 or num>9999:
        print("%d isn't a 4-digits number."% num)
    units = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100)%10
    thousands = num // 1000
    dif1 = thousands - hundreds
    dif2 = hundreds - tens
    dif3 = tens - units
    if dif1 == dif3 == dif2 and thousands < hundreds < tens < units:
        print("Increasing arithmetic sequence.")
    elif dif1 == dif3 == dif2 and thousands > hundreds > tens > units:
        print("Decreasing arithmetic sequence.")
    if thousands >= hundreds >= tens >= units:
        print("Decreasing sequence.")
    elif thousands <= hundreds <= tens <= units:
        print("Increasing sequence.")
    if thousands == hundreds == tens == units:
        print("All digits are the same.")
main()