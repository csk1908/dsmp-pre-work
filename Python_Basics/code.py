# --------------
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

#Concatenate the 'class_1' and 'class_2'
new_class = class_1 + class_2

#Add new element 
new_class.append('Peter Warden')

#Remove Carla Gentry
new_class.remove('Carla Gentry')
print(new_class)





# --------------
# Code starts here

#Creat Dictionary course
courses ={"Math":65, "English":70, "History":80, "French":70, "Science":60}
print(courses)

#Add all the marks
total = sum(courses.values())
print(total)

#Calculate the 'percentage' 
percentage = (total/500)*100
print(percentage)

# Code ends here


# --------------
# Code starts here
#Create a dictionary named 'mathematics' 
mathematics = {"Geoffrey Hinton":78, "Andrew Ng":95, "Sebastian Raschka":65, "Yoshua Benjio":50, "Hilary Mason":70, "Corinna Cortes":66, "Peter Warden":75}

#Find out the student with the highest marks
topper = max(mathematics,key = mathematics.get)
print (topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
# Code starts here
#Split the 'topper' using the "split()" function and store the results in 'first_name' and 'last_name'.
first_name = topper.split()[0] 
last_name = topper.split()[1]
print(first_name)
print(last_name)

#Display the full name concatenating + the strings 'last_name' and 'first_name' strings. 
#Add a whitespace character between them.
full_name = "{} {}".format(last_name,first_name)
print(full_name)

#Convert'full_name'string to uppercase, and store it to the 'certificate_name' variable.
certificate_name = full_name.upper()
print(certificate_name)



# Code ends here


