# Sentiment Analysis Tool

**Sentiment Analysis Tool** è un'applicazione Python con un'interfaccia grafica che consente l'analisi del sentiment su recensioni di prodotti. Utilizza tecniche di elaborazione del linguaggio naturale (NLP) per valutare l'opinione degli utenti riguardo ai prodotti, offrendo un'utile prospettiva per miglioramenti futuri.

## Descrizione

Questo repository contiene un'applicazione Python con un'interfaccia grafica per l'analisi del sentiment su recensioni di prodotti. L'app utilizza il modulo NLTK (Natural Language Toolkit) per calcolare il sentiment di frasi all'interno di documenti DOCX. Inoltre, è possibile calcolare ulteriori metriche come Precision, Recall e F1-Score, oltre all'accuratezza del sentiment previsto rispetto a un dataset di riferimento in formato Excel.

## Requisiti
Questo progetto richiede Python 3.7 o versioni successive. Assicurati di avere le seguenti librerie Python installate:

python-docx: Per la lettura di file Word (.docx).
matplotlib: Per la creazione di grafici e visualizzazioni.
nltk: Per l'analisi del sentiment.
pandas: Per la manipolazione e l'analisi dei dati.
scikit-learn: Per il calcolo di metriche come precisione, richiamo e punteggio F1.
openpyxl: Come dipendenza per pandas per leggere i file Excel (.xlsx).
La libreria tkinter è anche necessaria per l'interfaccia grafica, ma è generalmente inclusa nelle installazioni standard di Python.

Installazione delle Dipendenze

Puoi installare tutte le dipendenze richieste eseguendo il seguente comando nel tuo ambiente Python:
pip install python-docx matplotlib nltk pandas scikit-learn openpyxl
Configurazione di NLTK

Dopo aver installato nltk, è necessario scaricare il set di dati vader_lexicon, utilizzato dal SentimentIntensityAnalyzer. Esegui il seguente comando Python per completare questa configurazione:
import nltk
nltk.download('vader_lexicon')


```
## Utilizzo

Esegui l'applicazione con il seguente comando:

python sentiment_analysis.py
Segui questi passaggi per utilizzare l'applicazione:

Carica un documento DOCX contenente le recensioni dei prodotti tramite il pulsante "Sfoglia".
L'app analizzerà il sentiment delle frasi nel documento e visualizzerà i risultati nell'interfaccia grafica.
Puoi anche calcolare l'accuratezza delle previsioni del sentiment rispetto a un dataset di riferimento in formato Excel utilizzando il pulsante "Calcola Accuratezza".
Inoltre, è possibile calcolare ulteriori metriche come Precision, Recall e F1-Score per valutare le prestazioni dell'analisi del sentiment.

## Personalizzazione

Puoi personalizzare il codice per adattarlo alle tue esigenze specifiche o modificare le soglie di classificazione del sentiment nel file sentiment_analysis.py.

## Autori
Stefano Faraldi
## Licenza

Questo progetto è distribuito con la licenza MIT. Vedi il file LICENSE per ulteriori dettagli.

Assicurati di sostituire `[Stefano Faraldi]` con il tuo nome o il nome del team di sviluppo e di includere il file di licenza corretto se diverso dalla licenza MIT.

