import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Βρίσκουμε όλες τις μοναδικές τιμές στην στήλη 'Ownership' χωρίς τα NaN
unique_ownership = df['Ownership'].dropna().unique()

# Δημιουργούμε μια αντιστοίχιση τύπου ιδιοκτησίας -> αριθμός
ownership_mapping = {ownership: idx + 1 for idx, ownership in enumerate(unique_ownership)}

# Εμφανίζουμε την αντιστοίχιση
print(ownership_mapping)

# Ενημερώνουμε τη στήλη 'Ownership' με τους αριθμούς, διατηρώντας τα NaN ανέπαφα
df['Ownership'] = df['Ownership'].map(ownership_mapping)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['Ownership']].head())
