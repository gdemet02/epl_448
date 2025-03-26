import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Δημιουργούμε μια συνάρτηση για να κανονικοποιήσουμε τις τιμές ταξινομώντας τα στοιχεία
def normalize_overlooking(overlooking_value):
    # Αν η τιμή είναι 'Not Available', την αφαιρούμε
    if isinstance(overlooking_value, str) and 'Not Available' in overlooking_value:
        overlooking_value = overlooking_value.replace('Not Available', '').strip(', ')  # Αφαιρούμε το 'Not Available'
    
    # Χωρίζουμε τη τιμή σε λίστα και τα ταξινομούμε
    return ', '.join(sorted(overlooking_value.split(', '))) if overlooking_value else None

# Εφαρμόζουμε την κανονικοποίηση απευθείας στη στήλη 'overlooking'
df['overlooking'] = df['overlooking'].apply(lambda x: normalize_overlooking(x) if isinstance(x, str) else x)

# Βρίσκουμε όλες τις μοναδικές τιμές στην στήλη 'overlooking' χωρίς τα NaN
unique_overlooking = df['overlooking'].dropna().unique()

# Δημιουργούμε μια αντιστοίχιση τύπου κατεύθυνσης -> αριθμός
overlooking_mapping = {overlooking: idx + 1 for idx, overlooking in enumerate(unique_overlooking)}

# Εμφανίζουμε την αντιστοίχιση
print(overlooking_mapping)

# Ενημερώνουμε τη στήλη 'overlooking' με τους αριθμούς, διατηρώντας τα NaN ανέπαφα
df['overlooking'] = df['overlooking'].map(overlooking_mapping)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['overlooking']].head())
