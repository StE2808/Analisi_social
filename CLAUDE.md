# CLAUDE.md - Istruzioni per il Progetto Analisi_social

## Obiettivo del Progetto

Questo progetto si occupa di analizzare i trending topic di X (Twitter) Italia, classificandoli secondo le categorie del blog e generando report HTML completi con analisi del sentiment e insight sociologici.

## Categorie del Blog

Ogni trending topic viene classificato in una delle seguenti categorie prioritarie:

### Categorie Principali

1. **Opinioni ed Editoriali** - Commenti, riflessioni e prese di posizione su temi di attualità
2. **Politica Estera** - Eventi e discussioni sulla politica internazionale
3. **Politica Interna** - Dibattiti e notizie sulla politica nazionale italiana
4. **Geopolitica** - Analisi degli equilibri e rapporti di forza internazionali
5. **Ambiente** - Tematiche ecologiche, cambiamento climatico, sostenibilità
6. **Diritti Umani** - Discussioni su diritti civili, uguaglianza, giustizia sociale
7. **Inchieste e Dossier** - Approfondimenti investigativi e analisi dettagliate
8. **Scienza e Tecnologia** - Innovazioni, scoperte scientifiche, tech trends
9. **Società** - Temi sociali, demografici, culturali generali
10. **Cultura e Spettacolo** - Arte, cinema, musica, letteratura, entertainment
11. **Lifestyle e Moda** - Tendenze, benessere, stile di vita
12. **Cronaca Bianca** - Fatti quotidiani, eventi locali, notizie varie
13. **Cronaca Giudiziaria** - Procedimenti legali, sentenze, processi
14. **Cronaca Nera** - Crimini, incidenti, emergenze
15. **Cronaca Rosa** - Gossip, vip, celebrity news
16. **Economia e Finanza** - Mercati, business, economia nazionale e internazionale

### Logica di Categorizzazione

- Ogni topic deve essere assegnato alla categoria più pertinente
- In caso di topic multi-tematici, identificare la categoria primaria e secondaria
- Utilizzare NLP e keyword matching per la categorizzazione automatica
- Validazione manuale per topic ambigui o complessi

### Esempi di Keyword per Categoria

**Politica Interna**: Governo, Parlamento, elezioni, partito, Meloni, Salvini, Schlein, referendum, legge, decreto, ministro

**Politica Estera**: UE, NATO, USA, Russia, Cina, guerra, diplomazia, sanzioni, trattato, summit

**Geopolitica**: Mediterraneo, Medio Oriente, Africa, influenza, equilibri, potenza, alleanza

**Ambiente**: Clima, CO2, rinnovabili, inquinamento, biodiversità, sostenibilità, Green Deal

**Diritti Umani**: Discriminazione, uguaglianza, LGBT+, migranti, rifugiati, diritti civili, minoranze

**Scienza e Tecnologia**: AI, ricerca, scoperta, innovazione, tech, startup, digitale, spazio

**Economia e Finanza**: Borsa, PIL, inflazione, spread, banche, mercati, lavoro, imprese

**Cronaca Nera**: Omicidio, arresto, crimine, indagine, violenza, rapina

**Cronaca Rosa**: VIP, celebrity, gossip, matrimonio, separazione, scandalo

**Cultura e Spettacolo**: Cinema, musica, teatro, festival, libro, mostra, serie TV

**Sport** (sotto Cultura e Spettacolo): Calcio, Serie A, Champions, olimpiadi, tennis

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

### 2. Categorizzazione dei Topic
**PRIORITÀ ALTA** - Classificare ogni trending topic nelle categorie del blog:
- Analizzare il contenuto del topic e dei tweet correlati
- Applicare algoritmi di classificazione NLP (es. zero-shot classification)
- Assegnare categoria primaria (obbligatoria) e secondaria (opzionale)
- Calcolare confidence score per la categorizzazione
- Generare keyword clouds per categoria
- Output: `categorized_trends_YYYYMMDD_HHMMSS.json`

### 3. Analisi del Sentiment
- Processare i tweet relativi ai trending topic
- Analizzare il sentiment (positivo, negativo, neutro) **per categoria**
- Utilizzare librerie come TextBlob, VADER o modelli transformer italiani
- Confrontare sentiment tra diverse categorie

### 4. Insight Sociologici
Analizzare i trend da diverse prospettive, **raggruppando per categoria**:
- **Distribuzione per categoria**: Quali categorie dominano i trend del giorno
- **Tematiche dominanti**: Focus specifici all'interno di ogni categoria
- **Dinamiche temporali**: Orari di picco, durata del trend per categoria
- **Geografia**: Distribuzione geografica delle conversazioni per categoria
- **Demografie**: Analisi dei profili degli utenti coinvolti per categoria
- **Network analysis**: Identificazione degli influencer chiave per categoria
- **Polarizzazione**: Livello di divisione nelle opinioni, specialmente in Politica e Società
- **Cross-category trends**: Topic che attraversano più categorie

### 5. Generazione Report HTML
- Creare un report HTML interattivo e visualmente accattivante
- Includere grafici e visualizzazioni (chart.js, plotly, D3.js)
- **Strutturare tutto il report per categorie del blog**
- Sezioni del report:
  - **Executive Summary** con distribuzione per categoria
  - **Dashboard Categorie** - Grafico a torta/barre della distribuzione
  - **Top Trending Topics per Categoria** - Sezione dedicata per ogni categoria
  - **Analisi del Sentiment per Categoria** - Confronto sentiment tra categorie
  - **Insight Sociologici** raggruppati per categoria
  - **Timeline dei Trend** con filtri interattivi per categoria
  - **Network di Influencer** segmentato per categoria
  - **Heatmap Categorie** - Intensità dei trend per categoria nel tempo
  - **Cross-Category Analysis** - Correlazioni e overlap tra categorie
  - **Conclusioni e Raccomandazioni** specifiche per ogni categoria rilevante

