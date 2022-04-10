continue_ = True
readstring_ = ""


while continue_ != False:
    unconverted = float(input("Hello, please type in your degrees in fahrenheit : ")) 
    convert_value = (unconverted - 32) * 5/9
    rounded_temp = int(convert_value)
    print(f"{unconverted}° fahrenheit is {rounded_temp}° celsius")
    readstring_ = input("Do you want to continue? (yes/no) ") #if user wants to continue, program will run again
    if readstring_ == "yes": 
        continue_ = True #one equal sign sets continue_ EQUAL to true
    if readstring_ == "no": # == is a boolean operator.
        continue_ = False
        print("Please run me again!")
        exit()
