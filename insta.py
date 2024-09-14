import requests    # This line imports the requests library, which is used to send HTTP requests to websites.
from bs4 import BeautifulSoup    # BeautifulSoup from bs4 library helps us to easily extract data from web pages.
import uuid   # This library is used to generate unique identifiers (UUIDs).

insta_url = 'https://www.instagram.com'
username = input('Enter Instagram username: ')

response = requests.get(f"{insta_url}/{username}/") # Sends a GET request 

if response.ok:
    html_content = BeautifulSoup(response.text, 'html.parser')  #The HTML content of the response (in response.text) is converted to a 
                                                                #BeautifulSoup object for easier parsing and processing.

    picture = html_content.select_one('meta[property="og:image"]') #It looks for the meta tag of the profile image (with property="og:image")

    if picture:
        picture_url = picture['content'] #The URL of the profile image is extracted from the meta tag
        print("\nDownloading...")
        filename = f"pic_{uuid.uuid4()}.jpg" #A unique name is generated for the image using uuid.uuid4()
        with open(filename, 'wb') as file: # Opens a file named filename in binary write mode and defines the file variable for it.
            response = requests.get(picture_url, stream=True) #A GET request is sent to get the image from the extracted URL.
            if response.ok:
                file.write(response.content) #The content of the image received from the GET request is stored in the file.

                print("\nDownload completed.")
            else:
                print(f"Error downloading image: {response.status_code}")
    else:
        print("Profile picture meta tag not found.")
else:
    print(f"Error Instagram page: {response.status_code}")