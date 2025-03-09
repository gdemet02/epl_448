import pandas as pd
import re
import numpy as np

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Συνάρτηση για να μετατρέψουμε τις τιμές από Lac ή Cr σε αριθμούς και να χειριστούμε την τιμή "Call for price"
def convert_amount(amount):
    # Αν η τιμή είναι "Call for price", επιστρέφουμε NaN
    if isinstance(amount, str) and "Call for Price" in amount:
        return np.nan
    
    # Έλεγχος για την περίπτωση "Lac" ή "Cr"
    match_lac = re.search(r'(\d+(\.\d+)?)\s*Lac', amount)
    match_cr = re.search(r'(\d+(\.\d+)?)\s*Cr', amount)
    
    if match_lac:
        return float(match_lac.group(1)) * 100000  # Μετατροπή από Lac σε αριθμό
    elif match_cr:
        return float(match_cr.group(1)) * 10000000  # Μετατροπή από Cr σε αριθμό
    return None

# Εφαρμόζουμε τη συνάρτηση στην στήλη 'Amount(in rupees)'
df['Amount(in rupees)'] = df['Amount(in rupees)'].apply(convert_amount)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
#print(df[['Amount(in rupees)']].head())

