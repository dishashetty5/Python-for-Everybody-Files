"""Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. The program should behave normally for all other files which
exist and don’t exist. Here is a sample execution of the program:"""
fname=input("enter the filename: ")
count=0
if fname=="na na boo boo":
    print("na na boo boo to you:you have been punk'd!")
    exit()
try:
    fhand=open(fname)
except:
    print("file cannot be opened",fname)
    exit()
for line in fhand:
    line=line.rstrip()
    if line.startswith("Subject"):
        count=count+1
print("there were",count,"subject line in",fname)
