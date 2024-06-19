
def monthloop():
  global months
  months = int(input("\nEnter the number of months:"))

def boybmi(age,BMI,months):
  global status
  status="Blank"
  if age == 2 and months == 0:
    if BMI < 14.7:
      status = ("Underweight")
    elif BMI >= 14.7 and BMI < 18.2:
      status = ("Healthy Weight")
    elif BMI >= 18.2 and BMI < 19.2:
      status = ("Overweight")
    elif BMI >= 19.2:
      status = ("Obesity")
  if age == 2 and months == 6:
    if BMI < 14.5:
      status = ("Underweight")
    elif BMI >= 14.5 and BMI < 17.8:
      status = ("Healthy Weight")
    elif BMI >= 17.8 and BMI < 18.7:
      status = ("Overweight")
    elif BMI >= 18.7:
      status = ("Obesity")
  if age == 3 and months == 0:
    if BMI < 14.3:
      status = ("Underweight")
    elif BMI >= 14.3 and BMI < 17.4 :
      status = ("Healthy Weight")
    elif BMI >= 17.4 and BMI < 18.3:
      status = ("Overweight")
    elif BMI >= 18.3:
      status = ("Obesity")
  if age == 3 and months == 6:
      if BMI < 14.2:
        status = ("Underweight")
      elif BMI >= 14.2 and BMI < 17.1:
        status = ("Healthy Weight")
      elif BMI >= 17.1 and BMI < 17.9:
        status = ("Overweight")
      elif BMI >= 17.9:
        status = ("Obesity")
  if age == 4 and months == 0:
      if BMI < 14:
        status = ("Underweight")
      elif BMI >= 14 and BMI < 16.9:
        status = ("Healthy Weight")
      elif BMI >= 16.9 and BMI < 17.8:
        status = ("Overweight")
      elif BMI >= 17.8:
        status = ("Obesity")
  if age == 4 and months == 6:
      if BMI < 13.9:
        status = ("Underweight")
      elif BMI >= 13.9 and BMI < 16.9:
        status = ("Healthy Weight")
      elif BMI >= 16.9 and BMI < 17.8:
        status = ("Overweight")
      elif BMI >= 17.8:
        status = ("Obesity")
  if age == 5 and months == 0:
      if BMI < 13.8:
        status = ("Underweight")
      elif BMI >= 13.8 and BMI < 16.9:
        status = ("Healthy Weight")
      elif BMI >= 16.9 and BMI < 17.9:
        status = ("Overweight")
      elif BMI >= 17.9:
        status = ("Obesity")
  if age == 5 and months == 6:
      if BMI < 13.7:
        status = ("Underweight")
      elif BMI >= 13.7 and BMI < 16.9:
        status = ("Healthy Weight")
      elif BMI >= 16.9 and BMI < 18.1:
        status = ("Overweight")
      elif BMI >= 18.1:
        status = ("Obesity")
  if age == 6 and months == 0:
      if BMI < 13.7:
        status = ("Underweight")
      elif BMI >= 13.7 and BMI < 17:
        status = ("Healthy Weight")
      elif BMI >= 17 and BMI < 18.4:
        status = ("Overweight")
      elif BMI >= 18.4:
        status = ("Obesity")
  if age == 6 and months == 6:
      if BMI < 13.7:
        status = ("Underweight")
      elif BMI >= 13.7 and BMI < 17.2:
        status = ("Healthy Weight")
      elif BMI >= 17.2 and BMI < 18.8:
        status = ("Overweight")
      elif BMI >= 18.8:
        status = ("Obesity")
  if age == 7 and months == 0:
      if BMI < 13.7:
        status = ("Underweight")
      elif BMI >= 13.7 and BMI < 17.4:
        status = ("Healthy Weight")
      elif BMI >= 17.4 and BMI < 19.1:
        status = ("Overweight")
      elif BMI >= 19.1:
        status = ("Obesity")
  if age == 7 and months == 6:
      if BMI < 13.7:
        status = ("Underweight")
      elif BMI >= 13.7 and BMI < 17.7:
        status = ("Healthy Weight")
      elif BMI >= 17.7 and BMI < 19.6:
        status = ("Overweight")
      elif BMI >= 19.6:
        status = ("Obesity")
  if age == 8 and months == 0:
      if BMI < 13.8:
        status = ("Underweight")
      elif BMI >= 13.8 and BMI < 17.9:
        status = ("Healthy Weight")
      elif BMI >= 17.9 and BMI < 20:
        status = ("Overweight")
      elif BMI >= 20:
        status = ("Obesity")
  if age == 8 and months == 6:
      if BMI < 13.8:
        status = ("Underweight")
      elif BMI >= 13.8 and BMI < 18.3:
        status = ("Healthy Weight")
      elif BMI >= 18.3 and BMI < 20.5:
        status = ("Overweight")
      elif BMI >= 20.5:
        status = ("Obesity")
  if age == 9 and months == 0:
      if BMI < 13.9:
        status = ("Underweight")
      elif BMI >= 13.9 and BMI < 18.6:
        status = ("Healthy Weight")
      elif BMI >= 18.6 and BMI < 21:
        status = ("Overweight")
      elif BMI >= 21:
        status = ("Obesity")
  if age == 9 and months == 6:
      if BMI < 14:
        status = ("Underweight")
      elif BMI >= 14 and BMI < 19:
        status = ("Healthy Weight")
      elif BMI >= 19 and BMI < 21.5:
        status = ("Overweight")
      elif BMI >= 21.5:
        status = ("Obesity")
  if age == 10 and months == 0:
      if BMI < 14.2:
        status = ("Underweight")
      elif BMI >= 14.2 and BMI < 19.4:
        status = ("Healthy Weight")
      elif BMI >= 19.4 and BMI < 22.1:
        status = ("Overweight")
      elif BMI >= 22.1:
        status = ("Obesity")
  if age == 10 and months == 6:
      if BMI < 14.4:
        status = ("Underweight")
      elif BMI >= 14.4 and BMI < 19.8:
        status = ("Healthy Weight")
      elif BMI >= 19.8 and BMI < 22.7:
        status = ("Overweight")
      elif BMI >= 22.7:
        status = ("Obesity")
  if age == 11 and months == 0:
      if BMI < 14.6:
        status = ("Underweight")
      elif BMI >= 14.6 and BMI < 20.2:
        status = ("Healthy Weight")
      elif BMI >= 20.2 and BMI < 23.2:
        status = ("Overweight")
      elif BMI >= 23.2:
        status = ("Obesity")
  if age == 11 and months == 6:
      if BMI < 14.8:
        status = ("Underweight")
      elif BMI >= 14.8 and BMI < 20.6:
        status = ("Healthy Weight")
      elif BMI >= 20.6 and BMI < 23.7:
        status = ("Overweight")
      elif BMI >= 23.7:
        status = ("Obesity")
  if age == 12 and months == 0:
      if BMI < 15:
        status = ("Underweight")
      elif BMI >= 15 and BMI < 21:
        status = ("Healthy Weight")
      elif BMI >= 21 and BMI < 24.2:
        status = ("Overweight")
      elif BMI >= 24.2:
        status = ("Obesity")
  if age == 12 and months == 6:
      if BMI < 15.2:
        status = ("Underweight")
      elif BMI >= 15.2 and BMI < 21.5:
        status = ("Healthy Weight")
      elif BMI >= 21.5 and BMI < 24.7:
        status = ("Overweight")
      elif BMI >= 24.7:
        status = ("Obesity")
  if age == 13 and months == 0:
      if BMI < 15.5:
        status = ("Underweight")
      elif BMI >= 15.5 and BMI < 21.8:
        status = ("Healthy Weight")
      elif BMI >= 21.8 and BMI < 25.2:
        status = ("Overweight")
      elif BMI >= 25.2:
        status = ("Obesity")
  if age == 13 and months == 6:
      if BMI < 15.7:
        status = ("Underweight")
      elif BMI >= 15.7 and BMI < 22.3:
        status = ("Healthy Weight")
      elif BMI >= 22.3 and BMI < 25.6:
        status = ("Overweight")
      elif BMI >= 25.6:
        status = ("Obesity")
  if age == 14 and months == 0:
      if BMI < 16:
        status = ("Underweight")
      elif BMI >= 16 and BMI < 22.7:
        status = ("Healthy Weight")
      elif BMI >= 22.7 and BMI < 26:
        status = ("Overweight")
      elif BMI >= 26:
        status = ("Obesity")
  if age == 14 and months == 6:
      if BMI < 16.2:
        status = ("Underweight")
      elif BMI >= 16.2 and BMI < 23.1:
        status = ("Healthy Weight")
      elif BMI >= 23.1and BMI < 26.4:
        status = ("Overweight")
      elif BMI >= 26.4:
        status = ("Obesity")
  if age == 15 and months == 0:
      if BMI < 16.5:
        status = ("Underweight")
      elif BMI >= 16.5 and BMI < 23.4:
        status = ("Healthy Weight")
      elif BMI >= 23.4 and BMI < 26.8:
        status = ("Overweight")
      elif BMI >= 26.8:
        status = ("Obesity")
  if age == 15 and months == 6:
      if BMI < 16.8:
        status = ("Underweight")
      elif BMI >= 16.8 and BMI < 23.8:
        status = ("Healthy Weight")
      elif BMI >= 23.8 and BMI < 27.2:
        status = ("Overweight")
      elif BMI >= 27.2:
        status = ("Obesity")
  if age == 16 and months == 0:
      if BMI < 17.1:
        status = ("Underweight")
      elif BMI >= 17.1 and BMI < 24.2:
        status = ("Healthy Weight")
      elif BMI >= 24.2 and BMI < 27.6:
        status = ("Overweight")
      elif BMI >= 27.6:
        status = ("Obesity")
  if age == 16 and months == 6:
      if BMI < 17.4:
        status = ("Underweight")
      elif BMI >= 17.4 and BMI < 24.6:
        status = ("Healthy Weight")
      elif BMI >= 24.6and BMI < 27.9:
        status = ("Overweight")
      elif BMI >= 27.9:
        status = ("Obesity")
  if age == 17 and months == 0:
      if BMI < 17.7:
        status = ("Underweight")
      elif BMI >= 17.7 and BMI < 25:
        status = ("Healthy Weight")
      elif BMI >= 25 and BMI < 28.3:
        status = ("Overweight")
      elif BMI >= 28.3:
        status = ("Obesity")
  if age == 17 and months == 6:
      if BMI < 18:
        status = ("Underweight")
      elif BMI >= 18 and BMI < 25.3:
        status = ("Healthy Weight")
      elif BMI >= 25.3 and BMI < 28.6:
        status = ("Overweight")
      elif BMI >= 28.6:
        status = ("Obesity")
  if age == 18 and months == 0:
      if BMI < 18.3:
        status = ("Underweight")
      elif BMI >= 18.3 and BMI < 25.7:
        status = ("Healthy Weight")
      elif BMI >= 25.7 and BMI < 29:
        status = ("Overweight")
      elif BMI >= 29:
        status = ("Obesity")
  if age == 18 and months == 6:
      if BMI < 18.5:
        status = ("Underweight")
      elif BMI >= 18.5 and BMI < 26:
        status = ("Healthy Weight")
      elif BMI >= 26 and BMI < 29.3:
        status = ("Overweight")
      elif BMI >= 29.3:
        status = ("Obesity")
  if age == 19 and months == 0:
      if BMI < 18.7:
        status = ("Underweight")
      elif BMI >= 18.7 and BMI < 26.4:
        status = ("Healthy Weight")
      elif BMI >= 26.4and BMI < 29.8:
        status = ("Overweight")
      elif BMI >= 29.8:
        status = ("Obesity")
  if age == 19and months == 6:
      if BMI < 18.9:
        status = ("Underweight")
      elif BMI >= 18.9 and BMI < 26.7:
        status = ("Healthy Weight")
      elif BMI >= 26.7 and BMI < 30.1:
        status = ("Overweight")
      elif BMI >= 30.1:
        status = ("Obesity")
  return status

    
