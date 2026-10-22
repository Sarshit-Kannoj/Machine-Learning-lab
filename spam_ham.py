# Spam/Ham Filtering Model

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training dataset
messages = [
    "Win a free prize now",
    "Congratulations you won a lottery",
    "Claim your free gift",
    "Hello how are you",
    "Are we meeting today",
    "Please call me later",
    "You have won free money",
    "Let's study together"
]

labels = [
    "Spam",
    "Spam",
    "Spam",
    "Ham",
    "Ham",
    "Ham",
    "Spam",
    "Ham"
]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train the model
model = MultinomialNB()
model.fit(X, labels)

# Take user input
user_message = input("Enter a message to check: ")

# Predict Spam or Ham
message_vector = vectorizer.transform([user_message])
prediction = model.predict(message_vector)

print("Message:", user_message)
print("Prediction:", prediction[0])