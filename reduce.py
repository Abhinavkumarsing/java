from functools import reduce

lst=[2,3,4,5]
result=reduce(lambda x,y:x+y ,lst)
print(result)