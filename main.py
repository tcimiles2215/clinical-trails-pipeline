import requests
import pandas as pd

conditions = 'diabetes'
url = "https://clinicaltrials.gov/api/v2/studies"
params = {'query.cond': conditions,
          'pageSize': 10}
response = requests.get(url, params=params)
data = response.json()
studies = data['studies']
rows = []
for study in studies:
    nct_id = study["protocolSection"]["identificationModule"]["nctId"]
    title = study["protocolSection"]["identificationModule"]["briefTitle"]
    status = study["protocolSection"]["statusModule"]["overallStatus"]

    rows.append({
        'nct_id': nct_id,
        'title': title,
        'status': status
    })
df = pd.DataFrame(rows)
print(df)
