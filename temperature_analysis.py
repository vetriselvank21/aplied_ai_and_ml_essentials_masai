# Name: Vetriselvan K
# Roll Number: IITP_AIMLTN_2602721
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
max = temperatures[0]
min = temperatures[0]
for i in temperatures :
  if i >= max :
    max = i

  if i <=min :
    min = i

print(f"Highest Temperature: {max}°C ")
print(f"Lowest Temperature: {min}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
count = 0
for i in temperatures :
  if i > 30 :
    count+=1
  else :
    continue


print(f"Hot Days (>30°C): {count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_days = 0

for day, temp in enumerate(temperatures, start=1):
    if temp >= 40:
        print(f"Hot Days before alert: {hot_days}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break
    if temp > 30:
        hot_days += 1



