f=open("myfile.txt",'w')
print("Enter the text(In the finishing please enter # to finish)")
s=''
while s !='#' :

    s=input()
    f.write(s+'\n')

f.close