
# Assessment 2 - Requisition System

class Requisition:
    next_id = 10001

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1

        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def add_requisition(self, items):
        self.total = 0

        for item in items:
            self.total += item["cost"]

        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

        return self.status

    def respond_requisition(self, decision):
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision == "Not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"
            else:
                print("Invalid decision. Enter Approved or Not approved.")

        return self.status

    def display_requisition(self):
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print("--------------------------------")

    @staticmethod
    def requisition_statistics(requisitions):
        total = len(requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for req in requisitions:
            if req.status == "Approved":
                approved += 1
            elif req.status == "Pending":
                pending += 1
            elif req.status == "Not approved":
                not_approved += 1

        print("Displaying the Requisition Statistics")
        print("Total requisitions submitted:", total)
        print("Total approved requisitions:", approved)
        print("Total pending requisitions:", pending)
        print("Total not approved requisitions:", not_approved)

        return total, approved, pending, not_approved



# Requisition 1
req1 = Requisition("20/11/2026", "FN19", "John Paul")

items1 = [
    {"item": "Keyboard", "cost": 150},
    {"item": "Mouse", "cost": 100},
    {"item": "Headphones", "cost": 200}
]

req1.add_requisition(items1)
req1.approve_requisition()
req1.display_requisition()


# Requisition 2
req2 = Requisition("20/11/2026", "FN20", "Tracy Brown")

items2 = [
    {"item": "Laptop", "cost": 800},
    {"item": "Laptop Bag", "cost": 200}
]

req2.add_requisition(items2)
req2.approve_requisition()
req2.display_requisition()


# Requisition 3
req3 = Requisition("20/11/2026", "FN15", "Emma Wellington")

items3 = [
    {"item": "Desktop Computer", "cost": 2500},
    {"item": "Monitor", "cost": 1000}
]

req3.add_requisition(items3)
req3.approve_requisition()
req3.respond_requisition("Not approved")
req3.display_requisition()


# Requisition 4 - Boundary Test ($499)
req4 = Requisition("20/11/2026", "FN22", "Sam")

items4 = [
    {"item": "Office Chair", "cost": 299},
    {"item": "Desk Lamp", "cost": 200}
]

req4.add_requisition(items4)
req4.approve_requisition()
req4.display_requisition()


# Requisition 5 - Boundary Test ($500)
req5 = Requisition("20/11/2026", "FN25", "Alex Smith")

items5 = [
    {"item": "Office Desk", "cost": 300},
    {"item": "Keyboard", "cost": 200}
]

req5.add_requisition(items5)
req5.approve_requisition()
req5.display_requisition()


# Display Initial Statistics
requisitions = [req1, req2, req3, req4, req5]

Requisition.requisition_statistics(requisitions)


# Test Manager Approval for Requisition 2
print("\nTesting Manager Approval")

req2.respond_requisition("Approved")
req2.display_requisition()


# Display Updated Statistics
Requisition.requisition_statistics(requisitions)


# Test Approval Boundary
print("\nTesting Approval Boundary")

assert req4.total == 499
assert req4.status == "Approved"

assert req5.total == 500
assert req5.status == "Pending"

print("All boundary tests passed!")


# Test Manager Decisions
print("\nTesting Manager Decisions")

assert req2.status == "Approved"
assert req2.approval_reference == "FN20002"

assert req3.status == "Not approved"
assert req3.approval_reference == "Not available"

print("All manager decision tests passed!")


# Final Statistics Test
print("\nTesting Final Statistics")

total, approved, pending, not_approved = Requisition.requisition_statistics(requisitions)

assert total == 5
assert approved == 3
assert pending == 1
assert not_approved == 1

print("All final statistics tests passed!")
