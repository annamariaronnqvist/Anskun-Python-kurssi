name = input("Please share your first name:")
print("Hi," + name + ", Good Evening! ")

lastname = input("Please share your last name:")
print("Hi," + lastname + ", Good to see you ")

age = 75

print("Hi," ,name, lastname + ", Good to see you ")
print("hi " + name + str(age) + " years")

# str(age) tarkoittaa castaamista, eli muuntofunktiota

age2 = int(input("Anna Ikäsi: "))

print("hi, ",name, age2, "years.")