# CLAUDE.md - Istruzioni per il Progetto Analisi_social

## Obiettivo del Progetto

Questo progetto si occupa di analizzare i trending topic di X (Twitter) Italia, generando report HTML completi con analisi del sentiment e insight sociologici.

## Struttura del Progetto

```
Analisi_social/
├── data/
│   └── raw/          # Dati grezzi raccolti da X API
├── reports/
│   └── archive/      # Report HTML archiviati
├── scripts/          # Script Python per l'analisi
├── CLAUDE.md         # Questo file
├── README.md         # Documentazione pubblica
└── .gitignore        # File da escludere dal version control
```

## Workflow Standard

### 1. Raccolta Dati
- Utilizzare l'API di X per recuperare i trending topic italiani
- Salvare i dati grezzi in formato JSON in `data/raw/`
- Nomenclatura file: `trends_YYYYMMDD_HHMMSS.json`

### 2. Analisi del Sentiment
- Processare i tweet relativi ai trending topic
- Analizzare il sentiment (positivo, negativo, neutro)
- Utilizzare librerie come TextBlob, VADER o modelli transformer italiani

### 3. Insight Sociologici
Analizzare i trend da diverse prospettive:
- **Tematiche dominanti**: Politica, cultura, sport, intrattenimento
- **Dinamiche temporali**: Orari di picco, durata del trend
- **Geografia**: Distribuzione geografica delle conversazioni
- **Demografie**: Analisi dei profili degli utenti coinvolti
- **Network analysis**: Identificazione degli influencer chiave
- **Polarizzazione**: Livello di divisione nelle opinioni

### 4. Generazione Report HTML
- Creare un report HTML interattivo e visualmente accattivante
- Includere grafici e visualizzazioni (chart.js, plotly, D3.js)
- Sezioni del report:
  - Executive Summary
  - Top Trending Topics
  - Analisi del Sentiment
  - Insight Sociologici
  - Timeline dei Trend
  - Network di Influencer
  - Conclusioni e Raccomandazioni

### 5. Archiviazione
- Salvare i report in `reports/archive/`
- Nomenclatura: `report_YYYYMMDD.html`
- Mantenere i file JSON grezzi per riferimento futuro

## Tecnologie Consigliate

### Python Libraries
- **tweepy** o **snscrape**: Raccolta dati da X
- **pandas**: Manipolazione dati
- **nltk** o **spacy**: Elaborazione linguaggio naturale
- **transformers**: Modelli NLP avanzati
- **matplotlib**, **seaborn**, **plotly**: Visualizzazioni
- **jinja2**: Template HTML
- **networkx**: Analisi delle reti sociali

### API Keys & Credentials
- Configurare le credenziali X API in variabili d'ambiente
- NON committare mai le API keys nel repository
- Utilizzare `.env` file per le configurazioni locali

## Best Practices

### Codice
- Scrivere script modulari e riutilizzabili
- Documentare le funzioni con docstrings
- Gestire gli errori e le eccezioni in modo appropriato
- Logging dettagliato delle operazioni

### Dati
- Rispettare i rate limits dell'API di X
- Implementare caching per ridurre le chiamate API
- Anonimizzare i dati personali nei report pubblici
- Rispettare la privacy degli utenti

### Report
- Design responsive per dispositivi mobili
- Accessibilità (WCAG guidelines)
- Performance ottimizzate (lazy loading per immagini/grafici)
- SEO friendly se pubblicati online

## Esempi di Analisi Sociologiche

### Analisi di Polarizzazione
Identificare temi divisivi e misurare il livello di polarizzazione:
- Ratio di sentiment positivo/negativo
- Presenza di echo chambers
- Crossover tra diverse bolle sociali

### Trend Emergenti
Rilevare segnali deboli di trend emergenti:
- Topic in rapida crescita
- Nuovi hashtag virali
- Shift nel discorso pubblico

### Event Detection
Correlare i trend con eventi esterni:
- Notizie nazionali/internazionali
- Eventi sportivi/culturali
- Crisi e situazioni di emergenza

## Checklist per Ogni Report

- [ ] Dati raccolti e validati
- [ ] Sentiment analysis completata
- [ ] Almeno 3 insight sociologici identificati
- [ ] Visualizzazioni chiare e informative
- [ ] Report HTML generato e testato
- [ ] File archiviato correttamente
- [ ] Dati sensibili rimossi/anonimizzati
- [ ] Quality check finale

## Note Importanti

1. **Etica**: Mantenere sempre un approccio etico nell'analisi dei dati social
2. **Bias**: Essere consapevoli dei bias algoritmici e cercare di mitigarli
3. **Contestualizzazione**: I dati social devono essere contestualizzati nel panorama culturale italiano
4. **Aggiornamento**: Le API e i trend cambiano rapidamente - mantenere il codice aggiornato

## Prossimi Passi Suggeriti

1. Configurare l'ambiente Python con i requisiti necessari
2. Creare script di raccolta dati iniziale
3. Sviluppare pipeline di analisi sentiment
4. Progettare template HTML per i report
5. Implementare automazione per report periodici (daily/weekly)
6. Creare dashboard interattiva (opzionale)

## Risorse Utili

- [X API Documentation](https://developer.twitter.com/en/docs)
- [Italian NLP Models](https://huggingface.co/models?language=it)
- [Social Media Analytics Best Practices](https://www.socialmediaexaminer.com/)
- [Data Visualization Guidelines](https://www.data-to-viz.com/)

---

**Ultimo aggiornamento**: 2026-01-09
**Versione**: 1.0
