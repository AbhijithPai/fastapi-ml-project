import joblib
from sklearn.linear_model import LogisticRegression
from training.preprocess import prepare_data

MODEL_PATH = "models/model_v1.pkl"
VECTORIZER_PATH = "models/vectorizer_v1.pkl"

def train():
    X_train, X_test, y_train, y_test, vectorizer = prepare_data("api/data/sentiment.csv")

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print("✅ Model trained and saved")

if __name__ == "__main__":
    train()
