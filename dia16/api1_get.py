import requests, json

url = "https://jsonplaceholder.typicode.com/posts"

payload = {}#datos a enviar
headers = {}#formato o tipo de dato

#response = requests.request("GET", url, headers=headers, data=payload)

response = requests.get(url)

print("")
print(response)#<Response [200]>

if response.status_code == 200:
    #print(response.text) #convierte la respuesta en un string
    respuesta = json.loads(response.text)#conversión del texto a formato JSON
    print(type(respuesta))#<class 'list'>
    for posicion, dicc in enumerate(respuesta):
        print(f"diccionario{posicion} {dicc}")
    
else:
    print("Error en la solicitud", response.status_code)