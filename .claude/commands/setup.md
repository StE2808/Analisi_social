---
description: Inizializza struttura progetto Analisi_social
---

Crea la struttura del progetto:

1. Crea le seguenti directory se non esistono:
   - `data/raw/` (cartella per dati grezzi dei trend)
   - `reports/` (cartella per i report HTML generati)
   - `reports/archive/` (storico report più vecchi)

2. Crea un file `.gitignore` nella root se non esiste con questo contenuto:
   ```
   .DS_Store
   __pycache__/
   *.pyc
   *.pyo
   .env
   .venv/
   venv/
   *.log
   ```

3. Inizializza git se non presente:
   ```bash
   git init
   ```

4. Conferma la creazione della struttura mostrando l'albero delle directory create.
