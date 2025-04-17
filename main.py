class Patient:
    def __init__(self, patient_guid: int, name: str, age: int) -> None:
        """
        A patient has a guid, name, and an age.
        """
        self.patient_guid = patient_guid
        self.name = name
        self.age = age

    def get_summary(self) -> str:
        return f"Patient GUID: {self.patient_guid}, Name: {self.name}, Age: {self.age}"

# Create an object
patient = Patient(1324324324, "Fola", 26)
print(patient.get_summary())
