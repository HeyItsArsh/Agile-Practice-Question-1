# Adding a Ticket
patients=[]
waiting_list=[]
allocated_beds=0

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
        priority="CRITICAL"
    elif score>=50:
        priority="HIGH"
    elif score>=25:
        priority="MEDIUM"
    else:
        priority="LOW"

    return score,priority

def add_patient():
    global allocated_beds

    # Taking Patient Details
    patient_id=input("Enter Patient ID: ")

    # Checking Duplicate Patient
    for patient in patients:
        if patient["id"]==patient_id:
            print("Duplicate Patient ID. Patient rejected.")
            return

    try:
        age=int(input("Enter Age: "))
        oxygen=float(input("Enter Oxygen Level: "))
        heart_rate=int(input("Enter Heart Rate: "))
        blood_pressure=int(input("Enter Blood Pressure: "))
        temperature=float(input("Enter Temperature: "))
    except ValueError:
        print("Invalid input.")
        return

    conditions=input("Enter Existing Medical Conditions: ")
    emergency=input("Emergency Case? (yes/no): ").lower()

    # Validating Oxygen Level
    if oxygen<0 or oxygen>100:
        print("Invalid oxygen level.")
        return

    # Validating Heart Rate
    if heart_rate<=0:
        print("Invalid heart rate.")
        return

    # Calculating Priority
    score,priority=calculate_priority(
        oxygen,heart_rate,blood_pressure,temperature,conditions
    )

    patient={
        "id":patient_id,
        "age":age,
        "score":score,
        "priority":priority,
        "emergency":emergency=="yes"
    }

    patients.append(patient)

    # Allocating ICU Bed
    if allocated_beds>0:
        allocated_beds-=1
        print("ICU Bed Allocated")
        print("Patient:",patient_id)
        print("Priority:",priority)
        print("Score:",score)
    else:
        waiting_list.append(patient)
        print("No ICU beds available.")
        print("Patient added to waiting list.")


def display_patients():
    # Displaying Patient Information
    print("\nPatients:")
    for patient in patients:
        print(
            patient["id"],
           patient["priority"],
           patient["score"]
        )

    # Displaying Waiting List
    print("\nWaiting List:")
    for patient in waiting_list:
        print(
            patient["id"],
           patient["priority"],
           patient["score"]
        )


def main():
    global allocated_beds

    # Setting ICU Bed Availability
    try:
        allocated_beds=int(input("Enter Available ICU Beds: "))
    except ValueError:
        print("Invalid number of beds.")
        return

    # Adding Patients
    while True:
        add_patient()
        choice=input("Add another patient? (yes/no): ").lower()
        if choice!="yes":
            break

    # Displaying Results
    display_patients()


if __name__=="__main__":
    main()
