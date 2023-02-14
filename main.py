# prompt user for file name
# prompt user for their first name
# prompt user for street address name
# prompt user for their phone number
# write the first name, street name, phone number to a comma separated line in a file
# once the data has been written to the file your program should read the file and display the contents

file_name = input("What do you want to name your file? ")
user_fname = input("What is your first name? ")
user_street = input("What is your street address? ")
user_phone = input("What is you phone number? ")

# file_name = 'test.txt'
# user_fname = 'Charles'
# user_street = 'softwind loop'
# user_phone = '1234567'

input_data = ','.join([user_fname, user_street, user_phone])

print(input_data)

with open(file_name, 'w') as file_handle:
  file_handle.write(input_data)


#SOURCES
#https://www.w3schools.com/python/ref_string_join.asp
#Matthes, E. (2019). Chapter 10: Files and Exceptions. In Python crash course, 2nd Edition. essay, No Starch. 