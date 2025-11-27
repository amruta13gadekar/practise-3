import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = float(sys.argv[1])
    print("User provided input value:")
else:
    temp = 25      
    print("No input given - using default value")

if temp < 15:
    status = "Cold"
elif 15 <= temp <= 30:
    status = "Normal"
else:
    status = "Hot"


print("Temperature (°C):", temp)
print("Status:", status)
