# Analisi Social - Guida all'Uso

Sistema automatizzato per l'analisi di trending topics da X (Twitter) Italia con categorizzazione intelligente, analisi sentiment e generazione report HTML.

---

## 🚀 Quick Start

### 1. Installa dipendenze

```bash
pip install -r requirements.txt
```

### 2. Prepara i file markdown

Salva i file markdown generati da Perplexity in `data/daily/`:
- Un file per le **notizie politiche** (contiene keyword: "agenzie", "ANSA", "governo")
- Un file per i **trending topics** (contiene keyword: "trend", "Twitter", "hashtag")

Esempio:
```
data/daily/
├── politica_oggi.md
└── trend_oggi.md
```

### 3. Genera il report

```bash
python scripts/generate_report.py
```

### 4. Visualizza il report

Il report HTML verrà salvato in:
```
reports/report_YYYY-MM-DD.html
```

Aprilo con un browser per visualizzarlo.

---

## 📁 Struttura del Progetto

```
Analisi_social/
├── data/
│   ├── daily/          # File markdown da processare (INPUT)
│   ├── processed/      # File già processati (ARCHIVIO)
│   └── raw/            # Altri dati grezzi
├── reports/
│   └── report_*.html   # Report generati (OUTPUT)
├── config/
│   ├── categories.json      # 16 categorie del blog
│   ├── sentiment_rules.json # Regole sentiment italiano
│   └── settings.yaml        # Configurazione generale
├── scripts/
│   ├── generate_report.py      # ORCHESTRATORE PRINCIPALE
│   ├── parser.py               # Parse markdown
│   ├── categorizer.py          # Categorizzazione
│   ├── sentiment_analyzer.py   # Analisi sentiment
│   ├── template_engine.py      # Generazione HTML
│   └── utils.py                # Utility comuni
├── templates/
│   └── report_template.html    # Template Jinja2
├── logs/
│   ├── runs/           # Log esecuzioni successful
│   └── errors/         # Log errori
├── requirements.txt    # Dipendenze Python
└── USAGE.md           # Questo file
```

---

## 🔧 Pipeline Automatica

Il sistema esegue automaticamente:

1. **Ricerca file** → Identifica file politica e trend in `data/daily/`
2. **Parsing** → Estrae notizie e trending topics dai markdown
3. **Categorizzazione** → Assegna le 16 categorie del blog a ogni item
4. **Sentiment Analysis** → Analizza il sentiment (positivo/negativo/neutro/polarizzato)
5. **HTML Generation** → Renderizza template con design scuro elegante
6. **Salvataggio** → Salva report in `reports/`
7. **Archiviazione** → Sposta file processati in `data/processed/`
8. **Logging** → Salva log JSON in `logs/runs/`

---

## 📊 Output

### Report HTML
- Design scuro professionale
- Hero section con data e mood pills
- Stats bar (totale topics, categorie, sentiment, polarizzazione)
- Sezioni per categoria con items organizzati
- Tag sentiment colorati
- Hashtags visualizzati
- Fonti delle notizie
- Insight sociologici automatici
- Footer con timestamp

### Log JSON
Ogni esecuzione salva un log dettagliato in `logs/runs/run_YYYY-MM-DD_HHMMSS.json`:
```json
{
  "start_time": "...",
  "end_time": "...",
  "duration_seconds": 12.45,
  "steps": {
    "find_files": {...},
    "parse": {...},
    "categorize": {...},
    "sentiment": {...},
    "generate_html": {...},
    "save_report": {...},
    "move_files": {...}
  },
  "success": true
}
```

---

## ⚙️ Configurazione

### Settings (`config/settings.yaml`)

Modifica le impostazioni generali:
- `categorization.min_keyword_match`: Minimo keyword per assegnare categoria (default: 1)
- `categorization.multi_category`: Permetti categorie secondarie (default: true)
- `sentiment.neutral_threshold`: Soglia per sentiment neutro (default: 0.2)
- `logging.level`: Livello di logging (DEBUG, INFO, WARNING, ERROR)

### Categorie (`config/categories.json`)

Le 16 categorie del blog con:
- Keywords per matching automatico
- Hashtag patterns
- Account tipici
- Sentiment default
- Priorità

### Sentiment Rules (`config/sentiment_rules.json`)

Regole per l'analisi sentiment in italiano:
- Parole positive/negative
- Intensificatori
- Negatori
- Indicatori di polarizzazione
- Emoji sentiment
- Slang social italiano

---

## 🔍 Debugging

### Log dettagliati

I log vengono salvati in:
- `logs/runs/generate_report_YYYY-MM-DD_HHMMSS.log` (esecuzione corrente)
- `logs/runs/run_YYYY-MM-DD_HHMMSS.json` (summary JSON)
- `logs/errors/error_YYYY-MM-DD_HHMMSS.json` (in caso di errori)

### Test singoli moduli

Ogni modulo può essere testato singolarmente:

```bash
# Test parser
python scripts/parser.py

# Test categorizer
python scripts/categorizer.py

# Test sentiment analyzer
python scripts/sentiment_analyzer.py

# Test template engine
python scripts/template_engine.py
```

---

## 📝 Note

### Privacy
- I file di configurazione, script e dati rimangono **privati** (`.gitignore`)
- Solo i **report HTML** finali sono pubblici (repository GitHub)

### File processati
I file markdown processati vengono automaticamente spostati in `data/processed/` con timestamp:
```
nome_file_2026-01-12_150322.md
```

### Formato file markdown
Il parser si aspetta file markdown strutturati da Perplexity con:
- **Politica**: Sezioni H2/H3 con notizie
- **Trend**: Sezione "## 1. I 10 argomenti più discussi" + dettagli "### 2.X"

---

## 🆘 Troubleshooting

### "Nessun file da processare"
✅ Verifica che ci siano file `.md` in `data/daily/`

### "Jinja2 non installato"
✅ Esegui: `pip install -r requirements.txt`

### "File non riconosciuto"
✅ Assicurati che i file contengano le keyword corrette:
- Politica: "agenzie", "ANSA", "governo", "ministro"
- Trend: "trend", "Twitter", "hashtag", "discussi"

### Report vuoto o incompleto
✅ Controlla i log in `logs/runs/` per dettagli
✅ Verifica formato markdown dei file input

---

## 📧 Supporto

Per problemi o domande, consulta i log di esecuzione o il codice sorgente commentato.

---

**Versione**: 1.0
**Data**: Gennaio 2026
**Sistema**: Python 3.8+
