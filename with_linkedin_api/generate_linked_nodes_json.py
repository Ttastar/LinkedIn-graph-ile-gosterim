from linkedin_api import Linkedin
from getpass import getpass
import json

email = input("Please input the email you use to log into LinkedIn:\n")
password = getpass("Please input your LinkedIn password: \n")
api = Linkedin(email, password)

pid = input("Please input your LinkedIn public profile id: \n")
profile = api.get_profile(pid)
uid = profile["profile_id"]

publicIds = {pid}
links = []

connections = api.get_profile_connections(uid)
numberOfConnections = len(connections)
index = 0

for connection in connections:
    index += 1
    print("downloading connection " + str(index) + " of " + str(numberOfConnections))

    if (index == 50):
        break

    firstPublicId = connection["public_id"]
    publicIds.add(connection["public_id"])
    links.append({
        "source": pid,
        "target": firstPublicId
        })

    secondConnections = api.get_profile_connections(connection["urn_id"])
    for secondConnection in secondConnections:
        secondPublicId = secondConnection["public_id"]
        if (secondPublicId != pid):
            publicIds.add(secondPublicId)
            links.append({"source": firstPublicId,
                        "target": secondPublicId})

