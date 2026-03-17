from database import mydb, mycursor

def add_testimonial(user_id, comment, rating):
    try:
        # Insert new testimonial
        mycursor.execute(
            "INSERT INTO testimonials (user_id, comment, rating) VALUES (%s, %s, %s)",
            (user_id, comment, rating)
        )
        mydb.commit()
        print("✅ Testimonial added successfully!")

    except Exception as e:
        print("⚠️ Error while adding testimonial:", e)

    finally:
        mydb.close()

# 🔹 Example usage (temporary, for testing)
if __name__ == "__main__":
    # Testimonial data
    testimonials = [
        (1, "Pinki (Patna): Great experience! Loved the service!", 5),
        (2, "Geetanjali (Patna): Fantastic trip, highly recommend it!", 5),
        (3, "Muskan (Mumbai): Had a wonderful time, excellent support!", 4),
        (4, "Aditya (Bangalore): Amazing service but the food could improve.", 4),
        (5, "Arayan (Kolkata): Very helpful staff and smooth booking process.", 5),
        (6, "Prince (Jaipur): Good experience, but could have been more flexible with timings.", 3)
    ]
    
    # Add each testimonial to the database
    for testimonial in testimonials:
        user_id, comment, rating = testimonial
        add_testimonial(user_id, comment, rating)
