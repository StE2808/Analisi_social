# Analisi Social - Trending Topics X Italia

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

**📊 [Visualizza i Report Online](https://ste2808.github.io/Analisi_social/)**

## Panoramica

**Analisi_social** è un progetto di social media analytics focalizzato sull'analisi dei trending topic di X (Twitter) in Italia. Il sistema categorizza i trend secondo 16 categorie editoriali, genera report HTML dettagliati con analisi del sentiment, insight sociologici e visualizzazioni interattive per comprendere le dinamiche delle conversazioni online nel contesto italiano.

## Caratteristiche Principali

- **Categorizzazione Automatica**: Classificazione in 16 categorie editoriali del blog (Politica, Geopolitica, Economia, Cultura, Sport, Cronaca, Diritti Umani, Ambiente, Scienza, ecc.)
- **Raccolta Dati Automatizzata**: Integrazione con X API per il recupero dei trending topic italiani
- **Sentiment Analysis Avanzata**: Analisi del sentiment per topic e categoria con indici di polarizzazione
- **Cross-Category Analysis**: Identificazione di trend che attraversano multiple categorie
- **Insight Sociologici**: Pattern, trend emergenti, polarizzazione, event detection
- **Report HTML Interattivi**: Design editoriale premium, visualizzazioni responsive con Plotly.js
- **Pipeline End-to-End**: Sistema completo dalla raccolta dati alla generazione report

## Struttura del Progetto

```
Analisi_social/
├── data/
│   └── raw/              # Dati grezzi raccolti dall'API
├── reports/
│   └── archive/          # Report HTML generati
├── scripts/              # Script Python per analisi e processing
├── CLAUDE.md             # Istruzioni dettagliate del progetto
├── README.md             # Questo file
├── .gitignore            # File esclusi dal version control
└── requirements.txt      # Dipendenze Python (da creare)
```

## Prerequisiti

- Python 3.8 o superiore
- Account sviluppatore X (Twitter) con API access
- Librerie Python (vedi Installation)

## Installazione

### 1. Clona il repository

```bash
git clone https://github.com/your-username/Analisi_social.git
cd Analisi_social
```

### 2. Crea un ambiente virtuale

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Configura le credenziali API

Crea un file `.env` nella root del progetto:

```env
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

**IMPORTANTE**: Non committare mai il file `.env` nel repository!

## Utilizzo

### Raccolta dei Trending Topic

```bash
python scripts/collect_trends.py
```

Questo comando raccoglierà i trending topic italiani correnti e salverà i dati in `data/raw/`.

### Analisi del Sentiment

```bash
python scripts/analyze_sentiment.py --input data/raw/trends_YYYYMMDD.json
```

### Generazione Report HTML

```bash
python scripts/generate_report.py --date YYYYMMDD
```

Il report sarà salvato in `reports/archive/report_YYYYMMDD.html`.

### Pipeline Completa

Esegui l'intera pipeline con un singolo comando:

```bash
python scripts/run_pipeline.py
```

## Tipologie di Analisi

### 1. Sentiment Analysis
Analisi del sentiment delle conversazioni associate ai trending topic:
- Classificazione positivo/negativo/neutro
- Distribuzione del sentiment nel tempo
- Sentiment per topic specifico

### 2. Analisi Tematica
Identificazione delle categorie dominanti:
- Politica e attualità
- Sport e intrattenimento
- Tecnologia e innovazione
- Cultura e società

### 3. Network Analysis
Studio delle relazioni tra utenti:
- Identificazione degli influencer
- Analisi delle community
- Flussi di informazione

### 4. Analisi Temporale
Evoluzione dei trend:
- Velocità di crescita
- Durata dei trend
- Orari di picco

### 5. Insight Sociologici
Interpretazione delle dinamiche sociali:
- Livelli di polarizzazione
- Echo chambers
- Trend emergenti
- Correlazioni con eventi esterni

## Tecnologie Utilizzate

- **Python 3.8+**: Linguaggio principale
- **Tweepy/Snscrape**: Raccolta dati da X
- **Pandas**: Manipolazione e analisi dati
- **NLTK/spaCy**: Natural Language Processing
- **Transformers**: Modelli NLP avanzati
- **Matplotlib/Seaborn/Plotly**: Visualizzazioni
- **Jinja2**: Template HTML
- **NetworkX**: Analisi delle reti sociali

## Struttura dei Report HTML

I report generati includono:

1. **Executive Summary**: Panoramica dei principali trend
2. **Top Trending Topics**: Classifica dei topic più discussi
3. **Sentiment Analysis**: Distribuzione e analisi del sentiment
4. **Timeline**: Evoluzione temporale dei trend
5. **Network Visualization**: Grafo degli influencer
6. **Insight Sociologici**: Interpretazioni e pattern identificati
7. **Conclusioni**: Raccomandazioni e osservazioni finali

## Best Practices

### Etica e Privacy
- Anonimizzare sempre i dati personali nei report pubblici
- Rispettare i Terms of Service di X
- Non condividere mai le API credentials
- Utilizzare i dati in modo responsabile ed etico

### Performance
- Implementare caching per ridurre le chiamate API
- Rispettare i rate limits dell'API
- Ottimizzare le query sui dati
- Utilizzare processing parallelo quando possibile

### Qualità del Codice
- Seguire PEP 8 style guide
- Scrivere test unitari
- Documentare funzioni e classi
- Gestire errori ed eccezioni appropriatamente

## Visualizza i Report Online

I report sono pubblicati automaticamente su GitHub Pages:

**🌐 https://ste2808.github.io/Analisi_social/**

Ogni report include:
- Categorizzazione completa per le 16 categorie del blog
- Sentiment analysis con polarizzazione
- Insight sociologici approfonditi
- Visualizzazioni interattive
- Design editoriale premium dark mode

## Roadmap

- [x] Implementazione pipeline base di raccolta dati
- [x] Sistema di categorizzazione (16 categorie blog)
- [x] Sviluppo modulo sentiment analysis
- [x] Creazione template HTML report (design premium)
- [x] Cross-category analysis
- [x] GitHub Pages per pubblicazione report
- [ ] Integrazione analisi network avanzata
- [ ] Dashboard interattiva real-time
- [ ] API REST per accesso ai dati
- [ ] Automazione con GitHub Actions
- [ ] Notifiche automatiche per trend rilevanti
- [ ] ML models per previsione trend emergenti
- [ ] Supporto multi-lingua
- [ ] Mobile app per consultazione report

## Contribuire

Le contribuzioni sono benvenute! Per contribuire:

1. Fai un fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Committa le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Pusha al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## Autori

- **Il tuo nome** - *Initial work*

## Riconoscimenti

- X (Twitter) per l'accesso alle API
- Community open source per le librerie utilizzate
- Ricercatori nel campo della social media analytics

## Contatti

Per domande, suggerimenti o collaborazioni:
- Email: your.email@example.com
- GitHub: [@your-username](https://github.com/your-username)
- Twitter: [@your-handle](https://twitter.com/your-handle)

## Changelog

### [1.1.0] - 2026-01-09
- ✅ Pipeline completa end-to-end implementata
- ✅ Sistema di categorizzazione (16 categorie blog)
- ✅ Sentiment analysis con polarizzazione
- ✅ Cross-category analysis
- ✅ Template HTML premium (dark mode, Playfair Display)
- ✅ Report interattivi con Plotly.js
- ✅ GitHub Pages per pubblicazione online
- ✅ Primo report completo pubblicato (9 Gennaio 2026)

### [1.0.0] - 2026-01-09
- Inizializzazione progetto
- Struttura base del repository
- Documentazione iniziale (CLAUDE.md)

---

**Note**: Questo progetto è a scopo educativo e di ricerca. Assicurati di rispettare i Terms of Service di X e le normative sulla privacy applicabili.
