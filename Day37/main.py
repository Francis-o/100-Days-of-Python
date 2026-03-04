import requests
import os
from datetime import date

pixela_token = os.getenv("pixela_token")
pixela_username = "osazuwa01"
graph_id = "graph1"
today = date.today()
formatted_date = today.strftime("%Y%m%d")
url = "https://pixe.la/"
create_profile_url = f"{url}v1/users/"
create_graph_url = f"{create_profile_url}{pixela_username}/graphs"
send_pixel_url = f"{create_graph_url}/{graph_id}"
update_pixel_url = f"{send_pixel_url}/{formatted_date}"



header = {
    "X-USER-TOKEN": pixela_token,
}
params = {
    "date": formatted_date,
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=send_pixel_url, json=params, headers=header)
response.raise_for_status()
# print(response.text)

