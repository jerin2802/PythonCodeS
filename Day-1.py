# Write your code below this line 👇
print("Hey, This is my Day-1 challenge.\n")
name = input("project name:\n")

n1 = input("first name:\n")
n2 = input("last name:\n")

print("Real name is:" +n1+ " " +n2)

n3=n1
n1=n2
n2=n3

print("passport name is:" +n1+ " " +n2)

n_without=n1+n2
print("without space name length is:\n")
print(len(n_without))

n_with = n1+ " " +n2
print("with space name length is:\n")
print(len(n_with))