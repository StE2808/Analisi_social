---
description: Genera un report HTML interattivo strutturato per categorie
---

# Create Report

Genera un report HTML interattivo e visualmente accattivante strutturato per categorie.

## Obiettivo

Creare un report HTML completo che presenti tutti i dati e le analisi in modo chiaro, interattivo e organizzato per categoria del blog.

## IMPORTANTE: Template Grafico

**Usa SEMPRE il template in `templates/report_template.html` come base grafica per tutti i report.**

Il template fornisce uno stile editoriale elegante e professionale con:
- Design dark mode con palette sofisticata (nero profondo, oro miele, rosso tensione)
- Typography premium (Playfair Display + Source Sans Pro)
- Hero section full-screen impattante
- Card system per categorie con gradient accent
- Sentiment tags semantici (indignato, critico, preoccupato, entusiasta, etc.)
- Barre di rilevanza visuali
- Layout responsive mobile-first

**Workflow di utilizzo:**
1. Leggi il template da `templates/report_template.html`
2. Sostituisci i placeholder `{{...}}` con i dati reali dall'analisi
3. Ripeti le sezioni template per ogni categoria
4. Mantieni la struttura e lo stile del template

**Placeholder principali:**
- `{{DATA}}` - Data del report (es. "9 Gennaio 2026")
- `{{TITOLO}}` - Titolo hero (es. "Trend Italia")
- `{{SOTTOTITOLO}}` - Sottotitolo descrittivo
- `{{MOOD_PILLS}}` - Pills di mood (es. "TESO", "DIVISO", "RESILIENTE")
- `{{NUMERO}}` - Numero sezione
- `{{NOME_CATEGORIA}}` - Nome categoria
- `{{CLASSE_CATEGORIA}}` - Classe CSS categoria (politica, sport, intrattenimento, geopolitica, sentiment)
- `{{NOME_TREND}}` - Nome del trending topic
- `{{SINTESI}}` - Sintesi editoriale
- `{{SENTIMENT_TAGS}}` - Tags sentiment (usa classi: sentiment-indignato, sentiment-critico, etc.)
- `{{RILEVANZA_CLASSE}}` - Classe rilevanza (altissima, alta, media-alta, media)
- `{{INSIGHT_BLOCKS}}` - Blocchi insight

**NON modificare lo stile CSS del template.** Usa solo i placeholder per personalizzare i contenuti.

## REGOLE DI INPUT

Il comando accetta tre modalità di input diverse, riconoscibili da marcatori specifici:

### Modalità 1: Solo Trend X (Social Media)

**Input:** Dati preceduti da `=== TREND X ===`

**Output:** Report con sezioni:
- Hero con mood pills social
- **Politica & Geopolitica** (card-politica)
- **Sport & Intrattenimento** (card-sport / card-intrattenimento)
- **Sentiment Analysis** (card-sentiment)
- **Insight Chiave** (insight-section)

**Esempio input:**
```
=== TREND X ===
Trending topics:
- #MilanJuve: 150K tweet, sentiment polemico
- Meloni: 80K tweet, politica
...
```

### Modalità 2: Solo Notizie Agenzie

**Input:** Dati preceduti da `=== NOTIZIE AGENZIE ===`

**Output:** Report con sezione:
- Hero con mood pills editoriale
- **Notizie Agenzie Stampa** (card-agenzie, gradient arancione)
  - Tabella: Titolo | Fonte | Sintesi | Categoria
  - Badge con conteggio notizie per categoria
  - Filtro per fonte (ANSA, Reuters, AGI, etc.)

**Esempio input:**
```
=== NOTIZIE AGENZIE ===
1. Titolo: Accordo UE-Mercosur
   Fonte: ANSA
   Sintesi: ...
   Categoria: Economia
...
```

**CSS per card agenzie:**
```css
.card-agenzie::before {
    background: linear-gradient(90deg, #ff8c42, #ff6b35);
}
```

### Modalità 3: Report Completo (Trend + Notizie)

**Input:** Entrambi i marcatori presenti

**Output:** Report con TUTTE le sezioni delle modalità 1 e 2, PLUS:
- **Correlazioni Social-News** (sezione speciale, card-correlazioni)
  - Evidenzia collegamenti tra trend virali X e notizie agenzie
  - Tabella: Trend X | Notizia Correlata | Tipo Correlazione | Spiegazione
  - Tipi: CAUSA (news → trend), EFFETTO (trend → news), AMPLIFICAZIONE

