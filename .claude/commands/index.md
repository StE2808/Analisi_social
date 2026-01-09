---
description: Genera indice HTML dei report per GitHub Pages
---

# Generazione Indice Report

Crea una pagina index per navigare facilmente tutti i report generati.

## 1. Scansiona Report Disponibili

Trova tutti i file `report_*.html` in:
- `reports/` (report recenti)
- `reports/archive/` (report archiviati)

Ordina per data in modo decrescente (più recenti in alto).

## 2. Genera reports/index.html

Crea un file HTML con queste caratteristiche:

### Design
- **Stile coerente** con i report (tema scuro, Google Fonts)
- **Layout responsive**: griglia o lista adattiva
- **Tipografia**:
  - Titoli: Playfair Display
  - Corpo: Source Sans Pro

### Struttura

#### Header
- Titolo: "📊 Analisi Trend X Italia - Archivio Report"
- Sottotitolo: breve descrizione del progetto
- Stats: numero totale di report disponibili

#### Sezione Report Recenti
Lista dei report degli ultimi 7 giorni:
- Card per ogni report con:
  - Data (formato italiano: es. "9 gennaio 2026")
  - Link al report HTML
  - Badge "Nuovo" se generato nelle ultime 48 ore
  - Icona o emoji tematica

#### Sezione Report Archiviati
Lista collassabile o scrollabile dei report più vecchi:
- Raggruppati per mese/anno
- Link a ciascun report in archive/

#### Footer
- Link al repository GitHub
- Istruzioni su come generare nuovi report (riferimento ai comandi slash)
- Data ultimo aggiornamento dell'indice

### Requisiti Tecnici
- CSS e JavaScript inline (nessun file esterno tranne Google Fonts)
- Link relativi ai report (es. `./report_2026-01-09.html`)
- Navigazione keyboard-friendly
- Accessibilità WCAG AA

## 3. Salvataggio

Salva il file come: `reports/index.html`

## 4. Git Commit e Push

```bash
git add reports/index.html
git commit -m "📚 Aggiornamento indice report"
git push -u origin claude/automate-italy-trend-reports-hZ4Hn
```

## 5. Conferma Finale

Mostra all'utente:
- ✅ Indice generato con successo
- 📊 Numero di report listati (recenti + archiviati)
- 🔗 Link GitHub all'indice: `https://github.com/StE2808/Analisi_social/blob/claude/automate-italy-trend-reports-hZ4Hn/reports/index.html`
- 💡 Suggerimento: abilitare GitHub Pages per visualizzazione web diretta

---

**Nota**: L'indice facilita la navigazione di tutti i report storici e può essere usato come landing page per GitHub Pages.
