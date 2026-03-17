from database import mydb, mycursor

def book_tour(user_id, from_city, to_city, departure_date, tour_type, budget):
    try:
        # Insert new booking
        mycursor.execute(
            "INSERT INTO bookings (user_id, from_city, to_city, departure_date, tour_type, budget) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (user_id, from_city, to_city, departure_date, tour_type, budget)
        )
        mydb.commit()
        print("✅ Booking successful!")

    except Exception as e:
        print("⚠️ Error during booking:", e)

    finally:
        mydb.close()

# 🔹 Example usage (temporary, for testing)
if __name__ == "__main__":
    user_id = int(input("Enter your user ID: "))
    from_city = input("Enter your departure city: ")
    to_city = input("Enter your destination city: ")
    departure_date = input("Enter your departure date (YYYY-MM-DD): ")
    tour_type = input("Enter the tour type: ")
    budget = int(input("Enter your budget: "))
    book_tour(user_id, from_city, to_city, departure_date, tour_type, budget)
