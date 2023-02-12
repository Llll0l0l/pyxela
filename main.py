import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "ldark"
TOKEN = "adfsgtrew453egfsdfqer"


user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = pixela_endpoint + "/" + USERNAME + "/graphs"

graph_params_header = {
    "X-USER-TOKEN": TOKEN,
}

graph_params_body = {
    "id": "one",
    "name": "exercion",
    "unit": "calory",
    "type": "int",
    "color": "sora",
}


# response = requests.post(url=graph_endpoint, json=graph_params_body, headers=graph_params_header)
# print(response.text)


pixel_endpoint = f"{graph_endpoint}/{graph_params_body['id']}"

today = datetime.now().strftime("%Y%m%d")

pixel_body = {
    "date": today,
    "quantity": "100",
}

# response = requests.post(url=pixel_endpoint, json=pixel_body, headers=graph_params_header)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{today}"
update_params = {
    "quantity": "200",
}

# response = requests.put(url=update_endpoint, json=update_params, headers=graph_params_header)
# print(response.text)


# delete_endpoint = update_endpoint 
# response = requests.delete(url=delete_endpoint, headers=graph_params_header)









