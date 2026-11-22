
# Assessment 2 - Requisition System
# Stage 1: Class and staff information

class Requisition:
    next_id = 10001

    def __init__(self, req_date, staff_id, staff_name):
        self.date = req_date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1

        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_reference = "Not available"


if __name__ == "__main__":
    sample = Requisition("03/04/2024", "FN19", "John Paul")
    print("Class created. Requisition ID:", sample.requisition_id)
    print("Staff:", sample.staff_name)
