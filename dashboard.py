import streamlit as st
import pandas as pd
import requests

st.title('Clinical Trials Dashboard')

condition = st.text_input('Search condition', 'diabetes')

url = "https://clinicaltrials.gov/api/v2/studies"
params = {'query.cond': condition,
          'pageSize': 20}

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
        'status': status,
        'link': f'https://clinicaltrials.gov/study/{nct_id}'
    })

df = pd.DataFrame(rows)

st.write('Total trials found:', len(df))

status_filter = st.selectbox('Filter by status', ['All'] + list(df['status'].unique()))

if status_filter != 'All':
    df = df[df['status'] == status_filter]

if len(df) > 0:
    if len(df) <= 5:
        st.write('Showing all', len(df), 'trials')
    else:
        num_results = st.slider('Number of trials to show', 5, len(df), min(10, len(df)))
        df = df.head(num_results)
        st.write('Showing', len(df), 'trials')

    status_counts = df['status'].value_counts()
    st.bar_chart(status_counts)

    st.dataframe(
        df,
        column_config={
            'link': st.column_config.LinkColumn('View on ClinicalTrials.gov', display_text='Open ↗')
        }
    )
else:
    st.write('No trials match this filter.')
