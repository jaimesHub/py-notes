height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in lbs: "))

bmi_score = (weight * 703) / (height * height)
print(bmi_score)

if bmi_score < 16.0:
    print(f"your BMI of {round(bmi_score, 2)} makes you Severely Underweight")
elif bmi_score >= 16.0 and bmi_score <= 18.4:
    print(f"your BMI of {round(bmi_score, 2)} makes you Underweight")
elif bmi_score >= 18.5 and bmi_score <= 24.9:
    print(f"your BMI of {round(bmi_score, 2)} makes you Normal")
elif bmi_score >= 25.0 and bmi_score <= 29.9:
    print(f"your BMI of {round(bmi_score, 2)} makes you Overweight")
elif bmi_score >= 30.0 and bmi_score <= 34.9:
    print(f"your BMI of {round(bmi_score, 2)} makes you Moderately Obese")
elif bmi_score >= 35.0 and bmi_score <= 39.9:
    print(f"your BMI of {round(bmi_score, 2)} makes you Severely Obese")
else:
    print(f"your BMI of {round(bmi_score, 2)} makes you Morbidly Obese")