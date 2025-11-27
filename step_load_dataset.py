import pandas as pd

#loading dataset
phishing = pd.read_csv('data/phishing_emails.csv')
safe = pd.read_csv('data/enron_emails.csv')

#add proper labels for phishing and enron emails
phishing['label'] = 'phishing'
safe['label'] = 'legit'

#combine those datasets
emails = pd.concat([phishing, safe], ignore_index=True)

#shuffle phishing and enron datasets together
emails = emails.sample(frac=1).reset_index(drop=True)

#preview data
print(emails.head())