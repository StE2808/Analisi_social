---
description: Esegue l'intera pipeline di analisi dei trending topics end-to-end
---

# Run Pipeline

Esegue l'intera pipeline di analisi dei trending topics end-to-end.

## Obiettivo

Automatizzare l'intero workflow dall'acquisizione dati alla generazione del report HTML finale.

## Task da eseguire

Questo comando esegue in sequenza tutti gli step della pipeline:

1. **Collect Trends** (`/collect-trends`)
   - Raccoglie i trending topics da X API
   - Salva i dati grezzi in `data/raw/`
   - Output: `trends_YYYYMMDD_HHMMSS.json`

2. **Categorize** (`/categorize`)
   - Categorizza i trend nelle 16 categorie del blog
   - Salva i risultati in `data/raw/categorized_trends_YYYYMMDD_HHMMSS.json`
   - Verifica che non ci siano troppi trend che richiedono revisione manuale

3. **Analyze Sentiment** (`/analyze-sentiment`)
   - Analizza il sentiment per ogni topic e per categoria
   - Salva i risultati in `data/processed/sentiment_analysis_YYYYMMDD_HHMMSS.json`

4. **Generate Insights** (`/generate-insights`)
   - Genera insight sociologici approfonditi
   - Salva i risultati in `data/processed/insights_YYYYMMDD_HHMMSS.json`

5. **Create Report** (`/create-report`)
   - Compila tutti i dati in un report HTML interattivo
   - Salva il report in `reports/archive/report_YYYYMMDD.html`

6. **Quality Check Finale**
   - Verifica che tutti i file siano stati creati correttamente
   - Valida che il report HTML sia ben formato
   - Stampa un summary dell'esecuzione

7. **Archiviazione**
   - Assicura che tutti i file siano salvati correttamente
   - Opzionale: crea un backup compresso della giornata

## Gestione Errori

- Se uno step fallisce, logga l'errore ma cerca di completare gli step successivi se possibile
- Mantieni un log dettagliato dell'esecuzione in `logs/pipeline_YYYYMMDD_HHMMSS.log`
- In caso di errori critici (es. API non raggiungibile), interrompi la pipeline

## Output Finale

Al termine dell'esecuzione, stampa un report con:

```
=================================================
PIPELINE EXECUTION SUMMARY
=================================================
Execution Date: 2026-01-09 17:30:00
Status: SUCCESS / PARTIAL SUCCESS / FAILED
-------------------------------------------------

Steps Completed:
✓ Collect Trends      - 50 trends collected
✓ Categorize          - 50 trends categorized (5 need review)
✓ Analyze Sentiment   - Sentiment analysis completed
✓ Generate Insights   - 8 key insights identified
✓ Create Report       - HTML report generated

Files Generated:
- data/raw/trends_20260109_173000.json
- data/raw/categorized_trends_20260109_173200.json
- data/processed/sentiment_analysis_20260109_173400.json
- data/processed/insights_20260109_173600.json
- reports/archive/report_20260109.html

Category Distribution:
- Politica Interna: 12 (24%)
- Cronaca Nera: 8 (16%)
- Sport: 7 (14%)
- Economia e Finanza: 6 (12%)
- Altri: 17 (34%)

Top Insights:
1. Elevata polarizzazione rilevata in Politica Interna
2. Sentiment negativo dominante in Economia (-0.32)
3. Trend emergente: AI generativa nelle scuole

Report URL: file:///Users/ste/Desktop/Analisi_Social/reports/archive/report_20260109.html

Execution Time: 5m 32s
=================================================
```

## Modalità di Esecuzione

### Modalità Standard
Esegue la pipeline completa con i parametri di default.

### Modalità Opzionali

**Quick Mode** (se supportato)
- Raccoglie meno sample tweets per velocizzare
- Utile per testing

**Scheduled Mode** (per automazione futura)
- Può essere schedulato con cron per esecuzioni periodiche (daily/weekly)
- Invia notifiche via email al completamento (opzionale)

**Dry Run Mode** (per testing)
- Simula l'esecuzione senza chiamare le API o scrivere file
- Utile per verificare che la pipeline sia configurata correttamente

## Script da creare/usare

Se non esiste, crea `scripts/run_pipeline.py` che orchestra tutti gli altri script.

## Struttura del Pipeline Script

```python
# scripts/run_pipeline.py

import logging
from datetime import datetime
import sys

# Import altri script
from collect_trends import collect_trends
from categorize_trends import categorize_trends
from analyze_sentiment import analyze_sentiment
from generate_insights import generate_insights
from generate_report import generate_report

def setup_logging():
    # Setup logging configuration
    pass

def run_pipeline(mode='standard'):
    start_time = datetime.now()
    results = {}

    try:
        # Step 1: Collect
        logging.info("Starting Step 1: Collect Trends")
        results['collect'] = collect_trends()

        # Step 2: Categorize
        logging.info("Starting Step 2: Categorize")
        results['categorize'] = categorize_trends(results['collect']['output_file'])

        # Step 3: Sentiment
        logging.info("Starting Step 3: Analyze Sentiment")
        results['sentiment'] = analyze_sentiment(results['categorize']['output_file'])

        # Step 4: Insights
        logging.info("Starting Step 4: Generate Insights")
        results['insights'] = generate_insights(
            results['categorize']['output_file'],
            results['sentiment']['output_file']
        )

        # Step 5: Report
        logging.info("Starting Step 5: Create Report")
        results['report'] = generate_report(
            results['categorize']['output_file'],
            results['sentiment']['output_file'],
            results['insights']['output_file']
        )

        # Print summary
        print_summary(results, start_time)

        return results

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        print_error_summary(e)
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()
```

## Prerequisiti

Prima di eseguire la pipeline, verifica:
- [ ] Credenziali X API configurate nel `.env`
- [ ] Tutte le directory necessarie esistono (`data/raw/`, `data/processed/`, `reports/archive/`, `logs/`)
- [ ] Tutti i requirements Python sono installati
- [ ] Modelli NLP necessari sono scaricati

## Note importanti

- La pipeline completa può richiedere 5-15 minuti a seconda dei rate limits API
- Rispetta sempre i rate limits dell'API di X
- Salva log dettagliati per debugging
- Il report finale è standalone e può essere condiviso
- Considera l'automazione per esecuzioni periodiche (cron job, GitHub Actions)
