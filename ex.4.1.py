def main():
   weight=int(input("Enter Weight (in kg)")) 
   height=int(input("Enter Height (in cm)")) 
   height1=height/100
   BMI=weight/(height1**2)
   if BMI<18.5:
       print("Underweight")
   elif BMI>=18.5 and BMI<25.0:
       print("Normal weight")
   elif BMI>=25.5 and BMI<30.0:
       print("Increased weight")
   elif BMI>=30.0 and BMI<40:
       print("Obese")
   else:
       print("Very high obese")
main()