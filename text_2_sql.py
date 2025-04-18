import psycopg2
from google import genai
import re

# Database connection details
dbname = "School"
user = "postgres"
password = "12345"
host = "localhost"
port = 5432

schema_description = ""
conn = None
cursor = None

try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Get a list of all tables in the public schema
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        schema_description += f"Table: {table_name}\n"

        # Get column information for each table
        cursor.execute("""
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_name = %s;
        """, (table_name,))

        columns = cursor.fetchall()

        for column_name, column_type, is_nullable, default_value in columns:
            schema_description += f"  - {column_name}: {column_type}"
            if is_nullable == "NO":
                schema_description += ", NOT NULL"
            if default_value is not None:
                schema_description += f", DEFAULT {default_value}"
            schema_description += "\n"

    #print(schema_description)  # Print schema details

except psycopg2.Error as e:
    print(f"Error retrieving schema: {e}")

client = genai.Client(api_key="AIzaSyBLsd17zgwUIB8DmgbNy1bUiPTu8XjOaXQ")
natural_language_query = input("Enter your query: ")
prompt = f"""
       You are a helpful assistant that translates natural language into SQL queries.
       Here is the database schema: {schema_description}.
       Only generate the SQL query, no other text.

       User Query: {natural_language_query}
       """
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)
response_text = response.text
#print(sql_query)

match = re.search(r"```sql\n(.*?)\n```", response_text, re.DOTALL)
sql_query = match.group(1) if match else response_text.strip()

#print(sql_query)

try:

    cursor.execute(sql_query)

    # Determine if the query is a SELECT statement
    if sql_query.strip().lower().startswith("select"):
        results = cursor.fetchall()
        print("Results:")
        for row in results:
            print(row)
    else:
        conn.commit()  # Commit changes for INSERT, UPDATE, DELETE queries
        print("Query executed successfully.")

except psycopg2.Error as e:
    print(f"Error executing SQL: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()