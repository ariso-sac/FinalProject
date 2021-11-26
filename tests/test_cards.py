import requests

base_url = "http://127.0.0.1"
final_url = base_url+":8080/api/card"
# final_url="/{0}/friendly/{1}/url".format(base_url,any_value_here)

#payload = {'number': 2, 'value': 1}
'''
payload = {
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
'''

payload = {
    "front": "fl", "back": "fl", "deck": "1"
}

response = requests.post(final_url, data=payload)

print(response.text)  # TEXT/HTML
print(response.status_code, response.reason)  # HTTP
