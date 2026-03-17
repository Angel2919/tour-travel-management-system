from database import mydb, mycursor

try:
    # Create users table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100)
        )
    """)

    # Create bookings table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            from_city VARCHAR(100),
            to_city VARCHAR(100),
            departure_date DATE,
            tour_type VARCHAR(50),
            budget INT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Create testimonials table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS testimonials (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            comment TEXT,
            rating INT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Create contact table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_queries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT
        )
    """)

    # Create services filter table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INT AUTO_INCREMENT PRIMARY KEY,
            state VARCHAR(100),
            tour_type VARCHAR(100),
            room_guest VARCHAR(100),
            from_city VARCHAR(100),
            to_city VARCHAR(100),
            departure_date DATE,
            budget INT
        )
    """)

    # ✅ Create states table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS states (
            id INT AUTO_INCREMENT PRIMARY KEY,
            state_name VARCHAR(100) UNIQUE
        )
    """)

    # ✅ Create cities table (linked to states)
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INT AUTO_INCREMENT PRIMARY KEY,
            state_id INT,
            city_name VARCHAR(100),
            FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
        )
    """)

    # ✅ Create tours table (linked to cities)
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS tours (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city_id INT,
            tour_name VARCHAR(100),
            tour_type VARCHAR(50),  -- for example, religious, cultural, wildlife, etc.
            price DECIMAL(10, 2),
            description TEXT,
            FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE
        )
    """)

    # ✅ Commit the changes and print success
    mydb.commit()
    print("✅ All tables created successfully!")

except Exception as e:
    print("⚠️ Error while creating tables:", e)

finally:
    if mydb.is_connected():
        mydb.close()
