import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Βρίσκουμε όλες τις μοναδικές τοποθεσίες
unique_locations = df['location'].unique()

# Δημιουργούμε μια αντιστοίχιση τοποθεσίας -> αριθμός
location_mapping = {location: idx + 1 for idx, location in enumerate(unique_locations)}

# Εμφανίζουμε την αντιστοίχιση
print(location_mapping)

# Ενημερώνουμε τη στήλη 'location' με τους αριθμούς
df['location'] = df['location'].map(location_mapping)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['location']].head())

