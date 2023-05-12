#1.Write a function that takes an unknown number of arguments and returns their sum.
def addition(*nums):
    return sum(nums)
print(addition(4,5,6,7,8,4))    
    


#2.Write a function that takes two arguments, the first being a string and the second 
#being an unknown number of integers. The function should return a new string where the 
#integers have been added to the original string.
def add_num_string(names,*nums):
    result=names
    for num in nums:
        result+=str(num)
        return result
names="The number of mangoes are" 
result=add_num_string(names,30) 
print(result)      
 
#3.Write a function that takes an unknown number of keyword arguments and returns a 
#dictionary where the keys are the argument names and the values are the argument values.
def unknown_number(**kwargs):
    return kwargs
result=unknown_number(name="Ann",age=23) 
print(result)   

#4.Write a function that takes a function and an unknown number of arguments, and returns 
#the result of calling the function with the arguments.
def call_function(fun,*args):
    return fun(args)



#5.Write a function that takes a list of integers and an unknown number of keyword arguments.
# The function should return a new list where each integer in the original list has been 
#multiplied by the value of the corresponding keyword argument.
def multiplied(list_nums,**kwargs):


#6Write a function that takes a list of integers and an unknown number of additional
# integers as arguments. The function should return the index of the first occurrence of 
#the sum of the list and the additional integers

def find_first_index(list_nums,*nums):
    total=sum(list_nums)+sum(nums)
    for i,num in list_nums:
        if num ==total
        return i
#7.Write a function that takes an unknown number of keyword arguments, each with a string 
#value. The function should concatenate all the strings and return the resulting string
def concatenate_all_strings(**kwargs):
    concatenate=''
    for arg in kwargs