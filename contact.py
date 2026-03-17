from database import mydb, mycursor

def save_contact_message(name, email, message, contact_type):
    try:
        # Insert contact message with contact type
        query = "INSERT INTO contact_messages (name, email, message, contact_type) VALUES (%s, %s, %s, %s)"
        values = (name, email, message, contact_type)
        mycursor.execute(query, values)
        mydb.commit()
        print("✅ Contact message saved successfully.")
    except Exception as e:
        print("⚠️ Error while saving contact message:", e)

# 🧪 Sample test (remove this in production)
if __name__ == "__main__":
    # Test data for each contact option (using the names you requested)
    contact_messages = [
        ("Pinki Kumari", "pinki.patna@gmail.com", "I would like to inquire about beach tours in Goa.", "Email Us"),
        ("Geetanjali Kumari", "geetanjali.patna@gmail.com", "Can I call for a booking?", "Call Support"),
        ("Muskan", "muskan.mumbai@gmail.com", "Please assist with live chat for train bookings.", "Live Chat"),
        ("Aditya", "aditya.bangalore@gmail.com", "Send me the booking details on WhatsApp.", "WhatsApp"),
        ("Arayan", "arayan.kolkata@gmail.com", "Can I reach out through Social Media for discounts?", "Social Media"),
        ("Prince", "prince.jaipur@gmail.com", "I need information about the head office location.", "Head Office")
    ]
    
    # Save each contact message to the database
    for contact in contact_messages:
        name, email, message, contact_type = contact
        save_contact_message(name, email, message, contact_type)
