import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Βρίσκουμε όλες τις μοναδικές τιμές στην στήλη 'Facing' χωρίς τα NaN
unique_facing = df['facing'].dropna().unique()

# Δημιουργούμε μια αντιστοίχιση τύπου κατεύθυνσης -> αριθμός
facing_mapping = {facing: idx + 1 for idx, facing in enumerate(unique_facing)}

# Εμφανίζουμε την αντιστοίχιση
print(facing_mapping)

# Ενημερώνουμε τη στήλη 'Facing' με τους αριθμούς, διατηρώντας τα NaN ανέπαφα
df['facing'] = df['facing'].map(facing_mapping)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['facing']].head())
