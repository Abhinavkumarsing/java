import logging
logging.basicConfig(filename="mylg.log",level=logging.DEBUG)

try:
    a,b=[int(i) for i in input("Enter two value").split()]
    c=a/b
    logging.info("Division is in progress")
    print(c)

except ZeroDivisionError:
    print("please Enter Another Number")
    logging.error("Division by Zero")
else:
        print("you will inter a non-zero")
finally:
    print("program is Closed")
