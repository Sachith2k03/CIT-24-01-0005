import os
import time

import psycopg2
from flask import Flask

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])


def initialize_database():
    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS visits (
                    id SERIAL PRIMARY KEY,
                    count INTEGER NOT NULL DEFAULT 0
                );
                """
            )

            cursor.execute("SELECT COUNT(*) FROM visits;")
            row_count = cursor.fetchone()[0]

            if row_count == 0:
                cursor.execute(
                    "INSERT INTO visits (count) VALUES (0);"
                )

            connection.commit()
            cursor.close()
            connection.close()

            print("Database connected successfully.")
            return

        except psycopg2.OperationalError as error:
            print(
                f"Database connection attempt "
                f"{attempt}/{max_attempts} failed."
            )
            print(error)

            if attempt < max_attempts:
                print("Waiting for PostgreSQL...")
                time.sleep(3)

    raise RuntimeError(
        "Could not connect to PostgreSQL after several attempts."
    )


@app.route("/")
def home():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE visits
            SET count = count + 1
            WHERE id = (
                SELECT id
                FROM visits
                ORDER BY id
                LIMIT 1
            )
            RETURNING count;
            """
        )

        result = cursor.fetchone()
        connection.commit()

        if result is None:
            return "<h2>Visit counter could not be updated.</h2>", 500

        visit_count = result[0]

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            >
            <title>Docker Flask Application</title>
        </head>
        <body>
            <h1>Docker Flask Application</h1>
            <h2>Database Connected Successfully!</h2>
            <p>Total visits: {visit_count}</p>
        </body>
        </html>
        """

    except psycopg2.Error as error:
        print(f"Database error: {error}")

        if connection is not None:
            connection.rollback()

        return "<h2>Unable to connect to the database.</h2>", 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


@app.route("/health")
def health():
    return {"status": "running"}, 200


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5000)