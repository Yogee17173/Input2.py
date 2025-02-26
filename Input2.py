# Execute Strong Number 
# Example: 145
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Hence, 145 is a Strong Number

# Write a program to check whether a given number is Strong Number or not.
s=input("Enter the number: ")

for i in s:
    i=int(i)
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact)