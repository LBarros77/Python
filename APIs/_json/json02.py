import requests

url = "https://currency-exchange.p.rapidapi.com/exchange"

def convertBrFor(toConvert="USD"):
    querystring = {"from":"BRL","to":f"{toConvert}", "q":"1.0"}

    headers = {
        'x-rapidapi-key': "efc14fb4a0msh42c27763b6f5e97p13a83ajsn5116d7350ab2",
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return float(response.text)


brl = input("Digite um valor para à conversão: ")
br_mony = brl.split(",")
br_mony = float(".".join(br_mony))

usd_converted = convertBrFor()
eur_converted = convertBrFor("EUR")

print(f"A cotação R$ 1,00 = USD {usd_converted:.3f}")
print(f"A cotação R$ 1,00 = USD {eur_converted:.3f}")
print(f"R$ {brl} = USD {(br_mony * usd_converted):.2f}")
print(f"R$ {brl} = EUR {(br_mony * eur_converted):.2f}")