### 6. Archiviazione
- Salvare i report in `reports/archive/`
- Nomenclatura: `report_YYYYMMDD.html`
- Mantenere i file JSON grezzi e categorizzati per riferimento futuro
- Archiviare anche `categorized_trends_YYYYMMDD_HHMMSS.json` per analisi storiche
- Mantenere storico delle distribuzioni per categoria per trend analysis a lungo termine

## Tecnologie Consigliate

### Python Libraries
- **tweepy** o **snscrape**: Raccolta dati da X
- **pandas**: Manipolazione dati
- **nltk** o **spacy**: Elaborazione linguaggio naturale
- **transformers**: Modelli NLP avanzati (per categorizzazione zero-shot)
- **scikit-learn**: Algoritmi di classificazione per categorizzazione
- **sentence-transformers**: Embeddings per similarità semantica
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

## Esempi di Analisi Sociologiche per Categoria

### Analisi di Polarizzazione (Politica Interna, Politica Estera, Geopolitica)
Identificare temi divisivi e misurare il livello di polarizzazione nelle categorie politiche:
- Ratio di sentiment positivo/negativo per partito/corrente
- Presenza di echo chambers nelle discussioni politiche
- Crossover tra diverse bolle sociali
- Analisi dei topic che dividono maggiormente l'opinione pubblica

### Trend Emergenti per Categoria
Rilevare segnali deboli di trend emergenti categorizzati:
- **Scienza e Tecnologia**: Nuove innovazioni, breakthrough scientifici
- **Società**: Cambiamenti nei comportamenti sociali, nuovi movimenti
- **Cultura e Spettacolo**: Artisti emergenti, nuovi format di intrattenimento
- **Economia e Finanza**: Nuovi settori, startup, trend di mercato

### Event Detection per Categoria
Correlare i trend con eventi esterni categorizzati:
- **Cronaca Nera/Giudiziaria**: Crimini, processi in corso
- **Cronaca Rosa**: Eventi celebrity, gossip virale
- **Ambiente**: Disastri naturali, conferenze sul clima
- **Diritti Umani**: Proteste, manifestazioni, movimenti sociali
- **Inchieste e Dossier**: Scandali, rivelazioni investigative

### Distribuzione Temporale per Categoria
Analizzare quando ogni categoria domina la conversazione:
- **Politica**: Picchi durante eventi politici, elezioni, crisi di governo
- **Sport** (Cultura e Spettacolo): Weekend, eventi sportivi
- **Economia**: Orari di apertura mercati, conferenze stampa BCE
- **Cronaca**: Distribuzione uniforme con picchi mattutini/serali

## Checklist per Ogni Report

- [ ] Dati raccolti e validati
- [ ] **Categorizzazione completata per tutti i trending topic**
- [ ] **Verifica manuale delle categorizzazioni ambigue**
- [ ] Sentiment analysis completata **per ogni categoria**
- [ ] **Distribuzione per categoria analizzata e visualizzata**
- [ ] Almeno 3 insight sociologici identificati **con focus sulle categorie dominanti**
- [ ] **Analisi cross-category completata**
- [ ] Visualizzazioni chiare e informative **con grafici per categoria**
- [ ] Report HTML generato e testato con **navigazione per categoria**
- [ ] File archiviato correttamente (inclusi dati categorizzati)
- [ ] Dati sensibili rimossi/anonimizzati
- [ ] Quality check finale

## Note Importanti

1. **Etica**: Mantenere sempre un approccio etico nell'analisi dei dati social
2. **Bias**: Essere consapevoli dei bias algoritmici e cercare di mitigarli
3. **Contestualizzazione**: I dati social devono essere contestualizzati nel panorama culturale italiano
4. **Aggiornamento**: Le API e i trend cambiano rapidamente - mantenere il codice aggiornato
5. **Categorizzazione**: La qualità della categorizzazione è fondamentale per l'utilità del report - investire tempo nella validazione e nel miglioramento degli algoritmi di classificazione
6. **Categorie Multiple**: Alcuni topic possono appartenere a più categorie - documentare sempre la logica di assegnazione primaria/secondaria

## Prossimi Passi Suggeriti

1. Configurare l'ambiente Python con i requisiti necessari
2. Creare script di raccolta dati iniziale
3. **[PRIORITÀ ALTA] Sviluppare sistema di categorizzazione automatica**
   - Implementare zero-shot classification con transformers
   - Creare keyword mapping per ogni categoria
   - Sviluppare sistema di validazione e confidence scoring
4. Sviluppare pipeline di analisi sentiment **per categoria**
5. Progettare template HTML per i report **con navigazione per categoria**
6. **Implementare visualizzazioni specifiche per categoria** (dashboard, heatmap)
7. Implementare automazione per report periodici (daily/weekly)
8. Creare dashboard interattiva con **filtri per categoria** (opzionale)
9. **Sviluppare sistema di tracking storico delle distribuzioni per categoria**

## Risorse Utili

- [X API Documentation](https://developer.twitter.com/en/docs)
- [Italian NLP Models](https://huggingface.co/models?language=it)
- [Social Media Analytics Best Practices](https://www.socialmediaexaminer.com/)
- [Data Visualization Guidelines](https://www.data-to-viz.com/)

---

**Ultimo aggiornamento**: 2026-01-09
**Versione**: 2.0 - Sistema di categorizzazione del blog integrato
