# %%
import argparse
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score, roc_auc_score
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn

# %%
def parse_args():
    parser = argparse.ArgumentParser(description = 'Train a logistic regression model')
    parser.add_argument('--C', type = float, default = 1.0, help = 'Inverse of regularization strength')
    parser.add_argument('--max_iter', type = int, default = 100, help = 'Maximun number of iterations to converge')
    parser.add_argument('--penalty', type = str, default = 'l2', help = 'Norm used in the penalization')
    return parser.parse_args()

# %%
def main():
    # Parseamos los argumentos
    args = parse_args()

    # Cargar los datos
    df = (pd.read_csv('https://raw.githubusercontent.com/edroga/Datasets_for_projects/main/cancer.csv')
          .assign(diagnosis = lambda x: np.where(x['diagnosis'] == 'M', 1, 0)))

    # Partimos en train_test
    X_train, X_test, y_train, y_test = train_test_split(df.drop(columns = ['diagnosis']),
                                                        df['diagnosis'],
                                                        test_size = 0.2,
                                                        random_state = 42)

    # Usar el context manager para crear un ambiente de ejecución de mlflow
    with mlflow.start_run():
        # Loggeamos los parametros parseados que se van a usar
        mlflow.log_param('C', args.C)
        mlflow.log_param('max_iter', args.max_iter)
        mlflow.log_param('penalty', args.penalty)

        # Instanciamos el modelo
        model = LogisticRegression(C = args.C, max_iter = args.max_iter, penalty = args.penalty)
        # Entrenamos el modelo
        model.fit(X_train, y_train)
        # Creamos los pronosticos del modelo
        y_pred = model.predict(X_test)

        # Calculamos las metricas
        acc = accuracy_score(y_test, y_pred)
        balanced_acc = balanced_accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)

        # Loggeamos las metricas
        mlflow.log_metric('accuracy', acc)
        mlflow.log_metric('balanceded_accuracy', balanced_acc)
        mlflow.log_metric('f1_score', f1)
        mlflow.log_metric('roc_auc', roc_auc)

        # Loggear el modelo
        mlflow.sklearn.log_model(model, 'model')

        # Loggeamos el train.py como un artefacto
        mlflow.log_artifact('entrena.py')

        # Imprimit las metricas
        print(f'Accuracy: {acc}')
        print(f'Balanced accuracy: {balanced_acc}')
        print(f'f1 score: {f1}')
        print(f'ROC AUC: {roc_auc}')

# Entry point
if __name__ == '__main__':
    main()


