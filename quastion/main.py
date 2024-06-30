#1)
# a = int(input("PLEASE GIVE YOUR FIRST NUMBER"))
# b = int(input("PLEASE PROVIDE YOUR 2ND NUMBER"))

# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{b} is greater than {a}")
# else:
#     print("both the numbers are equal")

#2)
# gender = input("provide your gender as F or M")

# if gender == "M" or gender == "m":
#     print("Good morning Sir")
# elif gender == "F" or gender == "f":
#     print("Good morning Mam")
# else:
#     print("Wrong input")

#3)
# a = int(input("please provide your number"))

# if a %2 == 0:
#     print("my number is even")
# else:
#     print("my number is odd")


#4)

# name = input("please tell your name")
# age = int(input("please tell your age"))

# if age >= 18:
#     print(f"hello {name} you are a valid voter")
# elif age <18 and age >0:
#     print(f"hello {name} you are not a valid voter")
# else:
#     print("give a valid age")


#6)

# z = input("please give a character")

# if z in "aeiouAEIOU":
#     print("its a vowel")
# else:
#     print("its a consonent")

#loops question
#1)
# n = int(input("PLEASE TELL YOUR NUMBER"))

# for i in range(1,n+1):
#     print(i)



#2)
# n = int(input("please give your number"))

# for i in range(n,-1,-1):
#     print(i)

#3)

# n = int(input("which number table you want"))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

#4)
# n = int(input("please tell your number"))
# sum = 0
# for i in range(1,n+1):   
#     sum = sum + i

# print(sum)


#5)
# n = int(input("please tell your number"))

# fact = 1

# for i in range(1,n+1):
#     fact = fact *i

# print(fact)


#6)

# n = int(input("please tell your number"))
# print("all the factors are")
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i,end = " ")

#7)

# n = int(input("tell your number"))

# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("yes this is a strong number")
# else:
#     print("not a strong number") 

#8)

# n = int(input("tell your number"))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count +1

# if count == 2:
#     print("prime number")
# else:
#     print("composite number")


#9)

# a = int(input("please tell your number"))
# while a > 0:
#     print(a%10)
#     a = a//10


#10)

# n = int(input("tell your number"))
# copy = n
# rev = 0
# while n > 0:
#     z = n%10
#     rev = rev *10 + z
#     n = n//10

# if copy == rev:
#     print("PALLINDROMIC NUMBER")
# else:
#     print("NOT A PALLINDROMIC NUMBER")