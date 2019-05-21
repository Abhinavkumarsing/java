import logging
logging.basicConfig(filename="Assign.log",level=logging.DEBUG)

try:
    Passw=input("Enter the Password")
    assert len(Passw)>=8,"Please Enter Atleast 8 char"
    

except AssertionError as obj:
    print(obj)
    logging.error("invalid password")
