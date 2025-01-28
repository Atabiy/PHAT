gender = input("Enter your gender M - Male, F - Female")
age = int(input("Enter your age: "))
height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if gender == "M":
    g_koaf = 0.9
else:
    g_koaf = 0.085


if age < 30:
    a_koaf = 0.89
elif age > 50:
    a_koaf = 1.06
else:
    a_koaf = 1
 
normal_weight = ((height - 100) * g_koaf) * a_koaf

diff = ((weight - normal_weight)**2)**0.5

print(f"Your current weight is {weight}, your perfect weight is {normal_weight}. Difference is {diff}")
