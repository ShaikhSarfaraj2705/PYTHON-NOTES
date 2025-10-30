#FIRST PROGRAM
#using print statements
print("hello world")
print(7)
print(7.5353422)
print(2,8)
print(53+32)
print("___________________________________________________________________________________")

def palindrome(s):
    return str(s)==str(s)[::-1]             #palindrome (12321=reverse(12321))
s=12321
print(palindrome(s))

if palindrome(s):
    print("is palindrome")
else:
    print("not palindrome")
print("")
print("___________________________________________________________________________________")


def fibonnacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")                #fibonacci (7=0,1,1,2,3,5,8)=0,1,0+1,1+2,2+3,3+5
        a,b=b,a+b
    
n=7
fibonnacci(n)
print("\n___________________________________________________________________________________")

text="sarfaraj"
reversed_string=text[::-1]              #reverse string
print(reversed_string)


reversed_string=""
for char in text:
    reversed_string=char+reversed_string
   
print(reversed_string)

reversed_string=""
str1=reversed_string.join(reversed(text))
print(str1)
print("___________________________________________________________________________________")

def factorial(n):
    val=1
    for i in range(1,n+1):                  #factorial 
        val=val*i
    return val
n=5
print(factorial(n))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print("___________________________________________________________________________________")

num=153
num_str=str(num)
power=len(num_str)
new=sum(int(digit)** power for digit in num_str)            #armstrong (153= 1^3+  5^3+  3^3)
print(new)
print("___________________________________________________________________________________")

def prime(n):
    for i in range(2,int(n**.5)+1):                     #prime num divisible by only 1 and itself
        if n%i==0:
            return False
    return True
n=2
print(prime(n))
print("___________________________________________________________________________________")

a=6
b=9
a=a+b
b=a-b                           #swap two num without using third variable
a=a-b
print(a)
print(b)

a,b=b,a
print(a)
print(b)
print("___________________________________________________________________________________")
year=1964
if(year %4==0 and year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("not leap year")