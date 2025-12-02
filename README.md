Last updated: December 2, 2025

# phishing-email-detection-soc
SOC Analyst Project — Phishing Email Detection using NLP &amp; Machine Learning (Logistic Regression)


# Phishing Email Detection — SOC Analyst Project

![Project Overview](download%20phishing%20email%20data%20set%20in%20kaggle.png)

**Real SOC-relevant project**: Built a **phishing email classifier** using NLP + Machine Learning (Logistic Regression) to simulate how modern SOC teams detect phishing — the #1 attack vector.

> “As a student passionate about cybersecurity and SOC operations, I built this project to simulate how phishing emails are detected using Natural Language Processing (NLP) and Machine Learning. Since phishing is the #1 attack vector in modern cyber incidents, this project helped me understand how SOC teams triage and analyze suspicious emails daily.”

### Dataset Used
- Kaggle Phishing Email Dataset + Enron Email Dataset (legitimate emails)
- Labeled: Phishing = 1 | Legitimate = 0

### Steps Implemented

#### 1. Environment Setup
![Virtual Environment & Libraries](use%20a%20virtual%20environment%20to%20isolate%20project%20dependencies.png)
![Install Libraries](install%20essential%20libraries.png)

#### 2. Data Collection & Preprocessing (NLP)
![Download Dataset](download%20enron%20email%20dataset.png)
![Clean Text](Clean%20text%20ready%20for%20ML%20models,%20similar%20to%20what%20SOC%20analysts%20do%20to%20standardize%20data%20for%20automation3.png)
- Removed HTML, punctuation, stopwords
- Used **Bag of Words** + **TF-IDF Vectorizer**

#### 3. Model Training
![Train Model](train%20a%20model%20Naive%20Bayes%20classifier%20can%20detect%20phishing%20emails.png)
- Trained **Naive Bayes** (baseline) + **Logistic Regression** (final model)
- 80/20 Train-Test split
- Evaluated with accuracy, precision, recall, F1-score, confusion matrix

#### 4. SOC Simulation (Bonus!)
- Crafted phishing-style email in Kali Linux
- Sent to Windows mailbox
- Extracted text → ran through model → **Correctly flagged as phishing**

### Sample Results
| Class     | Precision | Recall | F1-score | Support |
|----------|-----------|--------|----------|---------|
| Legit    | 0.75      | 1.00   | 0.86     | 3       |
| Phishing | 1.00      | 0.50   | 0.67     | 2       |
| **Accuracy** |           |        | **0.80**     | 5       |

### Why This Matters for SOC Roles
- Phishing = most common SOC ticket
- Shows understanding of **email triage workflow**
- Combines **AI + Cybersecurity** — highly valued in modern security teams
- Demonstrates **analytical + technical thinking**

---


### Tools & Tech
- Python, scikit-learn, pandas, NLTK
- Jupyter / VS Code
- Kaggle + Enron datasets

### Next Steps
- Deploy as API + integrate with email gateway
- Add URL + attachment analysis
- Build dashboard for SOC analysts

---
**Original PDF**: [Phishing Email Detection.pdf](Phishing%20Email%20Detection.pdf)

**Author**: Nimesh Akalanka Peiris  
**LinkedIn**: [linkedin.com/in/nimesh23](https://www.linkedin.com/in/nimesh23)  
**Year**: 2025

---
**Perfect for SOC Analyst, Cybersecurity Analyst, or  Blue Team internships**
