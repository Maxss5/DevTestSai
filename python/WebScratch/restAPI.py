import requests

if __name__ == "__main__":
    url =  "http://placegoat.com/goatse/200/200"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        file = open('google.json','wb')
        file.write(response.content)
        file.close()
        print('archivo creado, revisa tu carpeta')

    if response.status_code == 429:
        print(response)

