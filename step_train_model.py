
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

emails = pd.read_csv("emails_cleaned.csv")

#Ensure no NaN values in clean_text
emails['clean_text'] = emails['clean_text'].fillna('')

#features and labels
x = emails['clean_text']
y = emails['label']

#split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#convert text to vector using TF
vectorizer = TfidfVectorizer(max_features=5000)
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

#train naive bayes model
model = MultinomialNB()
model.fit(x_train_vec, y_train)

#make predictions on test set
y_pred = model.predict(x_test_vec)

#test model performance
print("----- CONFUSION MATRIX -----")
print(confusion_matrix(y_test, y_pred))
print("----- CLASSIFICATION REPORT -----")
print(classification_report(y_test, y_pred))

print("model trained successfully")