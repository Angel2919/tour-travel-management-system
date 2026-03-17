from database import mydb, mycursor

def filter_services(state, tour_type, room_guest, from_city, to_city, departure_date, budget):
    try:
        # Apply the filter logic for services based on user input
        mycursor.execute("""
            SELECT * FROM services WHERE state = %s AND tour_type = %s AND room_guest = %s
            AND from_city = %s AND to_city = %s AND departure_date = %s AND budget <= %s
        """, (state, tour_type, room_guest, from_city, to_city, departure_date, budget))
        
        services = mycursor.fetchall()

        if services:
            for service in services:
                print(f"Service: {service}")
        else:
            print("❌ No services found for the given filter.")

    except Exception as e:
        print("⚠️ Error while filtering services:", e)

    finally:
        mydb.close()

# 🔹 Example usage (temporary, for testing)
if __name__ == "__main__":
    state = input("Enter your state: ")
    tour_type = input("Enter the tour type: ")
    room_guest = input("Enter rooms and guests: ")
    from_city = input("Enter from city: ")
    to_city = input("Enter to city: ")
    departure_date = input("Enter departure date (YYYY-MM-DD): ")
    budget = int(input("Enter your budget: "))
    filter_services(state, tour_type, room_guest, from_city, to_city, departure_date, budget)
