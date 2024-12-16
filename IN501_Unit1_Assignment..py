# Values for teh temperatures in Fahrenheit

value1 = float(input("Enter First Temperature in Fahrenheit: "))
value2 = float(input("Enter Second Temperature in Fahrenheit: "))
value3 = float(input("Enter Third Temperature in Fahrenheit: "))

#Calculations

#First Temperature
startval1 = value1 - 32
step2val1 = startval1 * 5
step3val1 = step2val1 / 9

#Second Temperature
startval2 = value2 - 32
step2val2 = startval2 * 5
step3val2 = step2val2 / 9

#Third Temperature
startval3 = value3 - 32
step2val3 = startval3 * 5
step3val3 = step2val3 / 9

#Average Value in Fahrenheit
sum = value1 + value2 + value3
avf = sum / 3

#Average Value for Celsius
sumc = step3val1 + step3val2 + step3val3 
avc = sumc / 3


#printing values after calculations

print("Fahrenheit  | Celsius")
print(value1,    f"|", step3val1)
print(value2,    f"|", step3val2)
print(value3,    f"|", step3val3)
print("   ")
print('Average Temps')
print(avf, f"|", avc)
