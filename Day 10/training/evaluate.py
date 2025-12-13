import joblib
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from training.preprocess import prepare_data

def evaluate():
    X_train, X_test, y_train, y_test, vectorizer = prepare_data("api/data/sentiment.csv")

    model = joblib.load("models/model_v1.pkl")

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average="weighted"
    )

    print("===== Evaluation Report =====")
    print(f"Accuracy  : {acc:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    print("==============================")

if __name__ == "__main__":
    evaluate()
