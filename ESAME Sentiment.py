import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, scrolledtext
import docx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# Inizializza l'analizzatore di sentiment di NLTK
sia = SentimentIntensityAnalyzer()

# Definisci le soglie per classificare le frasi come "Positive", "Neutral" o "Negative"
positive_threshold = 0.05
negative_threshold = -0.05

# Variabili globali per memorizzare il testo da analizzare e le previsioni di sentiment
current_text = ""
current_predictions = []

# Funzione per caricare un file Word e analizzare il suo contenuto
def load_file():
    global current_text, current_predictions
    file_path = filedialog.askopenfilename(
        filetypes=[("Word files", "*.docx")],
        title="Scegli un documento"
    )
    if file_path:
        try:
            # Leggi il testo dal file Word
            doc = docx.Document(file_path)
            text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, text)
            analyze_sentiment(text)
            current_text = text
            # Analizza e memorizza le previsioni di sentiment per ogni frase nel testo
            current_predictions = [classify_sentiment(sia.polarity_scores(sentence)['compound']) for sentence in text.split('\n') if sentence.strip()]
        except Exception as e:
            # Gestisci eventuali errori durante la lettura del file
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, f"Errore nella lettura del file: {e}")

# Funzione per classificare il sentiment sulla base del punteggio del sentiment
def classify_sentiment(compound_score):
    if compound_score > positive_threshold:
        return 'Positive'
    elif compound_score < negative_threshold:
        return 'Negative'
    else:
        return 'Neutral'

# Funzione per analizzare il sentiment del testo e visualizzare i risultati
def analyze_sentiment(text):
    for item in table.get_children():
        table.delete(item)

    sentences = text.split('\n')
    positive, neutral, negative = 0, 0, 0

    for i, sentence in enumerate(sentences):
        if sentence.strip():
            sentiment = sia.polarity_scores(sentence)
            esito = classify_sentiment(sentiment['compound'])
            if esito == 'Positive': positive += 1
            elif esito == 'Neutral': neutral += 1
            elif esito == 'Negative': negative += 1
            table.insert("", "end", values=(i + 1, sentence, sentiment['compound'], esito))

    total = positive + neutral + negative
    positive_pct = (positive / total * 100) if positive else 0
    neutral_pct = (neutral / total * 100) if neutral else 0
    negative_pct = (negative / total * 100) if negative else 0

    sentiment_result.config(text=f"Sentiment: {positive_pct:.2f}% Positive, {neutral_pct:.2f}% Neutral, {negative_pct:.2f}% Negative")
    update_graph(positive_pct, neutral_pct, negative_pct)

# Funzione per aggiornare il grafico a torta dei risultati del sentiment
def update_graph(positive_pct, neutral_pct, negative_pct):
    plt.clf()
    labels = []
    sizes = []
    colors = []

    if positive_pct > 0:
        labels.append('Positive')
        sizes.append(positive_pct)
        colors.append("#45d927")
    if neutral_pct > 0:
        labels.append('Neutral')
        sizes.append(neutral_pct)
        colors.append("#c7ccc6")
    if negative_pct > 0:
        labels.append('Negative')
        sizes.append(negative_pct)
        colors.append("#f73131")

    if sizes:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=None, colors=colors, autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '', startangle=90)
        ax.axis('equal')
        plt.legend(labels, loc="best")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    else:
        sentiment_result.config(text="Nessun dato sufficiente per il grafico")

# Funzione per calcolare l'accuratezza rispetto a un dataset di riferimento
def calculate_accuracy():
    if not current_predictions:
        accuracy_result.config(text="Carica e analizza un file DOCX prima.")
        return

    file_path = filedialog.askopenfilename(
        title="Scegli un file Excel",
        filetypes=[("Excel files", "*.xlsx")]
    )
    if file_path:
        try:
            dataset = pd.read_excel(file_path)

            if 'Text' in dataset.columns and 'Emotion' in dataset.columns:
                annotations = dataset['Emotion'].tolist()[:len(current_predictions)]

                correct_predictions = sum(p == a for p, a in zip(current_predictions, annotations))

                # Calcola l'accuratezza
                accuracy = correct_predictions / len(annotations) if annotations else 0

                accuracy_result.config(text=f"Accuratezza: {accuracy:.2f}")
            else:
                accuracy_result.config(text="Il dataset Excel non ha le colonne necessarie.")
        except Exception as e:
            accuracy_result.config(text=f"Errore nella lettura del file: {str(e)}")
    else:
        accuracy_result.config(text="Nessun file Excel selezionato")

