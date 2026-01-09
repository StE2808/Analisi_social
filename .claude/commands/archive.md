---
description: Archivia report vecchi
---

# Archiviazione Automatica Report

Esegui questi passi per archiviare i report più vecchi:

## 1. Identifica Report da Archiviare

Trova tutti i file HTML in `reports/` (esclusa la sottocartella `archive/`) che:
- Hanno più di 7 giorni rispetto alla data odierna
- Seguono il pattern `report_YYYY-MM-DD.html`

## 2. Sposta in Archive

Sposta tutti i report identificati in `reports/archive/`:
```bash
mv reports/report_YYYY-MM-DD.html reports/archive/
```

**Importante**:
- NON spostare `reports/index.html` (se esistente)
- Mantieni i nomi dei file originali
- Non cancellare nulla, solo spostare

## 3. Riepilogo Operazione

Mostra all'utente:
- Numero di report archiviati
- Lista dei file spostati con le loro date
- Se nessun file da archiviare, conferma che tutti i report sono recenti

## 4. Git Commit e Push

Se sono stati spostati file, committa le modifiche:

```bash
git add reports/
git commit -m "🗄️ Archiviazione report più vecchi di 7 giorni"
git push -u origin claude/automate-italy-trend-reports-hZ4Hn
```

## 5. Conferma Finale

Conferma all'utente:
- ✅ Operazione completata
- 📦 Numero di report archiviati
- 🔗 Link alla cartella archive su GitHub

---

**Nota**: Questo comando è utile per mantenere pulita la directory `reports/` principale, rendendo più facile trovare i report più recenti.
