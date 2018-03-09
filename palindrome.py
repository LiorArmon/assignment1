def palindrome_tester(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def check_palindrome():
     """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
   """
for current_number in range (100000,999999):
        if palindrome_tester(str(current_number)[2:6]) == 1:
            possible_pali = current_number
            current_number = current_number+1
            if palindrome_tester(str(current_number)[1:6]) == 1:
                current_number = current_number+1
                if palindrome_tester(str(current_number)[1:5]) == 1:
                   current_number = current_number+1
                   if palindrome_tester(str(current_number)) == 1:
                       print (possible_pali)
                       
                
            