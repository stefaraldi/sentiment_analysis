# Sentiment Analysis Tool

**Sentiment Analysis Tool** è un'applicazione Python con un'interfaccia grafica che consente l'analisi del sentiment su recensioni di prodotti. Utilizza tecniche di elaborazione del linguaggio naturale (NLP) per valutare l'opinione degli utenti riguardo ai prodotti, offrendo un'utile prospettiva per miglioramenti futuri.

## Descrizione

Questo repository contiene un'applicazione Python con un'interfaccia grafica per l'analisi del sentiment su recensioni di prodotti. L'app utilizza il modulo NLTK (Natural Language Toolkit) per calcolare il sentiment di frasi all'interno di documenti DOCX. Inoltre, è possibile calcolare ulteriori metriche come Precision, Recall e F1-Score, oltre all'accuratezza del sentiment previsto rispetto a un dataset di riferimento in formato Excel.

## Requisiti

Questo progetto richiede Python 3.7 o versioni successive. Assicurati di avere le seguenti librerie Python installate:

- python-docx: Per la lettura di file Word (.docx).
- matplotlib: Per la creazione di grafici e visualizzazioni.
- nltk: Per l'analisi del sentiment.
- pandas: Per la manipolazione e l'analisi dei dati.
- scikit-learn: Per il calcolo di metriche come precisione, richiamo e punteggio F1.
- openpyxl: Come dipendenza per pandas per leggere i file Excel (.xlsx).

Installazione delle Dipendenze

Puoi installare tutte le dipendenze richieste eseguendo il seguente comando nel tuo ambiente Python:

```pip install python-docx matplotlib nltk pandas scikit-learn openpyxl``` 
<img width="750" alt="Screenshot 2024-01-25 alle 13 04 06" src="https://github.com/stefaraldi/sentiment_analysis/assets/122448165/07326d6f-d4bc-431b-b5af-00c841557804">


## Utilizzo

Segui questi passaggi per utilizzare l'applicazione:

Carica un documento DOCX contenente le recensioni dei prodotti tramite il pulsante "Sfoglia".
L'app analizzerà il sentiment delle frasi nel documento e visualizzerà i risultati nell'interfaccia grafica.
Puoi anche calcolare l'accuratezza delle previsioni del sentiment rispetto a un dataset di riferimento in formato Excel utilizzando il pulsante "Calcola Accuratezza".
Inoltre, è possibile calcolare ulteriori metriche come Precision, Recall e F1-Score per valutare le prestazioni dell'analisi del sentiment.
<img width="646" alt="Screenshot 2023-12-04 alle 19 44 48" src="https://github.com/stefaraldi/sentiment_analysis/assets/122448165/e44f5c94-65ff-4ebe-8aaf-fff00cd53374">

## Personalizzazione

Puoi personalizzare il codice per adattarlo alle tue esigenze specifiche o modificare le soglie di classificazione del sentiment nel file sentiment_analysis.py.

## Autori
Stefano Faraldi

## Licenza

Questo progetto è distribuito sotto la Licenza Apache 2.0. Questa è una licenza permissiva le cui condizioni principali richiedono la conservazione delle note di copyright e di licenza. I contributori forniscono un'espressa concessione dei diritti di brevetto. Opere, modifiche e opere di maggiore entità possono essere distribuite secondo termini differenti e senza il codice sorgente.

Per ulteriori dettagli, consulta il file LICENSE incluso in questo progetto.

