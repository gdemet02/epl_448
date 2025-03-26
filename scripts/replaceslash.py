import pandas as pd

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Αντικαθιστούμε το "/" με ","
df['overlooking'] = df['overlooking'].replace({'/': ','}, regex=True)

# Αποθηκεύουμε το νέο αρχείο με τις αλλαγές σε μορφή CSV
df.to_csv('updated_house_prices_updated.csv', index=False)

print("Η αντικατάσταση ολοκληρώθηκε και το αρχείο αποθηκεύτηκε ως updated_house_prices_updated.csv.")
