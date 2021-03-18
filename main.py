#Write your code below this line 👇
def prime_checker(number):
	prime = True
	for i in range (2, number):
		if number % i == 0:
			prime = False
	if prime:
		print("Простое число!")
	else:
		print("Число не ПРОСТОЕ!")			
	




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



