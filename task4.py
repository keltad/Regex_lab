import re # 

email = "student123@gmail.com" # 
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" # О

if re.match(pattern, email): #
	print("Email коректний") #  
else: #
	print("Email некоректний") #
