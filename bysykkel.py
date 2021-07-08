import requests, json
from datetime import datetime


response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")

response.raise_for_status()

svar = json.loads(response.text)

stasjoner = svar["data"]["stations"]

for stasj in stasjoner:
    
    if stasj["station_id"] == "391":

        tid = datetime.strftime(datetime.fromtimestamp(stasj["last_reported"]), "%d/%m-%Y %H.%M")

        sykkel = stasj["num_bikes_available"]
        plass = stasj["num_docks_available"]

        break


        
print(f"Sist oppdatert: {tid}")
print(f"Antall sykler ledig: {sykkel}")
print(f"    Antall plasser ledig: {plass}")
