#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("./config/firebase-config.json")
admin = firebase_admin.initialize_app(cred)

# get all of user

page = auth.list_users()
while page:
    for user in page.users:
        print("user-->>" + user.uid)
        # get next batch of users

        page = page.get_next_page()

#
# Iterate through all users. This will still retrieve users in batches,
# buffering no more than 1000 users in memory at a time.

for user in auth.list_users().iterate_all():
    print("users--------->>" + user.uid)