# Funzione per calcolare le metriche (Precision, Recall, F1-Score) rispetto a un dataset di riferimento
def calculate_metrics():
    if not current_predictions:
        metrics_result.config(text="Carica e analizza un file DOCX prima.")
        return

    file_path = filedialog.askopenfilename(
        title="Scegli un file Excel",
        filetypes=[("Excel files", "*.xlsx")]
    )
    if file_path:
        try:
            dataset = pd.read_excel(file_path)

            if 'Text' in dataset.columns and 'Emotion' in dataset.columns:
                annotations = dataset['Emotion'].tolist()[:len(current_predictions)]

                # Calcola Precision, Recall e F1-Score
                precision = precision_score(annotations, current_predictions, average='weighted')
                recall = recall_score(annotations, current_predictions, average='weighted')
                f1 = f1_score(annotations, current_predictions, average='weighted')

                confusion = confusion_matrix(annotations, current_predictions)

                # Visualizza le metriche nella nuova area
                metrics_result.config(text=f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1-Score: {f1:.2f}")
                print("Confusion Matrix:")
                print(confusion)
            else:
                metrics_result.config(text="Il dataset Excel non ha le colonne necessarie.")
        except Exception as e:
            metrics_result.config(text=f"Errore nella lettura del file: {str(e)}")
    else:
        metrics_result.config(text="Nessun file Excel selezionato")

# Creazione della finestra principale
root = tk.Tk()
root.title("Sentiment Analysis")
root.geometry("800x600")

# Pulsante per caricare un file
open_file_btn = tk.Button(root, text="Sfoglia...", command=load_file)
open_file_btn.pack()

# Frame per l'area di testo
text_area_frame = ttk.Frame(root)
text_area_frame.pack(pady=10)

# TextArea per il testo
text_area = scrolledtext.ScrolledText(text_area_frame, wrap=tk.WORD, height=10, width=50)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Etichetta per il risultato del sentiment
sentiment_result = tk.Label(root, text="")
sentiment_result.pack()

# Frame per la tabella
table_frame = ttk.Frame(root)
table_frame.pack()

# Funzione per gestire la selezione nella tabella
def on_select(event):
    # Ottieni l'item selezionato
    selected_item = table.focus()

    # Ottieni i valori dell'item selezionato
    values = table.item(selected_item, 'values')

    # Controlla il valore della quarta colonna e imposta il colore di sfondo
    if values:
        fourth_column_value = values[3]
        if fourth_column_value == 'Negative':
            style.map("Treeview", background=[("selected", "#f73131")])
        elif fourth_column_value == 'Neutral':
            style.map("Treeview", background=[("selected", "#c7ccc6")])
        elif fourth_column_value == 'Positive':
            style.map("Treeview", background=[("selected", "#45d927")])

style = ttk.Style()

# Creazione della tabella
table = ttk.Treeview(table_frame, columns=("Indice", "Frase", "Valore", "Esito"))
table.heading("#1", text="Indice")
table.heading("#2", text="Frase")
table.heading("#3", text="Valore")
table.heading("#4", text="Esito")

table.column("#1", width=50)
table.column("#2", width=300)
table.column("#3", width=100)
table.column("#4", width=100)

# Scrollbar per la tabella
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")
table.configure(yscrollcommand=scrollbar.set)
table.bind('<<TreeviewSelect>>', on_select)
table.pack()

# Pulsante per calcolare l'accuratezza
accuracy_btn = tk.Button(root, text="Calcola Accuratezza", command=calculate_accuracy)
accuracy_btn.pack()

# Etichetta per il risultato dell'accuratezza
accuracy_result = tk.Label(root, text="")
accuracy_result.pack()

# Pulsante per calcolare le metriche
metrics_btn = tk.Button(root, text="Calcola Metriche", command=calculate_metrics)
metrics_btn.pack()

# Etichetta per il risultato delle metriche
metrics_result = tk.Label(root, text="")
metrics_result.pack()

# Esecuzione della finestra principale
root.mainloop()
