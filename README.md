# Analisi Social - Trending Topics X Italia

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## Panoramica

**Analisi_social** è un progetto di social media analytics focalizzato sull'analisi dei trending topic di X (Twitter) in Italia. Il sistema genera report HTML dettagliati che includono analisi del sentiment, insight sociologici e visualizzazioni interattive per comprendere le dinamiche delle conversazioni online nel contesto italiano.

## Caratteristiche Principali

- **Raccolta Dati Automatizzata**: Integrazione con X API per il recupero dei trending topic italiani
- **Sentiment Analysis**: Analisi approfondita del sentiment delle conversazioni (positivo, negativo, neutro)
- **Insight Sociologici**: Identificazione di pattern, temi emergenti e dinamiche sociali
- **Report HTML Interattivi**: Visualizzazioni responsive e grafici interattivi
- **Analisi Temporale**: Tracking dell'evoluzione dei trend nel tempo
- **Network Analysis**: Identificazione degli influencer e delle community

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

### ⚡ Quick Start con Claude Code (Consigliato)

Questo progetto include comandi slash personalizzati per Claude Code che automatizzano completamente il workflow di generazione dei report **senza richiedere API esterne**.

#### 1. Setup Iniziale

```
/setup
```

Inizializza la struttura del progetto creando tutte le directory necessarie.

#### 2. Generazione Report

```
/report
```

Quindi incolla i dati dei trending topic (puoi copiarli manualmente da X/Twitter). Claude genererà:
- Un report HTML professionale con design elegante
- Analisi del sentiment automatica
- Insight sociologici sulla viralità
- Commit e push automatico su GitHub

**Esempio di workflow**:
```
Utente: /report
Claude: "Per favore, incolla i dati dei trending topic..."
Utente: [incolla i trend del giorno]
Claude: [genera report, committa, pusha]
```

#### 3. Archiviazione Automatica

```
/archive
```

Sposta automaticamente i report più vecchi di 7 giorni in `reports/archive/`.

#### 4. Indice Report

```
/index
```

Genera una pagina HTML navigabile con tutti i report disponibili (perfetto per GitHub Pages).

#### Vantaggi dell'Approccio Claude Code

✅ **Nessuna API Key richiesta**: non serve configurare credenziali X
✅ **Semplicità**: un comando, zero configurazione
✅ **Flessibilità**: incolla qualsiasi dato di trend, anche manuale
✅ **Automazione Git**: commit e push automatici
✅ **Design professionale**: report HTML pronti per essere pubblicati

---

### 🐍 Utilizzo con Python (Opzionale)

Se preferisci usare script Python con l'API di X:

#### Raccolta dei Trending Topic

```bash
python scripts/collect_trends.py
```

Questo comando raccoglierà i trending topic italiani correnti e salverà i dati in `data/raw/`.

#### Analisi del Sentiment

```bash
python scripts/analyze_sentiment.py --input data/raw/trends_YYYYMMDD.json
```

#### Generazione Report HTML

```bash
python scripts/generate_report.py --date YYYYMMDD
```

Il report sarà salvato in `reports/archive/report_YYYYMMDD.html`.

#### Pipeline Completa

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

## Roadmap

- [ ] Implementazione pipeline base di raccolta dati
- [ ] Sviluppo modulo sentiment analysis
- [ ] Creazione template HTML report
- [ ] Integrazione analisi network
- [ ] Dashboard interattiva real-time
- [ ] API REST per accesso ai dati
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

### [1.0.0] - 2026-01-09
- Inizializzazione progetto
- Struttura base del repository
- Documentazione iniziale

---

**Note**: Questo progetto è a scopo educativo e di ricerca. Assicurati di rispettare i Terms of Service di X e le normative sulla privacy applicabili.
