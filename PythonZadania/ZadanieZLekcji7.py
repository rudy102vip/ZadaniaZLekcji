import requests
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wather")

uzytkownik = input("Podaj na jaki dzień mam sprawdzić pogodę: ")
miasto = input("Podaj miasto dla którego mam sprawdzić pogodę: ")

def zmieńMiastoNaSzerokoscGeofraficzna():
    lokalizacja = geolocator.geocode(miasto)
    if lokalizacja:
        return (lokalizacja.latitude, lokalizacja.longitude)
    else:
        print("Nie można znaleźć lokalizacji dla podanego miasta")
        return none

latitude, longitude = zmieńMiastoNaSzerokoscGeofraficzna()
print(latitude)
print(longitude)

urlLink = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
           f"&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={uzytkownik}&end_date={uzytkownik}")

daneZApi = requests.get(url=urlLink)
print(daneZApi.status_code)
print(daneZApi.json())
