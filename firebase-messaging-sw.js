importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');

firebase.initializeApp({
    apiKey: "AIzaSyB_KTD7uzaYz7_aD9w3MlKR_ZLBlsBRL2g",
    projectId: "inlaid-citron-403818",
    messagingSenderId: "948468092126",
    appId: "1:948468092126:web:6afee20ad2b4b6641d064f"
});

// We only declare this ONCE
const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log('[firebase-messaging-sw.js] Received background message:', payload);

    const notificationTitle = payload.notification?.title || 'Background Notification';
    const notificationBody = payload.notification?.body || 'Background body';

    self.registration.showNotification(notificationTitle, {
        body: notificationBody,
        icon: payload.notification?.icon || 'default-icon.png',
    });

    fetch('http://localhost:5000/store-notification', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title: notificationTitle,
            body: notificationBody,
            type: 'background',
            source: 'Instagram',
        }),
    })
        .then(response => response.json())
        .then((data) => console.log('Notification stored in MYSQL: ', data))
        .catch((error) => console.log('Error storing notification in MYSQL: ', error));
});