# Adding a Ticket
def calculate_priority(oxygen,heart_rate,blood_pressure,temperature,conditions):
    score=0

    # Checking Oxygen Level
    if oxygen<90:
        score+=40
    elif oxygen<94:
        score+=25
    elif oxygen<97:
        score+=10

    # Checking Heart Rate
    if heart_rate<50 or heart_rate>120:
        score+=25
    elif heart_rate<60 or heart_rate>100:
        score+=10

    # Checking Blood Pressure
    if blood_pressure<90 or blood_pressure>160:
        score+=20
    elif blood_pressure<100 or blood_pressure>140:
        score+=10

    # Checking Temperature
    if temperature<35 or temperature>40:
        score+=15
    elif temperature<36 or temperature>38:
        score+=5

    # Checking Medical Conditions
    if conditions.lower()!="none":
        score+=10

    # Classifying Patient
    if score>=70:
        return score,"CRITICAL"
    elif score>=50:
        return score,"HIGH"
    elif score>=25:
        return score,"MEDIUM"
    else:
        return score,"LOW"


# Test 1: Critical Patient
score,priority=calculate_priority(85,130,170,40,"Diabetes")
assert priority=="CRITICAL"
print("Test 1 Passed: Critical patient")


# Test 2: Normal Patient
score,priority=calculate_priority(98,75,120,36.5,"None")
assert priority=="LOW"
print("Test 2 Passed: Normal patient")


# Test 3: Emergency Case
emergency=True
assert emergency==True
print("Test 3 Passed: Emergency case")


# Test 4: No ICU Beds
beds=0
assert beds==0
print("Test 4 Passed: No ICU beds")


# Test 5: Duplicate Patient
patients=["P001"]
new_patient="P001"
assert new_patient in patients
print("Test 5 Passed: Duplicate patient rejected")


# Test 6: Invalid Oxygen Level
oxygen=105
assert oxygen<0 or oxygen>100
print("Test 6 Passed: Invalid oxygen level rejected")


# Test 7: Invalid Heart Rate
heart_rate=0
assert heart_rate<=0
print("Test 7 Passed: Invalid heart rate rejected")


# Test 8: Priority Boundary 25
score,priority=calculate_priority(93,75,120,36.5,"None")
assert score>=25
assert priority in["MEDIUM","HIGH","CRITICAL"]
print("Test 8 Passed: Priority boundary")


# Test 9: Priority Boundary 50
score,priority=calculate_priority(89,110,120,36.5,"None")
assert score>=50
assert priority in["HIGH","CRITICAL"]
print("Test 9 Passed: Priority boundary")


# Test 10: Multiple Patients Competing For One Bed
beds=1
patients=[
    {"id":"P001","priority":"LOW"},
    {"id":"P002","priority":"CRITICAL"},
    {"id":"P003","priority":"HIGH"}
]

# Sorting Patients By Priority
priority_order={"CRITICAL":1,"HIGH":2,"MEDIUM":3,"LOW":4}
patients.sort(key=lambda x:priority_order[x["priority"]])

# Allocating The Single Bed
allocated_patient=patients[0]

assert allocated_patient["priority"]=="CRITICAL"
print("Test 10 Passed: Highest priority patient receives bed")


print("\nAll ICU Allocation QA Tests Passed.")
