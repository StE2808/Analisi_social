---
description: Raccoglie i trending topics di X (Twitter) Italia e salva i dati grezzi
---

# Collect Trends

Raccoglie i trending topics di X (Twitter) Italia e salva i dati grezzi.

## Obiettivo

Utilizzare l'API di X per recuperare i trending topics italiani correnti e salvarli in formato JSON strutturato.

## Task da eseguire

1. **Verifica credenziali API**
   - Controllare che esistano le credenziali X API nel file `.env`
   - Le chiavi richieste sono:
     - TWITTER_API_KEY
     - TWITTER_API_SECRET
     - TWITTER_ACCESS_TOKEN
     - TWITTER_ACCESS_TOKEN_SECRET
     - TWITTER_BEARER_TOKEN

2. **Crea struttura directory**
   - Assicurati che esista `data/raw/`
   - Se non esiste, creala

3. **Raccolta dati**
   - Connettiti all'API di X usando tweepy o snscrape
   - Recupera i trending topics per l'Italia (WOEID: 23424853)
   - Per ogni trending topic, raccogli:
     - Nome del topic
     - Tweet count (se disponibile)
     - URL del topic
     - Timestamp della raccolta
     - Campione di tweet (50-100) associati al topic per analisi successiva

4. **Salvataggio**
   - Salva i dati in formato JSON
   - Nomenclatura file: `trends_YYYYMMDD_HHMMSS.json`
   - Struttura JSON suggerita:
     ```json
     {
       "timestamp": "2026-01-09T15:30:00Z",
       "location": "Italy",
       "woeid": 23424853,
       "trends": [
         {
           "name": "#TrendingTopic",
           "url": "https://twitter.com/search?q=%23TrendingTopic",
           "tweet_volume": 15000,
           "sample_tweets": [
             {
               "id": "123456",
               "text": "Tweet text...",
               "created_at": "2026-01-09T15:25:00Z",
               "user": {"screen_name": "user", "followers_count": 1000},
               "retweet_count": 50,
               "favorite_count": 100
             }
           ]
         }
       ]
     }
     ```

5. **Logging**
   - Logga il numero di trend raccolti
   - Logga eventuali errori o problemi con l'API
   - Stampa il path del file salvato

## Script da creare/usare

Se non esiste, crea `scripts/collect_trends.py` con le funzioni necessarie.

## Note importanti

- Rispetta i rate limits dell'API di X
- Gestisci gli errori di connessione e API
- Non committare mai le credenziali nel repository
