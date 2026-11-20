movies = {
    "Avengers": 15,
    "Frozen": 12,
    "Tangled": 18,
}
 
bookings = []
 
ticket_number = 0
 
def book_seat(name, movie, tickets):
    global ticket_number
    ticket_number += 1
   
    price = movies[movie]
    total = tickets * price
   
    booking = {
        "ticket": ticket_number,
        "name": name,
        "movie": movie,
        "tickets": tickets,
        "total": total,
        "status": "Pending"
    }
    bookings.append(booking)
    return booking
 
def pay_ticket(ticket):
    for booking in bookings:
        if booking["ticket"] == ticket:
            booking["status"] = "Paid"
            return True
    return False