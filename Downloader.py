import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

def login():
    # Inserisci qui le tue credenziali
    payload = {
        'username': '<username>',
        'password': '<password>'
    }

    session_requests = requests.session()
    login_url = "<login_url>"
    result = session_requests.post(login_url, data=payload)

    return session_requests

def scrape(session_requests):
    url = 'https://podcasters.spotify.com/dash/catalog'
    result = session_requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    # Trova le statistiche nel soup e salva in un dataframe
    stats = {}
    # ...
    df = pd.DataFrame(stats)

    df['DataOraAcquisizione'] = datetime.now()

    # Salva il dataframe in un file CSV
    df.to_csv('spotify_podcast_stats.csv', index=False)

def job():
    session_requests = login()
    scrape(session_requests)

# Esegui il job una volta alla settimana
schedule.every().week.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
