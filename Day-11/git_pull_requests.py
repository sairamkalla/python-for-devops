import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(response)         #prints the status code
# print(response.json())  #prints all the info from the above url and converts json to dictionary
print(response.status_code) #gives the output as 200

complete_detail = response.json()

for i in range(len(complete_detail)):
    print(complete_detail[0]["user"]["login"])


