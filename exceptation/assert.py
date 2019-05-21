try:
    num=int(input("Enter a even number"))
    assert num%2==0,"you have intered the Wrong valur"
except AssertionError as obj:
    print(obj)