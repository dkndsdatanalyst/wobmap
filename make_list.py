import json
import pandas as pd

with open('georef-germany-kreis.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extrahiere die Namen basierend auf deinem GeoJSON-Key (meist 'krs_name_short')
namen = [feature['properties']['krs_name_short'] for feature in data['features']]

# Speichern als saubere Liste
df = pd.DataFrame(sorted(list(set(namen))), columns=['landkreis'])
df.to_csv('landkreise.csv', index=False)
print("landkreise.csv erfolgreich erstellt!")