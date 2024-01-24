# Sentiment Analysis Tool


**Sentiment Analysis Tool** è un'applicazione Python con un'interfaccia grafica che consente l'analisi del sentiment su recensioni di prodotti. Utilizza tecniche di elaborazione del linguaggio naturale (NLP) per valutare l'opinione degli utenti riguardo ai prodotti, offrendo un'utile prospettiva per miglioramenti futuri.

## Descrizione

Questo repository contiene un'applicazione Python con un'interfaccia grafica per l'analisi del sentiment su recensioni di prodotti. L'app utilizza il modulo NLTK (Natural Language Toolkit) per calcolare il sentiment di frasi all'interno di documenti DOCX. Inoltre, è possibile calcolare ulteriori metriche come Precision, Recall e F1-Score, oltre all'accuratezza del sentiment previsto rispetto a un dataset di riferimento in formato Excel.

## Requisiti

Assicurati di aver installato Python 3.7 o versioni successive.

Puoi installare le dipendenze richieste eseguendo il seguente comando:

```bash
pip install transformers torch pandas nltk matplotlib python-docx

```
## Utilizzo

Esegui l'applicazione con il seguente comando:
python sentiment_analysis.py
Carica un documento DOCX contenente le recensioni dei prodotti tramite il pulsante "Sfoglia".
L'app analizzerà il sentiment delle frasi nel documento e visualizzerà i risultati nell'interfaccia grafica.
Puoi anche calcolare l'accuratezza delle previsioni del sentiment rispetto a un dataset di riferimento in formato Excel utilizzando il pulsante "Calcola Accuratezza".

## Personalizzazione

Puoi personalizzare il codice per adattarlo alle tue esigenze specifiche o modificare le soglie di classificazione del sentiment nel file sentiment_analysis.py.

## Autori
Stefano Faraldi
## Licenza

Questo progetto è distribuito con la licenza MIT. Vedi il file LICENSE per ulteriori dettagli.

Assicurati di sostituire `[Stefano Faraldi]` con il tuo nome o il nome del team di sviluppo e di includere il file di licenza corretto se diverso dalla licenza MIT.

