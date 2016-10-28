import requests
import json
head={'project_id': '184790648740', 'Content-Type': 'application/json', 'Authorization': 'key=AIzaSyBpHW6Bi0GKwWLFP5NADmYuna2v79o7Chw'}
messagestring=raw_input("Enter the message you wish to send as notification:")
d={'notification': {'sound': 'default', 'body': '%s'%messagestring}, 'to': 'f8MM_9b0w8Q:APA91bGSv8Sg7HdkJp2fKnx0D0vfMenTB2l71JYXml9uD5Ak9DpreH0oR4mcgrHbA4Q6mgdlBBWQcQB5N2qZXx6oz0ASgk2A-jpWUtULjXGnL1d7EFDvZvuqMZdbv2iUTXCahB7wR4YB', 'priority': 10}
lucky=requests.post(url='https://fcm.googleapis.com/fcm/send',headers=head,data=json.dumps(d))
