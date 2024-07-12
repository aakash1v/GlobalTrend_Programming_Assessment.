
def divide(num1,num2):
    try:
        return num1/num2
    except Exception as e:
        return "Error : we cannot divide any number by 0"
    


print(divide(10,5))
print(divide(10,0))
print(divide(10,10))
print(divide(10,100))