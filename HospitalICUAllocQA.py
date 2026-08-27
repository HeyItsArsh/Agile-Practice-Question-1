# Adding a Ticket

patients=[]
waiting_list=[]

# Adding ICU Bed Availability
icu_beds=2

# Adding Patient Data
patients_data=[
    {"id":"P001","age":65,"oxygen":85,"heart_rate":130,"blood_pressure":170,"temperature":40.2,"conditions":"Diabetes","emergency":False},
    {"id":"P002","age":45,"oxygen":98,"heart_rate":75,"blood_pressure":120,"temperature":36.5,"conditions":"None","emergency":False},
    {"id":"P003","age":70,"oxygen":88,"heart_rate":125,"blood_pressure":180,"temperature":39.5,"conditions":"Heart Disease","emergency":True},
    {"id":"P004","age":30,"oxygen":95,"heart_rate":80,"blood_pressure":120,"temperature":37.0,"conditions":"None","emergency":False}
]

# Calculating Priority
def calculate_priority(patient):
    score=0

    # Checking Oxygen Level
    if patient["oxygen"]<90:
        score+=40
    elif patient["oxygen"]<94:
        score+=25
    elif patient["oxygen"]<97:
        score+=10

    # Checking Heart Rate
    if patient["heart_rate"]<50 or patient["heart_rate"]>120:
        score+=25
    elif patient["heart_rate"]<60 or patient["heart_rate"]>100:
        score+=10

    # Checking Blood Pressure
    if patient["blood_pressure"]<90 or patient["blood_pressure"]>160:
        score+=20
    elif patient["blood_pressure"]<100 or patient["blood_pressure"]>140:
        score+=10

    # Checking Temperature
    if patient["temperature"]<35 or patient["temperature"]>40:
        score+=15
    elif patient["temperature"]<36 or patient["temperature"]>38:
        score+=5

    # Checking Medical Conditions
    if patient["conditions"].lower()!="none":
        score+=10

    # Classifying Priority
    if score>=70:
        priority="CRITICAL"
    elif score>=50:
        priority="HIGH"
    elif score>=25:
        priority="MEDIUM"
    else:
        priority="LOW"

    return score,priority


# Processing Patients
for patient in patients_data:

    # Checking Duplicate Patient
    if any(p["id"]==patient["id"] for p in patients):
        print("Duplicate Patient Rejected:",patient["id"])
        continue

    # Adding Patient
    score,priority=calculate_priority(patient)

    patient["score"]=score
    patient["priority"]=priority
    patients.append(patient)


# Sorting Patients By Priority
priority_order={
    "CRITICAL":1,
    "HIGH":2,
    "MEDIUM":3,
    "LOW":4
}

patients.sort(
    key=lambda x:(not x["emergency"],priority_order[x["priority"]])
)

# Allocating ICU Beds
for patient in patients:

    # Allocating Available Bed
    if icu_beds>0:
        icu_beds-=1
        print(
            "Patient:",patient["id"],
            "| Priority:",patient["priority"],
            "| Score:",patient["score"],
            "| ICU Bed: ALLOCATED"
        )

    # Adding Patient To Waiting List
    else:
        waiting_list.append(patient)
        print(
            "Patient:",patient["id"],
            "| Priority:",patient["priority"],
            "| Score:",patient["score"],
            "| ICU Bed: WAITING LIST"
        )

# Displaying Waiting List
print("\nWaiting List:")

for patient in waiting_list:
    print(patient["id"],patient["priority"])
