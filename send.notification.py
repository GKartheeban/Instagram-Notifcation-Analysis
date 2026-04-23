import random
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("D:/Project_SQL/service_key/serviceAccountKey.json")

firebase_admin.initialize_app(cred)



def get_random_instagram_notification():
    notifications = [
        "user1 liked your photo",
        "user2 sent you a friend request",
        "user3 started a live video",
        "user4 commented on your post",
        "user5 tagged you in a photo",
        "user6 shared your post",
        "user7 followed you",
        "user8 sent you a message",
    ]
    return random.choice(notifications)

def send_notification(token,title,body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title = title,
                body = body,
            ),
            token = token,
        )

        respose = messaging.send(message)
        print("Successfully sent message: ",respose)

    except Exception as e:
        print("Error sending Message:",e)


if __name__ == "__main__":
    fcm_token = "eXEVLxmT_VytlZ1fIepPMM:APA91bEZI1XTCFH_uTo_Yj2GSwuChloj42RhO4ERay-zBtyKFj4WASnlZxGBWo0RNOchSIOygFCyhlcuv-2Bsph5LA9PVUNOU0LYeY9O_U1PBSu1qtq-xaY"

    notification_body = get_random_instagram_notification()
    notification_title = "Instagram Notification"

    send_notification(fcm_token, notification_title, notification_body)