def girlbmi(age, BMI, months):
  global status
  status = "Blank"
  if age == 2 and months == 0:
    if BMI < 14.5:
      status = ("Underweight")
    elif BMI >= 14.5 and BMI < 18.5:
      status = ("Healthy Weight")
    elif BMI >= 18.5 and BMI < 19:
      status = ("Overweight")
    elif BMI >= 19:
      status = ("Obesity")
  if age == 2 and months == 6:
    if BMI < 14.2:
      status = ("Underweight")
    elif BMI >= 14.2 and BMI < 17.5:
      status = ("Healthy Weight")
    elif BMI >= 17.5 and BMI < 18.6:
      status = ("Overweight")
    elif BMI >= 18.6:
      status = ("Obesity")
  if age == 3 and months == 0:
    if BMI < 14:
      status = ("Underweight")
    elif BMI >= 14 and BMI < 17.3:
      status = ("Healthy Weight")
    elif BMI >= 17.3 and BMI < 18.3:
      status = ("Overweight")
    elif BMI >= 18.3:
      status = ("Obesity")
  if age == 3 and months == 6:
    if BMI < 13.9:
      status = ("Underweight")
    elif BMI >= 13.9 and BMI < 17:
      status = ("Healthy Weight")
    elif BMI >= 17 and BMI < 18.1:
      status = ("Overweight")
    elif BMI >= 18.1:
      status = ("Obesity")
  if age == 4 and months == 0:
    if BMI < 13.8:
      status = ("Underweight")
    elif BMI >= 13.8 and BMI < 16.8:
      status = ("Healthy Weight")
    elif BMI >= 16.8 and BMI < 18:
      status = ("Overweight")
    elif BMI >= 18:
      status = ("Obesity")
  if age == 4 and months == 6:
    if BMI < 13.6:
      status = ("Underweight")
    elif BMI >= 13.6 and BMI < 16.8:
      status = ("Healthy Weight")
    elif BMI >= 16.8 and BMI < 18.1:
      status = ("Overweight")
    elif BMI >= 18.1:
      status = ("Obesity")
  if age == 5 and months == 0:
    if BMI < 13.5:
      status = ("Underweight")
    elif BMI >= 13.5 and BMI < 16.8:
      status = ("Healthy Weight")
    elif BMI >= 16.8 and BMI < 18.3:
      status = ("Overweight")
    elif BMI >= 18.3:
      status = ("Obesity")
  if age == 5 and months == 6:
    if BMI < 13.5:
      status = ("Underweight")
    elif BMI >= 13.5 and BMI < 17:
      status = ("Healthy Weight")
    elif BMI >= 17 and BMI < 18.5:
      status = ("Overweight")
    elif BMI >= 18.5:
      status = ("Obesity")
  if age == 6 and months == 0:
    if BMI < 13.4:
      status = ("Underweight")
    elif BMI >= 13.4 and BMI < 17.1:
      status = ("Healthy Weight")
    elif BMI >= 17.2 and BMI < 18.8:
      status = ("Overweight")
    elif BMI >= 18.8:
      status = ("Obesity")
  if age == 6 and months == 6:
    if BMI < 13.4:
      status = ("Underweight")
    elif BMI >= 13.4 and BMI < 17.3:
      status = ("Healthy Weight")
    elif BMI >= 17.3 and BMI < 19.3:
      status = ("Overweight")
    elif BMI >= 19.3:
      status = ("Obesity")
  if age == 7 and months == 0:
    if BMI < 13.4:
      status = ("Underweight")
    elif BMI >= 13.4 and BMI < 17.6:
      status = ("Healthy Weight")
    elif BMI >= 17.6 and BMI < 19.7:
      status = ("Overweight")
    elif BMI >= 19.7:
      status = ("Obesity")
  if age == 7 and months == 6:
    if BMI < 14.5:
      status = ("Underweight")
    elif BMI >= 14.5 and BMI < 18.5:
      status = ("Healthy Weight")
    elif BMI >= 18.5 and BMI < 19:
      status = ("Overweight")
    elif BMI >= 19:
      status = ("Obesity")
  if age == 8:
    if BMI < 13.5:
      status = ("Underweight")
    elif BMI >= 13.5 and BMI < 18.3:
      status = ("Healthy Weight")
    elif BMI >= 18.3 and BMI < 20.7:
      status = ("Overweight")
    elif BMI >= 20.7:
      status = ("Obesity")
  if age == 8 and months == 6:
    if BMI < 13.6:
      status = ("Underweight")
    elif BMI >= 13.6 and BMI < 18.8:
      status = ("Healthy Weight")
    elif BMI >= 18.8 and BMI < 21.3:
      status = ("Overweight")
    elif BMI >= 21.3:
      status = ("Obesity")
  if age == 9 and months == 0:
    if BMI < 13.8:
      status = ("Underweight")
    elif BMI >= 13.8 and BMI < 19:
      status = ("Healthy Weight")
    elif BMI >= 19 and BMI < 21.8:
      status = ("Overweight")
    elif BMI >= 21.8:
      status = ("Obesity")
  if age == 9 and months == 6:
    if BMI < 13.9:
      status = ("Underweight")
    elif BMI >= 13.9 and BMI < 19.5:
      status = ("Healthy Weight")
    elif BMI >= 19.5 and BMI < 22.4:
      status = ("Overweight")
    elif BMI >= 22.4:
      status = ("Obesity")
  if age == 10 and months == 0:
    if BMI < 14:
      status = ("Underweight")
    elif BMI >= 14 and BMI < 20:
      status = ("Healthy Weight")
    elif BMI >= 20 and BMI < 23:
      status = ("Overweight")
    elif BMI >= 23:
      status = ("Obesity")
  if age == 10 and months == 6:
    if BMI < 14.2:
      status = ("Underweight")
    elif BMI >= 14.2 and BMI < 20.4:
      status = ("Healthy Weight")
    elif BMI >= 20.4 and BMI < 23.5:
      status = ("Overweight")
    elif BMI >= 23.5:
      status = ("Obesity")
  if age == 11 and months == 0:
    if BMI < 14.4:
      status = ("Underweight")
    elif BMI >= 14.4 and BMI < 20.8:
      status = ("Healthy Weight")
    elif BMI >= 20.8 and BMI < 24:
      status = ("Overweight")
    elif BMI >= 24:
      status = ("Obesity")
  if age == 11 and months == 6:
    if BMI < 14.6:
      status = ("Underweight")
    elif BMI >= 14.6 and BMI < 21.3:
      status = ("Healthy Weight")
    elif BMI >= 21.3 and BMI < 24.7:
      status = ("Overweight")
    elif BMI >= 24.7:
      status = ("Obesity")
  if age == 12 and months == 0:
    if BMI < 14.8:
      status = ("Underweight")
    elif BMI >= 14.8 and BMI < 21.7:
      status = ("Healthy Weight")
    elif BMI >= 21.7 and BMI < 25.3:
      status = ("Overweight")
    elif BMI >= 25.3:
      status = ("Obesity")
  if age == 12 and months == 6:
    if BMI < 15.1:
      status = ("Underweight")
    elif BMI >= 15.1 and BMI < 22.2:
      status = ("Healthy Weight")
    elif BMI >= 22.2 and BMI < 25.8:
      status = ("Overweight")
    elif BMI >= 25.8:
      status = ("Obesity")
  if age == 13 and months == 0:
    if BMI < 15.3:
      status = ("Underweight")
    elif BMI >= 15.3 and BMI < 22.5:
      status = ("Healthy Weight")
    elif BMI >= 22.5 and BMI < 26.3:
      status = ("Overweight")
    elif BMI >= 26.3:
      status = ("Obesity")
  if age == 13 and months == 6:
    if BMI < 15.5:
      status = ("Underweight")
    elif BMI >= 15.5 and BMI < 23:
      status = ("Healthy Weight")
    elif BMI >= 23 and BMI < 26.8:
      status = ("Overweight")
    elif BMI >= 26.8:
      status = ("Obesity")
  if age == 14 and months == 0:
    if BMI < 15.8:
      status = ("Underweight")
    elif BMI >= 15.8 and BMI < 23.3:
      status = ("Healthy Weight")
    elif BMI >= 23.3 and BMI < 27.3:
      status = ("Overweight")
    elif BMI >= 27.3:
      status = ("Obesity")
  if age == 14 and months == 6:
    if BMI < 16:
      status = ("Underweight")
    elif BMI >= 16 and BMI < 23.7:
      status = ("Healthy Weight")
    elif BMI >= 23.7 and BMI < 27.7:
      status = ("Overweight")
    elif BMI >= 27.7:
      status = ("Obesity")
  if age == 15 and months == 0:
    if BMI < 16.3:
      status = ("Underweight")
    elif BMI >= 16.3 and BMI < 24:
      status = ("Healthy Weight")
    elif BMI >= 24 and BMI < 28.1:
      status = ("Overweight")
    elif BMI >= 28.1:
      status = ("Obesity")
  if age == 15 and months == 6:
    if BMI < 16.5:
      status = ("Underweight")
    elif BMI >= 16.5 and BMI < 24.4:
      status = ("Healthy Weight")
    elif BMI >= 24.4 and BMI < 28.5:
      status = ("Overweight")
    elif BMI >= 28.5:
      status = ("Obesity")
  if age == 16 and months == 0:
    if BMI < 16.8:
      status = ("Underweight")
    elif BMI >= 16.8 and BMI < 24.7:
      status = ("Healthy Weight")
    elif BMI >= 24.7 and BMI < 28.9:
      status = ("Overweight")
    elif BMI >= 28.9:
      status = ("Obesity")
  if age == 16 and months == 6:
    if BMI < 17:
      status = ("Underweight")
    elif BMI >= 17 and BMI < 24.9:
      status = ("Healthy Weight")
    elif BMI >= 24.9 and BMI < 29.3:
      status = ("Overweight")
    elif BMI >= 29.3:
      status = ("Obesity")
  if age == 17 and months == 0:
    if BMI < 17.3:
      status = ("Underweight")
    elif BMI >= 17.3 and BMI < 25.3:
      status = ("Healthy Weight")
    elif BMI >= 25.3 and BMI < 29.7:
      status = ("Overweight")
    elif BMI >= 29.7:
      status = ("Obesity")
  if age == 17 and months == 6:
    if BMI < 17.4:
      status = ("Underweight")
    elif BMI >= 17.4 and BMI < 25.5:
      status = ("Healthy Weight")
    elif BMI >= 25.5 and BMI < 30:
      status = ("Overweight")
    elif BMI >= 30:
      status = ("Obesity")
  if age == 18 and months == 0:
    if BMI < 17.5:
      status = ("Underweight")
    elif BMI >= 17.5 and BMI < 25.7:
      status = ("Healthy Weight")
    elif BMI >= 25.7 and BMI < 30.3:
      status = ("Overweight")
    elif BMI >= 30.3:
      status = ("Obesity")
  if age == 18 and months == 6:
    if BMI < 17.7:
      status = ("Underweight")
    elif BMI >= 17.7 and BMI < 25.9:
      status = ("Healthy Weight")
    elif BMI >= 25.9 and BMI < 30.7:
      status = ("Overweight")
    elif BMI >= 30.7:
      status = ("Obesity")
  if age == 19 and months == 0:
    if BMI < 17.8:
      status = ("Underweight")
    elif BMI >= 17.8 and BMI < 26.1:
      status = ("Healthy Weight")
    elif BMI >= 26.1 and BMI < 31:
      status = ("Overweight")
    elif BMI >= 31:
      status = ("Obesity")
  if age == 19 and months == 6:
    if BMI < 17.8:
      status = ("Underweight")
    elif BMI >= 17.8 and BMI < 26.3:
      status = ("Healthy Weight")
    elif BMI >= 26.3 and BMI < 31.4:
      status = ("Overweight")
    elif BMI >= 31.4:
      status = ("Obesity")
    
    
  
  


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
months= "N/A"

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
  sex = input("Enter your sex (Female or Male) :  ").lower()
  while True:
    if sex!="female" or "f" or "male" or "m":
      print("Invalid Input- Try Again")
      sex = input("Enter your sex (Female or Male) :  ").lower()
      break
      
  if sex == "female".lower() or sex=="f".lower():
    girlbmi(age, BMI, months)
  if sex== "male".lower() or "m".lower():
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
