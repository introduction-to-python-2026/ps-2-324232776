def find_max_number(num1, num2, num3):
    if   num1>= num2 >= num3:
    return num1
    elif num2>= num1>= num3:
    return num2
    else: 
    return num3  # Replace 'pass' with code

def find_mean(num1, num2, num3):
    mean= (num1 + num2 +num3)/3
   return mean  # Replace 'pass' with code

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    mean= (num1 + num2 +num3)/3
    

  STD=(((num1-mean)**2+(num2-mean)**2+(num3-mean)**2)/3)**0.5
  return mean, STD  # Replace 'pass' with code

