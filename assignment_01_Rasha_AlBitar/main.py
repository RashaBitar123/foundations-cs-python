# Write a function that takes an integer from the user and calculates its factorial.

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n - 1)
n = input("Enter a number to calculate its factorial: ")
print(n+"! =",factorial(int(n))) 

# Write a function that takes an integer as an input from the user and finds all its divisors and stores them in a list.

def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
num = input("Enter a number to find its divisors: ")
print("Divisors of "+num+" are",divisors(int(num)))

# Write a function called reverseString that takes a string as input from the user and returns the string reversed.

def reverseString(s):
    return s[::-1]
input_string = input("Enter a string to  reverse: ")  
print("Reversed String: ",reverseString(input_string))

# Write a function that takes a list of integers as input from the user and returns a new list containing only the even numbers from the original list, in the same order.

def evenNumbers(n):
    evenNumbers = []
    for i in n:
        if i % 2 == 0:
            evenNumbers.append(i)
    return evenNumbers
  
user_input= input("Enter a list of integers separated by spaces: ")
input_list = [int(item) for item in user_input.split()]
print("Input List:", input_list)
print("Even Numbers:", evenNumbers(input_list))

# Write a function that takes a string as input and checks whether it meets the requirements for a strong password.A strong password should be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character (a special character is either #, ?, !, $).

def checkPassword(password):
  if (len(password) >= 8) and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in "#?!$" for c in password):
      return "Strong password"
  else:
      return "Weak password"

input_pass = input("Enter a password: ")  
print(checkPassword(input_pass))


# Write a function that takes a string as input andchecks whether it is a valid IPv4 address. A valid IPv4 address is a string of four numbers separated by periods, where each number is between 0 and 255. 

def checkIpV4(ip):
  octets = ip.split('.')
  if len(octets) != 4:
    return "Invalid IPv4 address"

  for octet in octets:
    if not octet.isdigit():
      return "Invalid IPv4 address" 
      value = int(octet)
      if value < 0 or value > 255:
        return "Invalid IPv4 address" 
      if len(octet) > 1 and octet[0] == '0':
        return "Invalid IPv4 address"
  return "Valid IPv4 address"

ip = input("Enter an IPv4 address: ")
print(checkIpV4(ip))


# Write a function that takes a list of integers as input and calculates their descriptive statistics: mean,mode,median,range,variance,standard deviation.

def calculateStatistics():
  numbers = input("Enter a list of integers separated by spaces: ").split()
  numbers = [int(num) for num in numbers]
  print("Input List:", numbers)

  # Mean
  mean = sum(numbers) / len(numbers)

  # Median
  n = len(numbers)
  numbers = sorted(numbers)
  if n % 2 == 0:
      median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
  else:
      median = numbers[n // 2]

  # Mode
  counts = {}
  for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
  max_count = max(counts.values())
  mode = [key for key, value in counts.items() if value == max_count]
  if max_count == 1:
    mode = "No mode"
 


  # Range
  data_range = max(numbers) - min(numbers)

  # Variance
  variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

  # Standard Deviation
  standard_deviation = variance ** 0.5

  
  print("Mean:", mean)
  print("Median:", median)
  print("Mode:", mode)
  print("Range:", data_range)
  print("Variance:", variance)
  print("Standard Deviation:", standard_deviation)

calculateStatistics()



 
