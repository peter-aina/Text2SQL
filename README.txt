Natural Language to SQL Query Generator:

This project provides a Python-based solution that translates natural language queries into SQL queries, executes them on a PostgreSQL database, and returns the results. The program uses Google GenAI for natural language processing and the psycopg2 library to connect and interact with a PostgreSQL database.

Features: 
Connect to PostgreSQL: The program connects to a PostgreSQL database using psycopg2.

Generate SQL from Natural Language: The program uses Google GenAI to translate a user’s natural language query into an SQL query.

Execute SQL Queries: The program executes the generated SQL query on the PostgreSQL database and returns results or commits changes.

Database Schema Extraction: It automatically retrieves the schema of the database tables (including table names, column names, data types, and constraints) to aid in generating the SQL queries.

Prerequisites:

Ensure you have the following installed:

Python 3.x

PostgreSQL database running locally or remotely

Required Python libraries:

psycopg2 for PostgreSQL connection

google for GenAI interaction

re for regular expression matching in SQL response

Before running the code, modify the following parameters to suit your environment:

Database Connection:

dbname: The name of the PostgreSQL database (e.g., School).

user: Your PostgreSQL username (e.g., postgres).

password: Your PostgreSQL password.

host: The host address of your PostgreSQL server (default is localhost).

port: The port for PostgreSQL (default is 5432).

Google GenAI API Key: Replace the placeholder API key with your actual Google GenAI API key. This is needed to interact with Google's NLP model.

How It Works
Database Connection: The script connects to the PostgreSQL database using the credentials specified in the configuration section.

Schema Retrieval: It fetches the schema details of all tables in the public schema, including the table names, column names, data types, nullability, and default values.

User Input: The script prompts the user to input a natural language query (e.g., "Show me all students who scored above 80 in math").

Natural Language Processing: The input query is sent to the Google GenAI model, which processes the natural language and returns an SQL query.

SQL Query Execution: The generated SQL query is executed on the PostgreSQL database, and the results are displayed if it is a SELECT query. For other queries (e.g., INSERT, UPDATE, DELETE), changes are committed to the database.

Results: The results of the query are displayed on the console, or a success message is shown if the query is executed successfully without errors.

Example Workflow
Database Schema: The program retrieves schema information for a table, e.g., students with columns like id, name, score.

User Input: You enter the query: Show me all students who scored above 80 in math.

Generated SQL Query: The GenAI model translates the natural language query into an SQL query:

sql
Copy
Edit
SELECT * FROM students WHERE score > 80 AND subject = 'math';
Execution: The script executes the SQL query and returns the results.

Error Handling
If an error occurs during schema retrieval or query execution, an appropriate error message is displayed to the user.

SQL queries are executed inside a try-except block to handle any PostgreSQL-related errors.

Closing Connections
The program ensures that both the cursor and database connection are properly closed after execution to prevent any resource leakage.

License
This project is licensed under the MIT License - see the LICENSE file for details.