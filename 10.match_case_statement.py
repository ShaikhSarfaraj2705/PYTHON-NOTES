#MATCH CASE STATEMENT
#to implement switch case like characteristics very similar to if else functionality, we use match case
# A match statement will compare a given variable's value to different shapes,also reffered to as pattern.
# he main idea is to comparing the variable with all the present patterns until its fit into one

val=int(input("enter the value: "))
match val:
    case a if val <=10:
        print("value is less than 11")
    case b if val>10 and val <=50:
        print( "value is betwwen 11-50")
    case c if val>51:
        print("value is greater than 50")