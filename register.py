from database import mydb, mycursor
import bcrypt

def register_user(name, email, password):
    try:
        # Check if user already exists
        mycursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing = mycursor.fetchone()

        if existing:
            print("❌ User with this email already exists.")
        else:
            # Hash the password before storing it in the database
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Insert new user with hashed password
            mycursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password)
            )
            mydb.commit()
            print("✅ User registered successfully!")

    except Exception as e:
        print("⚠️ Error during registration:", e)
        mydb.rollback()  # Rollback in case of error

# 🔹 Example usage (temporary, for testing)
if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    register_user(name, email, password)

# Don't close connection here
