---
description: Genera insight sociologici approfonditi raggruppati per categoria
---

# Generate Insights

Genera insight sociologici approfonditi raggruppati per categoria.

## Obiettivo

Analizzare i trend da diverse prospettive sociologiche, con focus sulla distribuzione e le dinamiche per categoria del blog.

## Task da eseguire

1. **Carica i dati**
   - Leggi i file di categorizzazione e sentiment analysis
   - Carica dati storici se disponibili per confronti temporali

2. **Distribuzione per Categoria**
   - Analizza quali categorie dominano i trend del giorno
   - Confronta con distribuzioni storiche (se disponibili)
   - Identifica anomalie o shift significativi
   - Genera visualizzazione della distribuzione

3. **Tematiche Dominanti per Categoria**
   - Per ogni categoria principale identificata:
     - Estrai i temi ricorrenti
     - Identifica parole chiave e n-grammi frequenti
     - Raggruppa topic simili

4. **Analisi di Polarizzazione (focus: Politica, Geopolitica, Società)**
   - Per le categorie politiche e sociali:
     - Misura il livello di polarizzazione
     - Identifica temi divisivi
     - Analizza echo chambers
     - Ratio di sentiment per schieramento/corrente

5. **Network Analysis per Categoria**
   - Identifica gli influencer chiave per ogni categoria principale
   - Analizza le community e le loro interazioni
   - Mappa i flussi di informazione
   - Identifica i bridge tra categorie diverse

6. **Dinamiche Temporali**
   - Analizza quando ogni categoria domina:
     - Orari di picco per categoria
     - Durata media dei trend per categoria
     - Velocità di crescita per tipologia di topic
   - Pattern ricorrenti (es. Sport nel weekend, Politica in settimana)

7. **Analisi Geografica (se dati disponibili)**
   - Distribuzione geografica per categoria
   - Differenze regionali nei trend
   - Topic locali vs nazionali

8. **Cross-Category Analysis**
   - Identifica topic che attraversano più categorie
   - Analizza le correlazioni tra categorie
   - Trova pattern di co-occorrenza

9. **Trend Emergenti per Categoria**
   - Rileva segnali deboli di trend emergenti:
     - Scienza e Tecnologia: innovazioni, breakthrough
     - Società: nuovi comportamenti sociali, movimenti
     - Cultura: artisti emergenti, nuovi format
     - Economia: nuovi settori, startup trends

10. **Event Detection Categorizzato**
    - Correla i trend con eventi esterni:
      - Cronaca: crimini, processi
      - Ambiente: disastri naturali, conferenze clima
      - Diritti Umani: proteste, manifestazioni
      - Inchieste: scandali, rivelazioni

11. **Salvataggio**
    - Salva i risultati in `data/processed/insights_YYYYMMDD_HHMMSS.json`
    - Struttura JSON suggerita:
      ```json
      {
        "timestamp": "2026-01-09T17:00:00Z",
        "source_files": ["categorized_trends...", "sentiment_analysis..."],
        "category_distribution": {
          "Politica Interna": {"count": 12, "percentage": 24},
          "Cronaca Nera": {"count": 8, "percentage": 16},
          ...
        },
        "dominant_themes_by_category": {
          "Politica Interna": [
            {"theme": "Riforma costituzionale", "relevance": 0.85},
            {"theme": "Elezioni regionali", "relevance": 0.72}
          ],
          ...
        },
        "polarization_analysis": {
          "most_polarized_categories": ["Politica Interna", "Geopolitica"],
          "details": {
            "Politica Interna": {
              "polarization_score": 0.78,
              "divisive_topics": ["#RiformaCostituzionale", "#LeggeElettorale"],
              "echo_chambers_detected": true
            }
          }
        },
        "influencers_by_category": {
          "Politica Interna": [
            {"username": "politico123", "followers": 500000, "engagement": 8500}
          ],
          ...
        },
        "temporal_patterns": {
          "peak_hours_by_category": {
            "Politica Interna": ["09:00-11:00", "20:00-22:00"],
            "Sport": ["15:00-18:00", "21:00-23:00"]
          }
        },
        "cross_category_trends": [
          {
            "topic": "#CrisiClimatica",
            "categories": ["Ambiente", "Politica Estera", "Economia e Finanza"],
            "overlap_score": 0.65
          }
        ],
        "emerging_trends": [
          {
            "topic": "AI generativa nelle scuole",
            "category": "Scienza e Tecnologia",
            "growth_rate": 2.5,
            "signal_strength": "medium"
          }
        ],
        "key_insights": [
          "La categoria Politica Interna domina con il 24% dei trending topics",
          "Elevata polarizzazione rilevata nei temi di riforma costituzionale",
          "Trend emergente cross-category: crisi climatica collega Ambiente, Politica e Economia"
        ]
      }
      ```

12. **Report Testuale**
    - Genera un summary testuale degli insight principali
    - Almeno 3-5 insight significativi
    - Focus sulle categorie dominanti
    - Evidenzia pattern insoliti o rilevanti

## Script da creare/usare

Se non esiste, crea `scripts/generate_insights.py` con le funzioni necessarie.

## Tecnologie consigliate

- pandas per aggregazioni
- networkx per network analysis
- sklearn per clustering e pattern detection
- gensim per topic modeling
- matplotlib/seaborn per visualizzazioni esplorative

## Note importanti

- Gli insight devono essere actionable e interessanti per il lettore
- Contestualizzare sempre nel panorama culturale e politico italiano
- La categorizzazione è il filo conduttore di tutta l'analisi
- Confrontare con dati storici quando possibile per identificare trend
- Essere consapevoli dei bias algoritmici
