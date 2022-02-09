import requests
import json

#quote generator
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " ~" + json_data[0]['a']
    return (quote)

meow = ["Meow","meow","Woof","woof","MEOW","WOOF"]