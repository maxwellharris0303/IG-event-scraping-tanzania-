import requests

def download_image(url, save_path):
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary mode and write the image content
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image successfully downloaded: {save_path}")
    else:
        print(f"Failed to retrieve image. HTTP Status code: {response.status_code}")

# Example usage
# image_url = 'https://scontent-hel3-1.cdninstagram.com/v/t51.29350-15/321363886_209458771473984_8119407454071164230_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE0NDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=100&_nc_ohc=_aNxxU1AaZYQ7kNvgErBkC4&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzAwMDMzODU1Mzg1MTI2NTMzMA%3D%3D.2-ccb7-5&oh=00_AYCVUYe0C6hOSBUO8mj6jXQyV3GehKdjSdinZE52nktAGA&oe=66CFC3C8&_nc_sid=8f1549'
# save_path = 'image.jpg'
# download_image(image_url, save_path)
