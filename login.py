from database import mydb, mycursor
import bcrypt

def login_user(email, password):
    try:
        # Check if user exists
        mycursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = mycursor.fetchone()

        if user:
            # Compare hashed password with the one entered by the user
            if bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
                print("✅ Login successful!")
            else:
                print("❌ Incorrect password.")
        else:
            print("❌ User not found.")

    except Exception as e:
        print("⚠️ Error during login:", e)

    finally:
        mydb.close()

# 🔹 Example usage (temporary, for testing)
if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    login_user(email, password)
