def div():
    try:

        a= int(input("Enter the num1:"))
        b= int(input("Enter the num2:"))
        c= a/b
        print(c)

    except ValueError:
        print("Values should be int")
        div()

    except ZeroDivisionError:
        print("b Should not be zero")
        div()


div()



