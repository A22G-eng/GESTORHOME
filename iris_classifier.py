# Iris_classifier.py

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    # Carregar o conjunto de dados Iris
    iris = load_iris()
    X = iris.data  # Características (features)
    y = iris.target  # Rótulos (labels)

    # Dividir o conjunto de dados em conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar o classificador
    classifier = DecisionTreeClassifier()

    # Treinar o classificador
    classifier.fit(X_train, y_train)

    # Fazer previsões
    y_pred = classifier.predict(X_test)

    # Avaliar o modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Acurácia: {accuracy * 100:.2f}%")
    print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    main()