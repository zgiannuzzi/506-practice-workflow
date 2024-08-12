import pandas as pd 
import numpy as np 


numvar = 5 
stringvar = 'hello'
listvar = [1,2,'word','random']
dictvar = {
  "brad": 48,
  "Zach": 26,
  "Anthony": 18,
  "Char" : 24
}

#Calculates Oral dose
def number_is_larger(num1,num2):
    if(num1 > num2):
      return num1
    else:
      return num2 

    

larger_num = number_is_larger(20,40)


print('The larger number is',larger_num)
print('numvar =',numvar)
print('stringvar =',stringvar)
print('listvar =',listvar)
print('dictvar =',dictvar)