import pandas as pd
import re

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Συνάρτηση για να εξάγουμε τον αριθμό από τη στήλη 'Carpet Area'
def extract_area(area):
    # Ελέγχουμε αν η τιμή είναι αλφαριθμητική
    if isinstance(area, str):
        # Εξάγουμε μόνο τον αριθμό από τη μορφή "xxx sqft"
        match = re.search(r'(\d+)', area)
        if match:
            return int(match.group(1))  # Επιστρέφουμε τον αριθμό ως ακέραιο
    return None

# Εφαρμόζουμε τη συνάρτηση στην στήλη 'Carpet Area'
df['Carpet Area'] = df['Carpet Area'].apply(extract_area)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
#print(df[['Carpet Area']].head())

