import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Βρίσκουμε όλες τις μοναδικές τιμές στην στήλη 'Furnishing' χωρίς τα NaN
unique_furnishing = df['Furnishing'].dropna().unique()

# Δημιουργούμε μια αντιστοίχιση τύπου επίπλωσης -> αριθμός
furnishing_mapping = {furnishing: idx + 1 for idx, furnishing in enumerate(unique_furnishing)}

# Εμφανίζουμε την αντιστοίχιση
print(furnishing_mapping)

# Ενημερώνουμε τη στήλη 'Furnishing' με τους αριθμούς, διατηρώντας τα NaN ανέπαφα
df['Furnishing'] = df['Furnishing'].map(furnishing_mapping)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['Furnishing']].head())
