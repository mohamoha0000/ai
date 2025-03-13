


import requests

url=("https://malpha.123tokyo.xyz/get.php/a/a6/GgNq8qLVeVQ.mp3?cid=MmEwMTo0Zjg6YzAxMjozMmVlOjoxfE5BfERF&h=zMRM4nHkqMVrLkPGCsQt7w&s=1730986554&n=D-BOY%20-%20Binetna%20Layem%203chiri%20_%20%D8%A8%D9%8A%D9%86%D8%A7%D8%AA%D9%86%D8%A7%20%D8%A7%D9%84%D8%A3%D9%8A%D8%A7%D9%85%20%D8%B9%D8%B4%D9%8A%D8%B1%D9%8A%20%28Clip%20Officiel%29&uT=R&uN=bW9oYW1lZGVsbWFleW91Zg%3D%3D")

def get_headers(url, custom_headers=None):
    # Send a GET request to the specified URL
    response = requests.get(url, headers=custom_headers)
    
    # Print the status code and the headers of the response
    print(f"Status Code: {response.status_code}")
    
    # Print the headers dictionary
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

get_headers(url)
