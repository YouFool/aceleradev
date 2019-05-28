import requests

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
print(response.apparent_encoding)
print(response.text)

decodedString = ""
for letter in response.text:
    if letter.isalpha():
        val = bytes(letter, 'utf-8')
        print(type(val))
        decodedString = str(val)
    else:
        decodedString.__add__(letter)


print(decodedString)
