import base64
import requests

def img_to_base64(images_array):
    images_array_base64 = []
    for img in images_array:
        response = requests.get(img)
        uri = ("data:" +
               response.headers['Content-Type'] + ";" +
               "base64," + base64.b64encode(response.content).decode("utf-8"))
        images_array_base64.append(uri)
        #print(uri)

    return images_array_base64
