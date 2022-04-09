#as americans are accustomed to using the imperical system of measurement, if travelers go outside of the country, accurate dimensions need to be established.


#x will be set as degrees fahrenheit
#y will be degrees in  

continue_ = True
while continue_ != False:
    unconverted = float(input("Hello, please type in your degrees in fahrenheit : ")) 
    convert_value = (unconverted - 32) * 5/9
    print(f"{unconverted}° fahrenheit is {convert_value}° celsius")
    continue_ = input("Do you want to continue? (yes/no)") #if user wants to continue, program will run again
if continue_ == 'yes': 
    continue_ == True
if continue_ == 'no':
    continue_ == False
    print("Please run me again!")
    exit()
