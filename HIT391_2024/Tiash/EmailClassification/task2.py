#%%
import numpy as np      
import pandas as pd       
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#%%
df = pd.read_csv("emails.csv")
df.isnull().sum()


#%%
spam_count = sum(df['spam'])
non_spam_count = len(df) - spam_count
total_emails = len(df)
print("Spam :", spam_count)
print("Non-spam :", non_spam_count)

categories = ['Spam', 'Non-spam']
counts = [spam_count, non_spam_count]

plt.bar(categories, counts)
plt.xlabel('Email Type')
plt.ylabel('Count')
plt.title('Count of Spam and Non-spam Emails')
plt.show()

#%%
df = df.iloc[:, 1:]
df

#%%
X = df.iloc[:, :5000]
y = df.iloc[:, 5000]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#%%
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score

lrc = LogisticRegression(solver = 'liblinear', penalty = 'l1')
svc = SVC(kernel= "sigmoid", gamma  = 1.0)

clfs = {
    'LR': lrc,
    'SVC': svc,
 
}


#%%
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, classification_report

# Initialize the classifiers
lrc = LogisticRegression(solver='liblinear', penalty='l1')
svc = SVC(kernel="sigmoid", gamma=1.0)

clfs = {
    'LR': lrc,
    'SVC': svc,
}

# Function to train classifier and evaluate it
def train_classifier(clf, X_train, y_train, X_test, y_test):
    print("Training {} ...".format(clf.__class__.__name__))	
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro', zero_division=1)  # Specify zero_division parameter
    report = classification_report(y_test, y_pred, zero_division=1)  # Specify zero_division parameter
    return accuracy, precision, report

# Train classifiers and collect metrics
accuracy_scores = []
precision_scores = []

for name, clf in clfs.items():
    current_accuracy, current_precision, report = train_classifier(clf, X_train, y_train, X_test, y_test)
    print()
    print("For: ", name)
    print("Accuracy: ", current_accuracy)
    print("Precision: ", current_precision)
    print(report)
    
    accuracy_scores.append(current_accuracy)
    precision_scores.append(current_precision)
