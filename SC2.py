#Name:alaya
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:

Height=int(input("height in feet and inches"))
Weight=int(input("weight in pounds "))
bmi= Weight/ (Height**2)*703
if bmi <18.5:
    print("you are underweight")
elif 18.5 <= bmi <= 24.9:
    print("you are normal")
elif 25 <= bmi <= 29.9:
    print("you are overweight")
else :
    print("you are obese")
