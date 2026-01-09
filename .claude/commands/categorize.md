---
description: Categorizza i trending topics nelle 16 categorie del blog
---

# Categorize Trends

Categorizza i trending topics nelle 16 categorie del blog.

## Obiettivo

**PRIORITÀ ALTA** - Classificare ogni trending topic raccolto in una o più delle 16 categorie specifiche del blog.

## Categorie del Blog

1. Opinioni ed Editoriali
2. Politica Estera
3. Politica Interna
4. Geopolitica
5. Ambiente
6. Diritti Umani
7. Inchieste e Dossier
8. Scienza e Tecnologia
9. Società
10. Cultura e Spettacolo
11. Lifestyle e Moda
12. Cronaca Bianca
13. Cronaca Giudiziaria
14. Cronaca Nera
15. Cronaca Rosa
16. Economia e Finanza

## Task da eseguire

1. **Carica i dati**
   - Leggi il file JSON più recente da `data/raw/`
   - O specifica un file particolare se fornito

2. **Preprocessing**
   - Pulisci il testo dei tweet
   - Rimuovi URL, menzioni, caratteri speciali
   - Normalizza il testo

3. **Categorizzazione automatica**
   - Utilizza modelli NLP per la classificazione:
     - **Zero-shot classification** con transformers (consigliato: `facebook/bart-large-mnli` o modelli italiani come `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`)
     - Keyword matching per ogni categoria (vedi CLAUDE.md per esempi di keyword)
     - Sentence embeddings per similarità semantica

4. **Assegnazione categoria**
   - Per ogni trending topic:
     - Assegna categoria primaria (obbligatoria)
     - Assegna categoria secondaria se applicabile
     - Calcola confidence score (0-1)
     - Identifica le keyword rilevanti che hanno portato alla categorizzazione

5. **Validazione**
   - Flagga i topic con confidence score < 0.6 per revisione manuale
   - Genera un summary delle categorizzazioni per review

6. **Salvataggio**
   - Salva i risultati in `data/raw/categorized_trends_YYYYMMDD_HHMMSS.json`
   - Struttura JSON suggerita:
     ```json
     {
       "timestamp": "2026-01-09T15:30:00Z",
       "source_file": "trends_20260109_153000.json",
       "categorized_trends": [
         {
           "name": "#TrendingTopic",
           "primary_category": "Politica Interna",
           "secondary_category": "Opinioni ed Editoriali",
           "confidence_score": 0.85,
           "relevant_keywords": ["governo", "parlamento", "legge"],
           "needs_review": false,
           "sample_tweets": [...]
         }
       ],
       "statistics": {
         "total_trends": 50,
         "trends_by_category": {
           "Politica Interna": 12,
           "Cronaca Nera": 8,
           "Sport": 7,
           ...
         },
         "needs_review_count": 5
       }
     }
     ```

7. **Report di categorizzazione**
   - Stampa statistiche di distribuzione per categoria
   - Mostra i topic che necessitano revisione manuale
   - Salva il path del file generato

## Script da creare/usare

Se non esiste, crea `scripts/categorize_trends.py` con le funzioni necessarie.

## Tecnologie consigliate

- transformers (Hugging Face)
- sentence-transformers
- scikit-learn
- spacy (modello italiano)

## Note importanti

- La qualità della categorizzazione è fondamentale per l'utilità del report
- Investire tempo nella validazione e nel miglioramento degli algoritmi
- Alcuni topic possono appartenere a più categorie - documentare la logica
- Utilizzare modelli pre-addestrati su testi italiani quando possibile
