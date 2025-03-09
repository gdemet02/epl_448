import pandas as pd
import re

# Φορτώνουμε το αρχείο CSV με τις τιμές που έχουν αποθηκευτεί.
df = pd.read_csv('updated_house_prices.csv')  # Προσαρμόστε το μονοπάτι του αρχείου αν είναι απαραίτητο

# Συνάρτηση για να αφαιρούμε τα κόμματα και τις τελείες και να μετατρέπουμε τις μονάδες σε sqft
def convert_super_area(area):
    # Εξασφαλίζουμε ότι η τιμή είναι σε μορφή string
    area = str(area).replace(',', '').replace('.', '')  # Αφαιρούμε κόμματα και τελείες

    # Αν η μονάδα είναι sqm, μετατρέπουμε σε sqft
    if 'sqm' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 10.7639  # sqm -> sqft
    # Αν η μονάδα είναι sqyrd, μετατρέπουμε σε sqft
    elif 'sqyrd' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 9  # sqyrd -> sqft
    # Αν η μονάδα είναι marla, μετατρέπουμε σε sqft
    elif 'marla' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 272.25  # marla -> sqft
    # Αν η μονάδα είναι kanal, μετατρέπουμε σε sqft
    elif 'kanal' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 5445  # kanal -> sqft
    # Αν η μονάδα είναι ground, μετατρέπουμε σε sqft
    elif 'ground' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 2400  # ground -> sqft
    # Αν η μονάδα είναι biswa, μετατρέπουμε σε sqft
    elif 'biswa' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 450  # biswa -> sqft
    # Αν η μονάδα είναι aankadam, μετατρέπουμε σε sqft (αν δεν γνωρίζουμε ακριβώς την αντιστοιχία, βάζουμε 1 ή τροποποιούμε αργότερα)
    elif 'aankadam' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 1  # Στην περίπτωση που δεν ξέρουμε την αντιστοιχία
    # Αν η μονάδα είναι acre, μετατρέπουμε σε sqft
    elif 'acre' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 43560  # acre -> sqft
    # Αν η μονάδα είναι hectare, μετατρέπουμε σε sqft
    elif 'hectare' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 107639.104  # hectare -> sqft
    # Αν η μονάδα είναι cent, μετατρέπουμε σε sqft
    elif 'cent' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))
        return area_value * 435.6  # cent -> sqft
    # Αν η μονάδα είναι ήδη sqft ή κάτι άλλο
    elif 'sqft' in area:
        area_value = float(re.sub(r'[^\d.]', '', area))  # Αφαιρούμε οποιαδήποτε μη αριθμητικά στοιχεία
        return area_value
    else:
        # Επιστρέφουμε τον αριθμό αν δεν υπάρχουν μονάδες
        return float(area)

# Εφαρμόζουμε τη συνάρτηση στην στήλη 'Super Area'
df['Super Area'] = df['Super Area'].apply(convert_super_area)

# Εξάγουμε το αρχείο με τις επικαιροποιημένες τιμές.
df.to_csv('updated_house_prices.csv', index=False)

# Εμφανίζουμε τις πρώτες γραμμές για επιβεβαίωση
print(df[['Super Area']].head())

