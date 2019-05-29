import requests
import json

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data"

querystring = {"token": "c79258ecd2e64f3032404137d9a7237ed4958783"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "a8f7e2c3-5b0d-497f-b9fe-37838348a06c",
    'charset': "utf-8",
    'Content-Type': "application/json"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring, verify=False)

print(response)
print('Response' + response.text)

# Parse the response JSON as a Dictionary
jsonResponse = json.loads(response.text)
print(type(jsonResponse))

decodedString = ""
# Get the cypher in the JSON response
#cypher = response.text.numero_casas 
for letter in response.text:
    if letter.isalpha():
        decodedLetter = chr(ord(letter) + cypher)
        decodedString = decodedString.append(decodedLetter)
    else:
        decodedString = decodedString.append(letter)

print(decodedString)

with open('answer.json', 'w') as outfile:
	json.dump(data, outfile)