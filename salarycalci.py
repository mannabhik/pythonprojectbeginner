h = input("Enter hour:")
r = input("Enter rate:")
try:
    hour = float(h)
    rate = float(r)
    if (hour > 40):
        print("Overtime")
        sal = 40 * rate
        osal = (hour - 40) * (rate * 1.5)
        tsal = sal + osal
        print("Your salary:", tsal)
    else:
        print("General")
        sal = hour * rate
        print("Your salary:", sal)
except:
    print("Enter numeric value")