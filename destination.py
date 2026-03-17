from database import mydb, mycursor

def insert_states_and_cities():
    try:
        # Insert States
        states = [
            'Andhra Pradesh', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 
            'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 
            'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 
            'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh', 
            'Uttarakhand', 'West Bengal'
        ]

        # Insert States into the 'states' table
        for state in states:
            mycursor.execute("INSERT INTO states (state_name) VALUES (%s)", (state,))
        
        mydb.commit()
        print("✅ States inserted successfully!")

        # Insert Cities for each state
        cities = {
            'Andhra Pradesh': ['Visakhapatnam', 'Tirupati', 'Amaravati'],
            'Bihar': ['Patna', 'Gaya'],
            'Chhattisgarh': ['Raipur', 'Bilaspur'],
            'Goa': ['Panaji', 'Vasco da Gama'],
            'Gujarat': ['Ahmedabad', 'Surat'],
            'Haryana': ['Chandigarh', 'Gurugram'],
            'Himachal Pradesh': ['Shimla', 'Manali'],
            'Jharkhand': ['Ranchi', 'Jamshedpur'],
            'Karnataka': ['Bangalore', 'Mysuru'],
            'Kerala': ['Kochi', 'Thiruvananthapuram'],
            'Madhya Pradesh': ['Bhopal', 'Indore'],
            'Maharashtra': ['Mumbai', 'Pune'],
            'Manipur': ['Imphal'],
            'Meghalaya': ['Shillong'],
            'Mizoram': ['Aizawl'],
            'Nagaland': ['Kohima'],
            'Odisha': ['Bhubaneswar', 'Puri'],
            'Punjab': ['Chandigarh', 'Amritsar'],
            'Rajasthan': ['Jaipur', 'Udaipur'],
            'Sikkim': ['Gangtok'],
            'Tamil Nadu': ['Chennai', 'Madurai'],
            'Telangana': ['Hyderabad'],
            'Uttar Pradesh': ['Lucknow', 'Varanasi'],
            'Uttarakhand': ['Dehradun', 'Nainital'],
            'West Bengal': ['Kolkata', 'Darjeeling']
        }

        # Insert Cities into the 'cities' table
        for state_name, cities_list in cities.items():
            # Get the state_id for the given state
            mycursor.execute("SELECT id FROM states WHERE state_name = %s", (state_name,))
            state_id = mycursor.fetchone()[0]

            # Insert cities for each state
            for city in cities_list:
                mycursor.execute("INSERT INTO cities (state_id, city_name) VALUES (%s, %s)", (state_id, city))

        mydb.commit()
        print("✅ Cities inserted successfully!")

    except Exception as e:
        print("⚠️ Error during insertion:", e)

    finally:
        mydb.close()

# Run the function
if __name__ == "__main__":
    insert_states_and_cities()
