import pandas as pd
import re

# Φορτώνει το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Συνάρτηση για την εξαγωγή του society name από το title
def extract_society_name(title):
    # Εξάγουμε το κείμενο μετά τη λέξη "sale" ή "sale in"
    match = re.search(r"(?:sale|sale in)\s*(.*)", title)
    if match:
        society_name = match.group(1).strip()  # Αφαιρούμε τα περιττά κενά
        # Αφαιρούμε τη λέξη "in" αν υπάρχει
        society_name = re.sub(r'\bin\b', '', society_name).strip()
        return society_name
    return None

# Εφαρμόζουμε τη συνάρτηση στην στήλη 'Title' και γεμίζουμε τη στήλη 'Society'
df['Society'] = df['Title'].apply(extract_society_name)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
#print(df[['Title', 'Society']].head())

