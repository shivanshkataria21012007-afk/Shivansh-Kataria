
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



    def add_requisition(self, items):
        self.items = items
        self.total = 0

        for item_name, price in items:
            self.total += price

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
                self.approval_reference = (
                    self.staff_id + str(self.requisition_id)[-3:]
                )
            elif decision == "Not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"

        return self.status

    def display_requisition(self):
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + format(self.total, "g"))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

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
        print("Total submitted:", total)
        print("Total approved:", approved)
        print("Total pending:", pending)
        print("Total not approved:", not_approved)

        return total, approved, pending, not_approved





# Create a requisition using terminal input
def enter_requisition():
    print("\nEnter your information:")
    req_date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    req = Requisition(req_date, staff_id, staff_name)

    print("Requisition ID:", req.requisition_id)
    print("\nAdd items:")

    items = []

    while True:
        item_name = input("Item Name: ")

        while True:
            try:
                price = float(input("Item Price ($): "))
                if price < 0:
                    print("Price cannot be negative.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        items.append((item_name, price))

        another = input("Add another item (yes/no): ").lower()
        if another != "yes":
            break

    req.add_requisition(items)
    req.approve_requisition()

    print("\nRequisition submitted:")
    req.display_requisition()

    return req


# Five requisitions for assessment testing
def test_five_requisitions(requisitions):
    if requisitions:
        print("Load examples before adding other requisitions.")
        return

    examples = [
        ("03/04/2024", "FN19", "John Paul",
         [("Printer paper", 150), ("Ink cartridges", 300)]),

        ("05/04/2024", "FN20", "Tracy Brown",
         [("Office chair", 600), ("Desk lamp", 400)]),

        ("07/05/2024", "FN15", "Emma Wellington",
         [("Laptop", 3000), ("Laptop bag", 500)]),

        ("03/05/2024", "FN02", "Catlin White",
         [("Stationery", 290), ("Whiteboard", 200)]),

        ("09/05/2024", "FN07", "Liam Smith",
         [("Monitor", 450), ("Keyboard", 50)])
    ]

    for req_date, staff_id, staff_name, items in examples:
        req = Requisition(req_date, staff_id, staff_name)
        req.add_requisition(items)
        req.approve_requisition()
        requisitions.append(req)

    print("\nBefore manager responses:")
    for req in requisitions:
        req.display_requisition()

    Requisition.requisition_statistics(requisitions)

    # Manager decisions
    requisitions[2].respond_requisition("Not approved")
    requisitions[4].respond_requisition("Approved")
    # Requisition 2 remains Pending

    print("\nAfter manager responses:")
    for req in requisitions:
        req.display_requisition()

    results = Requisition.requisition_statistics(requisitions)

    assert results == (5, 3, 1, 1)
    assert requisitions[0].total == 450
    assert requisitions[3].total == 490
    assert requisitions[4].total == 500

    print("\nAll five requisition tests passed!")


# Main terminal menu
def main():
    requisitions = []

    while True:
        print("\n========== REQUISITION SYSTEM ==========")
        print("1. Add New Requisition")
        print("2. Manager Response")
        print("3. Display All Requisitions")
        print("4. Display Statistics")
        print("5. Test Five Requisitions")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            req = enter_requisition()
            requisitions.append(req)

        elif choice == "2":
            req_id = input("Enter Requisition ID: ")

            for req in requisitions:
                if str(req.requisition_id) == req_id:
                    if req.status == "Pending":
                        decision = input(
                            "Decision (Approved/Not approved): "
                        )
                        req.respond_requisition(decision)
                        req.display_requisition()
                    else:
                        print("This requisition is already decided.")
                    break
            else:
                print("Requisition not found.")

        elif choice == "3":
            for req in requisitions:
                req.display_requisition()

        elif choice == "4":
            Requisition.requisition_statistics(requisitions)

        elif choice == "5":
            test_five_requisitions(requisitions)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
