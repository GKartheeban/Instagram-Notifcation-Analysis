Full-Stack Firebase Push Notification System
📝 Description
A complete, full-stack web application that demonstrates how to generate, receive, and persistently store web push notifications. This project simulates an "Instagram-style" notification system, utilizing Firebase Cloud Messaging (FCM) for real-time delivery, a Flask backend for API handling, and a MySQL database for permanent storage.

It effectively handles both foreground (when the user is actively on the page) and background (when the page is closed) notification states using JavaScript Service Workers.

✨ Key Features
Real-time Push Notifications: Triggered via Python using the Firebase Admin SDK.

FCM Token Management: Automatically requests browser permissions and generates unique device tokens.

Foreground & Background Handling: Captures notifications seamlessly whether the user is browsing the app or has the tab closed (via firebase-messaging-sw.js).

REST API Backend: A Flask-based server that listens for incoming notification data from the client side.

Database Persistence: Automatically logs all received notifications (title, body, type, source, and timestamp) into a MySQL database.

CORS Enabled: Secure cross-origin communication between the frontend client and the Flask server.

🛠️ Tech Stack
Frontend: HTML5, Vanilla JavaScript, Firebase Web SDK (v8.10.0)

Backend: Python, Flask, Flask-CORS

Database: MySQL (mysql-connector-python)

Services: Firebase Cloud Messaging (FCM), Firebase Admin SDK

🔄 How It Works (The Data Flow)
Client Setup: The user visits the web page and clicks "Enable Notification", prompting the browser to request notification permissions.

Token Generation: A Service Worker is registered, and an FCM token is generated for that specific browser instance.

Triggering the Push: A separate Python script (send_notification.py) uses the Firebase Admin SDK to send a simulated Instagram notification to the generated token.

Receiving the Payload: The browser receives the payload via the Service Worker (if closed) or the main thread (if open) and displays the native system notification.

Database Storage: The frontend instantly fires a POST request with the notification payload to the Flask API (/store-notification), which saves the record into the MySQL database.

*** ### Next Steps for your GitHub repository:
To make your repository completely ready, you might also want to add a quick "How to Run" section below this description. Be sure to remind people to:

Add their own firebaseConfig keys to the HTML and JS files.

Add their own serviceAccountKey.json to the Python folder (and remind them to add that file to .gitignore so they don't accidentally publish their private keys to GitHub!).

Run pip install flask flask-cors mysql-connector-python firebase-admin.