**Esempio input:**
```
=== TREND X ===
[dati trend]

=== NOTIZIE AGENZIE ===
[dati news]
```

**CSS per card correlazioni:**
```css
.card-correlazioni::before {
    background: linear-gradient(90deg, #9b59b6, #8e44ad);
}
```

**Esempio correlazione:**
| Trend X | Notizia | Tipo | Spiegazione |
|---------|---------|------|-------------|
| #Groenlandia (50K) | Reuters: Trump rivendica Groenlandia | CAUSA | Notizia Reuters genera discussione virale su X |
| Meloni (80K) | ANSA: Conferenza stampa premier | AMPLIFICAZIONE | Notizia amplificata da dibattito politico online |

### Rilevamento Automatico Modalità

```python
def detect_mode(input_text):
    has_trends = "=== TREND X ===" in input_text
    has_news = "=== NOTIZIE AGENZIE ===" in input_text

    if has_trends and has_news:
        return "COMPLETO"  # Modalità 3
    elif has_trends:
        return "SOCIAL"    # Modalità 1
    elif has_news:
        return "EDITORIALE"  # Modalità 2
    else:
        # Fallback: tenta di classificare dal contenuto
        if "tweet" in input_text or "trending" in input_text:
            return "SOCIAL"
        else:
            return "EDITORIALE"
```

### Gestione Dati Mancanti

- Se input non ha marcatori → Interpreta come modalità editoriale (default)
- Se sezione vuota → Genera placeholder "Nessun dato disponibile"
- Se correlazioni non identificabili → Sezione correlazioni opzionale

## Task da eseguire

1. **Carica tutti i dati**
   - Dati grezzi categorizzati
   - Risultati sentiment analysis
   - Insight sociologici
   - Eventuali dati storici per confronti

2. **Struttura del Report HTML**

   Il report deve includere le seguenti sezioni in ordine:

   ### A. Header e Metadata
   - Titolo: "Report Trending Topics X Italia - [DATA]"
   - Data e ora della raccolta
   - Link al progetto GitHub
   - Disclaimer etico

   ### B. Executive Summary
   - Overview dei dati raccolti (numero di trend, timeframe)
   - Distribuzione percentuale per categoria (grafico a torta/barre)
   - Top 3 categorie dominanti
   - Sentiment generale
   - Highlight principali (3-5 punti)

   ### C. Dashboard Categorie
   - **Grafico a torta interattivo**: Distribuzione dei trend per categoria
   - **Grafico a barre**: Top 10 categorie per numero di trend
   - **Heatmap**: Intensità dei trend per categoria nel tempo (se dati disponibili)
   - Filtri interattivi per esplorare i dati

   ### D. Top Trending Topics per Categoria
   - Sezione dedicata per ogni categoria rilevante (almeno 5 trend)
   - Per ogni categoria:
     - Titolo categoria con icona
     - Lista dei top trending topics:
       - Nome del topic (linkabile a Twitter)
       - Volume di tweet
       - Sentiment score e distribuzione
       - Breve descrizione/contesto
       - Top keywords
     - Grafico sentiment specifico per la categoria

   ### E. Analisi del Sentiment per Categoria
   - **Grafico comparativo** del sentiment medio per categoria
   - **Box plot** della distribuzione sentiment per categoria
   - **Scatter plot**: Sentiment vs Volume per topic
   - Tabella delle categorie più positive/negative/polarizzate
   - Analisi testuale dei pattern sentiment emergenti

   ### F. Insight Sociologici
   - Organizzati per categoria e tema:
     - **Polarizzazione** (Politica Interna, Geopolitica, Società)
     - **Trend Emergenti** per categoria
     - **Network Analysis** con visualizzazione grafo per categoria
     - **Dinamiche Temporali** (grafici timeline per categoria)
     - **Cross-Category Analysis** con diagramma di Sankey
     - **Event Detection** categorizzato
   - Ogni insight con:
     - Visualizzazione appropriata
     - Spiegazione testuale
     - Implicazioni e contesto

   ### G. Timeline dei Trend
   - Grafico temporale interattivo (se dati disponibili)
   - Filtri per categoria
   - Marcatori per eventi significativi
   - Slider temporale

   ### H. Network di Influencer
   - Visualizzazione grafo interattivo (D3.js o Plotly)
   - Segmentato per categoria
   - Top 20 influencer per engagement
   - Community detection

   ### I. Analisi Cross-Category
   - Diagramma di Venn/Sankey per overlap tra categorie
   - Topic multi-categoria evidenziati
   - Matrice di correlazione categorie

   ### J. Conclusioni e Raccomandazioni
   - Summary degli insight principali
   - Raccomandazioni specifiche per categoria rilevanti
   - Pattern da monitorare
   - Prossimi step suggeriti

   ### K. Metodologia e Note Tecniche
   - Descrizione dei metodi di raccolta dati
   - Algoritmi di categorizzazione utilizzati
   - Modelli di sentiment analysis
   - Limitazioni e disclaimer
   - Link alle risorse e documentazione

