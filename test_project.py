import requests

# API URL
url = "http://localhost:8000/generate-article/"

# Test data
payload = {
    "video_ids": ["oxmGOkQJu3A"],  # Replace with a real YouTube video link
}

# Send the request
try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("API Response:")
        print(response.json())  # The generated article content
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
