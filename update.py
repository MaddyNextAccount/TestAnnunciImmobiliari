import json
from datetime import datetime

# Annunci di esempio (simulazione)
annunci = [
    {
        "titolo": "Bilocale centro Cremona",
        "prezzo": "120.000 €",
        "link": "https://example.com/1"
    },
    {
        "titolo": "Trilocale zona Po",
        "prezzo": "185.000 €",
        "link": "https://example.com/2"
    }
]

# Creazione file JSON
data = {
    "ultimo_aggiornamento": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "annunci": annunci
}

with open("annunci.json", "w") as f:
    json.dump(data, f, indent=4)

print("File annunci.json creato con successo")
