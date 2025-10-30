#RECURSION-is the process of defining something in terms of itself
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n*factorial(n-1))