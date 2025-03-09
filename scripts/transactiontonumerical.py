import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Βρίσκουμε όλες τις μοναδικές τιμές στην στήλη 'Transaction' χωρίς τα NaN
unique_transactions = df['Transaction'].dropna().unique()

# Δημιουργούμε μια αντιστοίχιση τύπου συναλλαγής -> αριθμός
transaction_mapping = {transaction: idx + 1 for idx, transaction in enumerate(unique_transactions)}

# Εμφανίζουμε την αντιστοίχιση
print(transaction_mapping)

# Ενημερώνουμε τη στήλη 'Transaction' με τους αριθμούς, διατηρώντας τα NaN ανέπαφα
df['Transaction'] = df['Transaction'].map(transaction_mapping)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['Transaction']].head())
