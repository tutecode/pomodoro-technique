import psycopg2
from psycopg2 import Error

def create_table(work_duration, break_duration):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port",
            database="your_database"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Check if the table already exists
        check_table_query = """
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_name = 'pomodoro_settings'
            );
        """
        cursor.execute(check_table_query)
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # Create the table with the specified columns
            create_table_query = """
                CREATE TABLE pomodoro_settings (
                    id SERIAL PRIMARY KEY,
                    work_duration INT,
                    break_duration INT
                );
            """
            cursor.execute(create_table_query)
            connection.commit()

            print("Table created successfully.")

        # Insert the work_duration and break_duration values into the table
        insert_query = f"""
            INSERT INTO pomodoro_settings (work_duration, break_duration)
            VALUES ({work_duration}, {break_duration});
        """
        cursor.execute(insert_query)
        connection.commit()

        print("Data inserted successfully.")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL or executing queries:", error)

    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()



# ESTA PARTE LA TENGO QUE PONER EN EL OTRO SCRIPT
# Prompt the user to enter work duration and break duration
work_duration = int(input("Enter the work duration (in minutes): "))
break_duration = int(input("Enter the break duration (in minutes): "))

# Call the create_table function with the provided durations
create_table(work_duration, break_duration)

