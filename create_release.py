import os
import requests
from datetime import datetime

# Configuració
REPO = "Diego06CH/Random_C"  # Reemplaça amb el teu repositori
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # Agafa el token de Jenkins
EXECUTABLE = "random_number"  # Nom de l'executable generat

# Genera un nom de release basat en la data i hora
release_name = f"Release {datetime.now().strftime('%Y-%m-%d %H:%M')}"

# Crea la release via GitHub API
url = f"https://api.github.com/repos/{REPO}/releases"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
data = {
    "tag_name": f"v{datetime.now().strftime('%Y%m%d%H%M')}",
    "name": release_name,
    "body": "Release automàtica generada per Jenkins"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("✅ Release creada correctament!")
    upload_url = response.json()["upload_url"].split("{")[0]
    
    # Puja l'executable com a asset
    with open(EXECUTABLE, "rb") as f:
        asset_response = requests.post(
            f"{upload_url}?name={EXECUTABLE}",
            headers=headers,
            data=f.read()
        )
        if asset_response.status_code == 201:
            print(f"✅ Executable {EXECUTABLE} pujat correctament!")
        else:
            print(f"❌ Error en pujar l'executable: {asset_response.text}")
else:
    print(f"❌ Error en crear la release: {response.text}")
