from flask import Flask,request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='notification_db'
        )
        return connection
    except Error as e:
        print("Error conencting to mysql: ", e)
        return None


# FIXED: URL typo and function name
@app.route('/store-notification', methods=["POST"])
def store_notification():
    data = request.json
    title = data.get('title')
    body = data.get('body')

    # FIXED: Look for 'type', not 'notification_type'
    notification_type = data.get('type')
    source = data.get('source', 'Instagram')

    if not title or not body:
        return jsonify({"error": "Title and body are required"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Database Connection failed"}), 500

    try:
        cursor = connection.cursor()
        query = """INSERT INTO notifications (title, body, type, source) \
                   VALUES (%s, %s, %s, %s) ON DUPLICATE KEY \
                   UPDATE received_at = CURRENT_TIMESTAMP"""

        cursor.execute(query, (title, body, notification_type, source))
        connection.commit()
        return jsonify({"message": "notification successfully stored"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
