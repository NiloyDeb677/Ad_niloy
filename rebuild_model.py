import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('heart.csv')
y = df["target"]
X = df.drop('target',axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, Y_train)
print("Model built and trained.")

joblib.dump(clf, 'heartmodel.pkl')
print("Model saved as heartmodel.pkl.")
