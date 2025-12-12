import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from preprocess import prepare_data


def evaluate_model():
    model = joblib.load("models/model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")

    _, X_test, _, y_test, _ = prepare_data()

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    precision = precision_score(y_test, preds, average="weighted")
    recall = recall_score(y_test, preds, average="weighted")
    f1 = f1_score(y_test, preds, average="weighted")

    print("\n===== Evaluation Report =====")
    print(f"Accuracy  : {acc:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    print("==============================\n")


if __name__ == "__main__":
    evaluate_model()
