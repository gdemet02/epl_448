import pandas as pd

# Φορτώνουμε το αρχείο CSV
df = pd.read_csv('updated_house_prices.csv')  # Ενημερώστε το μονοπάτι του αρχείου

# Ελέγχουμε τις πρώτες γραμμές του αρχείου για να δούμε τη δομή των δεδομένων
print("Πρώτες γραμμές του αρχείου:")
print(df.head())

# Μετατρέπουμε τις στήλες σε αριθμητικές τιμές (και τα NaN να παραμείνουν αν υπάρχουν)
df['Super Area'] = pd.to_numeric(df['Super Area'], errors='coerce')
df['Carpet Area'] = pd.to_numeric(df['Carpet Area'], errors='coerce')

# Δημιουργούμε τη νέα στήλη "Total Area", υπολογίζοντας το Super Area και Carpet Area με NaN ως 0
df['Total Area'] = df['Super Area'].fillna(0) + df['Carpet Area'].fillna(0)

# Εξάγουμε το αρχείο με την νέα στήλη
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print("\nΠρώτες γραμμές με την νέα στήλη 'Total Area':")
print(df[['Super Area', 'Carpet Area', 'Total Area']].head())
