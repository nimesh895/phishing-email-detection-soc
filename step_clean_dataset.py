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

def clean_email(text):
    if pd.isnull(text):
        return ""

    #Remove HTML
    text = BeautifulSoup(str(text), "lxml").get_text()
    #Remove special charac and numbers
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    #lowercase
    text = text.lower()
    #remove stopwords
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

#Apply cleaning
if 'text' in emails.columns:
    emails['clean_text'] = emails['text'].apply(clean_email)
elif 'message' in emails.columns:
    emails['clean_text'] = emails['message'].apply(clean_email)
else:
    raise ValueError("Dataset must contain either 'text' or 'message' column!")

emails.to_csv("emails_cleaned.csv", index=False)

print("----- CLEANED DATA -----")
print(emails[['clean_text', 'label']].head(5))

print("Cleaning done")