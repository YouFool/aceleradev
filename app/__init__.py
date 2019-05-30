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

print('Response is:' + response.text)

# Parse the response JSON as a Dictionary
jsonResponse = json.loads(response.text)

# Get the cypher in the JSON response
cypher = jsonResponse['numero_casas']

decodedString = ""
for letter in jsonResponse['cifrado']:
    if letter.isalpha():
        decodedLetter = chr(ord(letter) - cypher)
        decodedString = decodedString.__add__(decodedLetter)
    else:
        decodedString = decodedString.__add__(letter)

print('Decoded string is: ' + decodedString)
jsonResponse['decifrado'] = decodedString
jsonResponse[]

## Use SH1 to encrypt the decoded string

fileName = 'answer.json'
with open(fileName, 'w') as outfile:
    json.dump(jsonResponse, outfile)

with open(fileName, 'rb') as f:
    url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution"
    headers = {
        'Content-Type': "multipart/form-data"
    }
    postResponse = requests.post(url, files={fileName: f}, headers=headers, params=querystring, verify=False)

    print(postResponse)


