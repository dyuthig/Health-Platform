import json

with open("boybmi.json") as bmifile:
  global boybmidata
  boybmidata = json.loads(bmifile.read())

with open("girlbmi.json") as bmifile:
  global girlbmidata
  girlbmidata= json.loads(bmifile.read())


def monthloop():
  global months
  months = int(input("\nEnter the number of months:"))


def boybmi(age, BMI, months):
  global status
  status = "Blank"
  bmirange = boybmidata[str(age)][0 if months == 0 else 1]
  if BMI < bmirange[0]:
    status = ("Underweight")
  if BMI >= bmirange[0] and BMI < bmirange[1]:
    status = ("Healthy Weight")
  if BMI >= bmirange[1] and BMI < bmirange[2]:
    status = ("Overweight")
  if BMI >= bmirange[2]:
    status = ("Obesity")
  return status


def girlbmi(age, BMI, months):
  global status
  status = "Blank"
  bmirange = girlbmidata[str(age)][0 if months == 0 else 1]
  if BMI < bmirange[0]:
    status = ("Underweight")
  if BMI >= bmirange[0] and BMI < bmirange[1]:
    status = ("Healthy Weight")
  if BMI >= bmirange[1] and BMI < bmirange[2]:
    status = ("Overweight")
  if BMI >= bmirange[2]:
    status = ("Obesity")
  return status


  


print("BMI Calculator- Please do not type any units\n")
global age
global BMI
age = int(input("Enter your age in years: "))
validmonths = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

totalweight = float(input("Input your weight in pounds: "))

print("\nHeight:")
heightfeet = float(input("\nFeet: "))
heightinches = float(input("Inches: "))
decimalheight = float(input("Decimal of Inch:"))

totalheight = heightfeet * 12
totalheight = totalheight + heightinches + decimalheight
BMI = totalweight / (totalheight**2) * 703
BMI = round(BMI, 1)
months = "N/A"

if age < 20:
  monthloop()
  while True:
    if months not in validmonths:
      print("Invalid Input Try Again: ")
      monthloop()
    else:
      break
  if months == 0 or months == 1 or months == 2 or months == 3:
    months = 0
  if months == 4 or months == 5 or months == 6 or months == 7 or months == 8:
    months = 6
  else:
    age = age + 1
    months = 0
  sex = input("Enter your sex (F or M) :  ").lower()
  sexlist=["female", "f", "male", "m"]
  
  while True:
    if sex not in sexlist:
      print("Invalid Input-Try Again")
      sex = input("Enter your sex (F or M) :  ").lower()
    else:
      break   
  if sex == "female".lower() or sex == "f".lower():
    girlbmi(age, BMI, months)
  if sex == "male".lower() or sex== "m".lower():
    boybmi(age, BMI, months)
elif age >= 20:
  if BMI < 18.5:
    status = ("Underweight")
  elif BMI >= 18.5 and BMI <= 24.9:
    status = ("Healthy Weight")
  elif BMI >= 25.0 and BMI <= 29.9:
    status = ("Overweight")
  elif BMI >= 30.0:
    status = ("Obesity")

print("\nYour Result Is: ")
print(f"\nHeight: {totalheight} inches\n ")
print(f"Weight: {totalweight} lbs\n")
print(
    f"Your BMI is {BMI} which indicates that you are currently in the {status} category"
)
