# Come Attivare GitHub Pages

Segui questi passaggi per rendere i report accessibili online.

## Istruzioni Step-by-Step

### 1. Vai alle Impostazioni del Repository

1. Apri il tuo browser
2. Vai a: https://github.com/StE2808/Analisi_social
3. Clicca su **"Settings"** (icona ingranaggio in alto a destra)

### 2. Attiva GitHub Pages

1. Nel menu laterale sinistro, scorri fino a trovare **"Pages"**
2. Clicca su **"Pages"**
3. Nella sezione **"Source"**:
   - Seleziona **"Deploy from a branch"**
4. Nella sezione **"Branch"**:
   - Seleziona **"main"** dal dropdown
   - Seleziona **"/ (root)"** come cartella
   - Clicca su **"Save"**

### 3. Attendi il Deployment

1. GitHub inizierà automaticamente a costruire il sito
2. Dopo 1-2 minuti, ricarica la pagina Settings > Pages
3. Vedrai un box verde con il messaggio:
   ```
   ✓ Your site is live at https://ste2808.github.io/Analisi_social/
   ```

### 4. Accedi al Sito

Il tuo sito sarà disponibile a:

**🌐 https://ste2808.github.io/Analisi_social/**

- **Landing page**: https://ste2808.github.io/Analisi_social/
- **Report 9 Gen**: https://ste2808.github.io/Analisi_social/reports/archive/report_20260109.html

## Verifica

Una volta attivato, dovresti vedere:

1. La landing page elegante con il logo "Analisi Social"
2. La card del report del 9 gennaio 2026
3. I link a GitHub e alla documentazione funzionanti

## Troubleshooting

### Il sito non si carica

- Attendi 2-3 minuti dopo l'attivazione
- Svuota la cache del browser (Ctrl+Shift+R o Cmd+Shift+R)
- Verifica che il branch selezionato sia "main" e la cartella "/ (root)"

### Errore 404

- Controlla che index.html sia nella root del repository
- Verifica che il commit sia stato pushato correttamente
- Vai su Actions tab per vedere se il deployment ha avuto successo

### Il CSS non si carica

- I CSS sono embedded nell'HTML, quindi dovrebbe funzionare
- Verifica la console del browser (F12) per eventuali errori

## Prossimi Report

Ogni volta che pubblichi un nuovo report:

1. Genera il report HTML con `python scripts/generate_report.py`
2. Aggiorna `index.html` per includere la nuova card
3. Fai commit e push
4. GitHub Pages aggiornerà automaticamente il sito in 1-2 minuti

## Custom Domain (Opzionale)

Se vuoi usare un dominio personalizzato (es. `analisi.tuodominio.com`):

1. Nelle impostazioni Pages, troverai la sezione "Custom domain"
2. Inserisci il tuo dominio
3. Configura il DNS del tuo provider con un CNAME record

## Note

- GitHub Pages è **gratuito** per repository pubblici
- Aggiornamenti automatici ad ogni push su main
- Supporta HTTPS by default
- Nessun server da gestire

---

Una volta attivato, condividi il link: **https://ste2808.github.io/Analisi_social/**
