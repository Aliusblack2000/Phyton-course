
import math #математические функции
def height(v,a,t): #вспомогательная функция для высоты
    g = 9.81
    h = (v*math.sin(deg2rad(a))*t)-(g*t**2)/2
    return h
    
def horizontal(v,a,t): #всп функция для ширины  
    s = v*math.cos(deg2rad(a))*t
    return s

def deg2rad(a): #всп ф для переводы в радианы
    radians = (a/180)*(math.pi)
    return radians

def main():#основная функция
    v,a = eval(input("Enter v(0-100) m/s and a (0-90 degrees): "))
    while 100.0 >= v >= 0.0  and 90 >= a >= 0:#внешняя лула
        t = 0
        h = height(v, a, t) #возврат функции
        s = horizontal(v, a, t)#возврат функции
        while h >= 0: #внутренняя лула
            t += 0.1
            h = height(v, a, t)#возврат функции
            s = horizontal(v, a, t)  #возврат функции        
            print("Time: %.1f.....S=%5.2f H=%5.2f"%(t, s, h))
        print("Fallen\n")
        v,a = eval(input("Enter v(0-100) m/s and a (0-90 degrees): "))
    print("Finish\n")    

main()
