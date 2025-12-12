import joblib
from sklearn.linear_model import LogisticRegression
from api.preprocess import prepare_text

def train_model():
    X_train, X_test, y_train, y_test, vectorizer = prepare_text()

    model = LogisticRegression(max_iter= 200)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")

    print(" Training Completed! ")
    print(" model saved as models/model.pkl ")
    print(" vectorizer saved as models/vectorizer.pkl ")

    return model

if __name__ == "__main__":
    train_model()