"""
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.
In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals
"""
import requests, json
from pprint import pprint

response=requests.get("https://restcountries.com/v3.1/all").text
# response=requests.get("https://restcountries.com/v3.1/all")
response=json.loads(response)
for each in response:
    name=each["name"]["common"]
    area=each["area"]
    population=each["population"]
    # print(f"{name} have {area} km2 and {population/1000000} millions people")
    if name=="India":
        currency=each["currencies"]
        print(f"The currency of {name} is {currency}. The population is {population/1000000} millions people")
    if name=="France":
        currency=each["currencies"]
        print(f"The currency of {name} is {currency}. The population is {population/1000000} millions people")
    if name=="Costa Rica":
        currency=each["currencies"]
        print(f"The currency of {name} is {currency}. The population is {population/1000000} millions people")
    
    

