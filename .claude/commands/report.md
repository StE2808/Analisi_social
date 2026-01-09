---
description: Genera report trend X Italia e pubblica su GitHub
---

# Workflow Completo per Generare Report Trend X Italia

Esegui questi passi in sequenza:

## 1. Acquisizione Dati

**Se l'utente ha incollato dati dopo questo comando**: usali direttamente.

**Altrimenti**: chiedi all'utente di incollare i dati dei trending topic (può essere testo libero, copia-incolla da X, o dati strutturati).

## 2. Salvataggio Dati Grezzi

Salva i dati forniti dall'utente in formato testo:
- **Path**: `data/raw/YYYY-MM-DD.txt` (usa la data odierna nel formato ISO)
- **Contenuto**: esattamente i dati forniti dall'utente, senza modifiche

## 3. Generazione Report HTML

Genera un report HTML professionale come **dashboard interattiva** con queste caratteristiche:

### Design e Stile
- **Tema**: scuro ed elegante (background #0f0f23, testi chiari)
- **Font**: Google Fonts
  - Titoli: `Playfair Display` (serif elegante)
  - Corpo: `Source Sans Pro` (sans-serif leggibile)
- **Layout**: responsive, mobile-first
- **Colori tema**:
  - Politica: `#e74c3c` (rosso)
  - Sport: `#27ae60` (verde)
  - Intrattenimento: `#f39c12` (oro)
  - Geopolitica: `#3498db` (blu)
  - Sentiment: `#9b59b6` (viola)

### Struttura del Report

#### Header / Hero Section
- Titolo evocativo con la data del report
- Sottotitolo che cattura l'umore nazionale
- "Mood Pills": 3-4 badge colorati con sentiment aggregato (es: "🔥 Polarizzato", "💬 Conversazionale", "⚡ Virale")

#### Sezione 1: Top Trending Topics
Tabella o griglia con i principali trend del giorno:
- Nome del trend/hashtag
- Categoria (Politica/Sport/Intrattenimento/etc.)
- Sentiment dominante (tag colorato: Positivo verde, Negativo rosso, Neutro grigio)
- Barra di rilevanza (0-100%)

#### Sezione 2: Analisi per Categoria
5 card colorate (una per categoria):
- Icona rappresentativa
- Titolo categoria
- Top 3 trend della categoria
- Breve sintesi (2-3 righe)

#### Sezione 3: Sentiment Overview
- Grafico a torta o barre con distribuzione sentiment (Positivo/Negativo/Neutro)
- Percentuali chiare
- Interpretazione testuale

#### Sezione 4: Insight del Giorno
4 blocchi di analisi sociologica sulla viralità:
1. **Dinamica Temporale**: quando i trend hanno raggiunto il picco
2. **Polarizzazione**: livello di divisione nelle conversazioni
3. **Influencer & Amplificazione**: chi ha guidato la conversazione
4. **Contesto Culturale**: correlazione con eventi esterni

Ogni insight deve essere:
- Basato sui dati forniti (o inferito intelligentemente)
- Scritto in italiano professionale ma scattante
- 3-5 righe max

#### Footer
- Data e ora di generazione del report
- Link al repository GitHub
- Versione del report

### Requisiti Tecnici
- **CSS inline**: tutto il CSS deve essere in un tag `<style>` nell'HTML
- **JavaScript inline**: eventuali interazioni in un tag `<script>` nell'HTML
- **Nessuna dipendenza esterna** tranne Google Fonts (via CDN)
- **Accessibilità**: contrasti WCAG AA, testi alternativi
- **Performance**: HTML ottimizzato, sotto 200KB

### Tono e Linguaggio
- **Lingua**: italiano
- **Stile**: professionale ma vivace, giornalistico
- **Evitare**: gergo tecnico eccessivo, tono accademico pesante
- **Preferire**: insights chiari, narrazione coinvolgente, dati concreti

## 4. Salvataggio Report

Salva il report HTML generato:
- **Path**: `reports/report_YYYY-MM-DD.html` (usa la data odierna)

## 5. Git Commit e Push

Esegui questi comandi git in sequenza:

```bash
git add data/raw/ reports/
git commit -m "📊 Report trend X Italia - YYYY-MM-DD"
git push -u origin claude/automate-italy-trend-reports-hZ4Hn
```

**Importante**: usa esattamente il branch specificato sopra.

## 6. Conferma Finale

Mostra all'utente:
- ✅ Conferma che il report è stato generato e pubblicato
- 📁 Path locale del report
- 🔗 Link GitHub al report (formato: `https://github.com/StE2808/Analisi_social/blob/claude/automate-italy-trend-reports-hZ4Hn/reports/report_YYYY-MM-DD.html`)
- 📊 Breve summary dei principali insight emersi

---

**Note**:
- Se i dati forniti sono scarni, inferisci intelligentemente i dettagli mancanti
- Creatività nel design è incoraggiata, ma mantieni la struttura base
- I report devono essere visualizzabili su GitHub direttamente (no server-side code)
