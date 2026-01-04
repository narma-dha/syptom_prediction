# train_model.py
import pandas as pd
import os
import glob
import json
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATA_DIR = "data"     # All CSV files must be inside /data folder
MODEL_DIR = "."       # Save model in current folder

# 1. Load all CSV files
files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
if not files:
    raise SystemExit("❌ No CSV files found in data/ folder!")

print("📌 Found CSV files:", files)

dfs = [pd.read_csv(f) for f in files]

# 2. Clean columns
for i, df in enumerate(dfs):
    df.columns = [c.strip().lower() for c in df.columns]
    dfs[i] = df

# 3. Merge all CSV files
df = pd.concat(dfs, ignore_index=True)

# 4. Separate symptom columns
if "disease" not in df.columns:
    raise SystemExit("❌ Your CSV MUST contain a 'disease' column!")

symptom_cols = [c for c in df.columns if c != "disease"]

print("\n🩺 Using symptom columns:")
print(symptom_cols)

# Convert symptoms to integer 0/1
df[symptom_cols] = df[symptom_cols].fillna(0).astype(int)

# 5. Features & labels
X = df[symptom_cols]
y = df["disease"]

# 6. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 7. Train Model
print("\n🔨 Training model...")
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 8. Evaluate
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)

print("\n🎯 Model Accuracy:", accuracy)

# 9. Save model + symptom index
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("symptom_index.json", "w") as f:
    json.dump(symptom_cols, f, indent=2)

print("\n✅ Training complete!")
print("📁 model.pkl saved")
print("📁 symptom_index.json saved")
