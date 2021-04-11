import json
import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

def translate(text, lang):
    payload = f"q={text}&source=pt&target={lang}"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': "efc14fb4a0msh42c27763b6f5e97p13a83ajsn5116d7350ab2",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    datas = json.loads(response.text)["data"]["translations"]

    print(datas[0]["translatedText"])


language = input("Digite o idioma [en/es]: ")[:3].lower()
phrase = input("Digite algo: ").split(" ")
phrase = "%20".join(phrase)

translate(phrase, language)