3. **Design e UX**
   - **Responsive design**: Funzionale su desktop, tablet, mobile
   - **Color scheme**: Coerente e professionale
     - Colori distinti per ogni categoria
     - Palette per sentiment (verde=pos, rosso=neg, grigio=neu)
   - **Typography**: Leggibile e gerarchica
   - **Navigation**:
     - Sticky header con menu
     - Table of contents laterale
     - Smooth scroll tra sezioni
     - Bottone "torna su"
   - **Interattività**:
     - Grafici interattivi con hover/tooltip
     - Filtri e controlli
     - Accordion/collapse per sezioni lunghe
     - Modal per dettagli approfonditi

4. **Visualizzazioni**
   - Utilizzare librerie JavaScript moderne:
     - **Chart.js**: Grafici base (torta, barre, linee)
     - **Plotly.js**: Grafici avanzati e interattivi
     - **D3.js**: Visualizzazioni custom (network graph, Sankey)
   - Tutte le visualizzazioni devono:
     - Essere responsive
     - Avere tooltips informativi
     - Supportare export come immagine (PNG/SVG)
     - Essere accessibili (alt text, aria labels)

5. **Template HTML**
   - Utilizzare Jinja2 per il templating
   - Creare template riutilizzabile in `templates/report_template.html`
   - Separare CSS in file esterno o includere in `<style>`
   - JavaScript può essere inline o esterno

6. **Generazione e Salvataggio**
   - Genera l'HTML compilando il template con i dati
   - Salva in `reports/archive/report_YYYYMMDD.html`
   - Il file deve essere standalone (CSS/JS inline o embedded)
   - Opzionale: genera anche PDF via wkhtmltopdf o Playwright

7. **Quality Check**
   - Valida l'HTML (W3C validator)
   - Testa su diversi browser
   - Verifica responsive su mobile
   - Controlla che tutti i link funzionino
   - Verifica accessibilità (WCAG 2.1 AA)
   - Performance: pagina deve caricare in < 3 secondi

8. **Output**
   - Stampa il path del report generato
   - Opzionale: apri automaticamente nel browser
   - Log eventuali warning o problemi

## Script da creare/usare

Se non esiste, crea `scripts/generate_report.py` con le funzioni necessarie.

## Tecnologie consigliate

### Python
- jinja2 per templating
- pandas per manipolazione dati
- plotly per grafici esportabili in HTML
- json per caricamento dati

### Frontend (nel template HTML)
- HTML5 semantic markup
- CSS3 con Flexbox/Grid
- JavaScript ES6+
- Chart.js o Plotly.js
- D3.js per grafici avanzati
- Bootstrap o Tailwind per layout responsive (opzionale)

## Template HTML Base

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Trending Topics X Italia - {{ date }}</title>
    <style>
        /* CSS here or link to external */
    </style>
</head>
<body>
    <header>
        <nav><!-- Navigation menu --></nav>
    </header>

    <main>
        <section id="executive-summary">
            <!-- Executive Summary -->
        </section>

        <section id="category-dashboard">
            <!-- Dashboard Categorie -->
        </section>

        <section id="trending-by-category">
            <!-- Top Trending per Categoria -->
        </section>

        <section id="sentiment-analysis">
            <!-- Analisi Sentiment -->
        </section>

        <section id="insights">
            <!-- Insight Sociologici -->
        </section>

        <!-- More sections... -->
    </main>

    <footer>
        <!-- Metodologia, Credits, Links -->
    </footer>

    <script>
        // JavaScript for interactivity
    </script>
</body>
</html>
```

## Note importanti

- Il report deve essere **standalone** - tutto incluso in un file HTML
- La categorizzazione è il filo conduttore - ogni sezione deve riferirsi alle categorie
- L'UX è fondamentale - l'utente deve poter navigare facilmente
- Le visualizzazioni devono raccontare una storia, non solo mostrare dati
- Accessibilità e performance sono requisiti, non optional
- Il report deve essere professionale e presentabile pubblicamente
