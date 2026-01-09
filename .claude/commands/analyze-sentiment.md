---
description: Analizza il sentiment dei tweet associati ai trending topics per categoria
---

# Analyze Sentiment

Analizza il sentiment dei tweet associati ai trending topics, raggruppato per categoria.

## Obiettivo

Processare i tweet relativi ai trending topic e analizzare il sentiment (positivo, negativo, neutro) con focus sulla distribuzione per categoria.

## Task da eseguire

1. **Carica i dati categorizzati**
   - Leggi il file `categorized_trends_YYYYMMDD_HHMMSS.json` più recente
   - O specifica un file particolare se fornito

2. **Preprocessing dei tweet**
   - Pulisci il testo
   - Rimuovi stopwords italiane
   - Normalizza emoticon e emoji
   - Gestisci hashtag e menzioni

3. **Analisi del sentiment**
   - Per ogni tweet di ogni trending topic:
     - Classifica il sentiment come: positivo, negativo, neutro
     - Calcola un sentiment score (-1 a +1)
     - Utilizza uno di questi approcci:
       - VADER con lessico italiano
       - TextBlob con traduzione
       - Modelli transformer italiani (es. `neuraly/bert-base-italian-cased-sentiment`)
       - Feel-IT (sentiment analysis per italiano)

4. **Aggregazione per topic**
   - Per ogni trending topic calcola:
     - Percentuale sentiment positivo/negativo/neutro
     - Sentiment score medio
     - Deviazione standard (per misurare polarizzazione)

5. **Aggregazione per categoria**
   - Raggruppa i risultati per categoria primaria
   - Calcola statistiche aggregate per categoria:
     - Sentiment medio della categoria
     - Distribuzione sentiment (% pos/neg/neu)
     - Categoria più positiva/negativa
     - Livello di polarizzazione per categoria

6. **Analisi temporale**
   - Se disponibili timestamp dei tweet:
     - Traccia l'evoluzione del sentiment nel tempo
     - Identifica picchi di sentiment positivo/negativo

7. **Salvataggio**
   - Salva i risultati in `data/processed/sentiment_analysis_YYYYMMDD_HHMMSS.json`
   - Struttura JSON suggerita:
     ```json
     {
       "timestamp": "2026-01-09T16:00:00Z",
       "source_file": "categorized_trends_20260109_153000.json",
       "sentiment_by_topic": [
         {
           "topic_name": "#TrendingTopic",
           "category": "Politica Interna",
           "sentiment_distribution": {
             "positive": 35,
             "negative": 45,
             "neutral": 20
           },
           "sentiment_score": -0.15,
           "polarization_index": 0.72,
           "tweet_count": 100
         }
       ],
       "sentiment_by_category": {
         "Politica Interna": {
           "avg_sentiment_score": -0.22,
           "distribution": {"positive": 30, "negative": 50, "neutral": 20},
           "polarization_index": 0.68,
           "topic_count": 12
         },
         ...
       },
       "overall_statistics": {
         "most_positive_category": "Cultura e Spettacolo",
         "most_negative_category": "Politica Interna",
         "most_polarized_category": "Geopolitica"
       }
     }
     ```

8. **Report**
   - Stampa un summary dell'analisi
   - Evidenzia le categorie più polarizzate
   - Mostra le differenze di sentiment tra categorie

## Script da creare/usare

Se non esiste, crea `scripts/analyze_sentiment.py` con le funzioni necessarie.

## Tecnologie consigliate

- transformers (modelli italiani)
- feel-it
- vaderSentiment (con lessico IT)
- textblob

## Note importanti

- L'analisi del sentiment deve essere **per categoria** per essere utile
- Il contesto italiano è importante - usare modelli addestrati su testo italiano
- La polarizzazione è un indicatore chiave per categorie come Politica
- Confrontare il sentiment tra diverse categorie fornisce insight preziosi
