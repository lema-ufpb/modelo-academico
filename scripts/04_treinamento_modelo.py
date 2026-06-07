#!/usr/bin/env python3
"""
04_treinamento_modelo.py — Treinamento e Validação de Modelos
=============================================================

Este script treina três modelos de classificação para previsão de
churn, utilizando validação cruzada estratificada (K-Fold).

Modelos treinados:
    1. Regressão Logística
    2. Random Forest
    3. LightGBM

Uso:
    python scripts/04_treinamento_modelo.py

Entradas:
    dados/processados/dataset_treino.csv

Saídas:
    modelos/logistic_regression.joblib
    modelos/random_forest.joblib
    modelos/lightgbm.joblib
    resultados/metricas/validacao_cruzada.csv
"""

import os
import re
import unicodedata

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate

# Gradient Boosting — usa LightGBM se disponível, senão sklearn
try:
    from lightgbm import LGBMClassifier
    TEM_LIGHTGBM = True
except ImportError:
    from sklearn.ensemble import GradientBoostingClassifier
    TEM_LIGHTGBM = False

# ── Configurações ──────────────────────────────────────────────
SEED = 42
K_FOLDS = 5
CAMINHO_TREINO = os.path.join("dados", "processados", "dataset_treino.csv")
DIR_MODELOS = "modelos"
DIR_METRICAS = os.path.join("resultados", "metricas")


def carregar_treino():
    """Carrega e separa features e target do dataset de treino."""
    df = pd.read_csv(CAMINHO_TREINO)
    X = df.drop(columns=["churn"])
    y = df["churn"]
    print(f"Dataset de treino: {X.shape[0]} registros, {X.shape[1]} features")
    print(f"Distribuição de churn: {y.value_counts().to_dict()}\n")
    return X, y


def definir_modelos() -> dict:
    """Define os modelos a serem treinados com hiperparâmetros padrão."""
    modelos = {
        "Regressão Logística": LogisticRegression(
            max_iter=1000,
            random_state=SEED,
            solver="lbfgs",
            C=1.0,
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            min_samples_split=5,
            random_state=SEED,
            n_jobs=-1,
        ),
    }

    if TEM_LIGHTGBM:
        modelos["LightGBM"] = LGBMClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.05,
            random_state=SEED,
            verbose=-1,
            n_jobs=-1,
        )
    else:
        modelos["Gradient Boosting"] = GradientBoostingClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.05,
            random_state=SEED,
        )

    return modelos


def validacao_cruzada(modelos: dict, X, y) -> pd.DataFrame:
    """Executa validação cruzada estratificada e retorna métricas."""
    cv = StratifiedKFold(n_splits=K_FOLDS, shuffle=True, random_state=SEED)

    # Usar scorers por string (compatível com todas as versões do scikit-learn)
    scoring = {
        "roc_auc": "roc_auc",
        "f1": "f1",
        "accuracy": "accuracy",
    }

    resultados = []

    for nome, modelo in modelos.items():
        print(f"Treinando: {nome}...")
        cv_results = cross_validate(
            modelo, X, y,
            cv=cv,
            scoring=scoring,
            return_train_score=False,
            n_jobs=-1,
        )

        resultado = {
            "Modelo": nome,
            "AUC-ROC (média)": cv_results["test_roc_auc"].mean(),
            "AUC-ROC (dp)": cv_results["test_roc_auc"].std(),
            "F1-Score (média)": cv_results["test_f1"].mean(),
            "F1-Score (dp)": cv_results["test_f1"].std(),
            "Acurácia (média)": cv_results["test_accuracy"].mean(),
            "Acurácia (dp)": cv_results["test_accuracy"].std(),
        }
        resultados.append(resultado)

        auc_msg = f"AUC-ROC: {resultado['AUC-ROC (média)']:.4f} ± {resultado['AUC-ROC (dp)']:.4f}"
        f1_msg = f"F1: {resultado['F1-Score (média)']:.4f} ± {resultado['F1-Score (dp)']:.4f}"
        acc_msg = f"Acc: {resultado['Acurácia (média)']:.4f} ± {resultado['Acurácia (dp)']:.4f}"
        print(f"  → {auc_msg}")
        print(f"  → {f1_msg}")
        print(f"  → {acc_msg}")
        print()

    return pd.DataFrame(resultados)


def sanitizar_nome(nome: str) -> str:
    """Remove acentos e caracteres especiais, mantendo underscores."""
    nome_ascii = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode("ascii")
    nome_underscore = nome_ascii.replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_]", "", nome_underscore).lower()


def treinar_e_salvar(modelos: dict, X, y):
    """Treina os modelos no dataset completo de treino e salva em disco."""
    os.makedirs(DIR_MODELOS, exist_ok=True)

    for nome, modelo in modelos.items():
        modelo.fit(X, y)
        nome_arquivo = sanitizar_nome(nome) + ".joblib"
        caminho = os.path.join(DIR_MODELOS, nome_arquivo)
        joblib.dump(modelo, caminho)
        print(f"✓ {nome} salvo em: {caminho}")


def main():
    """Ponto de entrada principal."""
    print("=" * 60)
    print("04 — Treinamento e Validação de Modelos")
    print("=" * 60)

    os.makedirs(DIR_METRICAS, exist_ok=True)

    X, y = carregar_treino()
    modelos = definir_modelos()

    # Validação cruzada
    print(f"\nValidação Cruzada Estratificada ({K_FOLDS}-Fold):")
    print("-" * 50)
    df_resultados = validacao_cruzada(modelos, X, y)

    caminho_cv = os.path.join(DIR_METRICAS, "validacao_cruzada.csv")
    df_resultados.to_csv(caminho_cv, index=False, encoding="utf-8")
    print(f"✓ Resultados de CV salvos em: {caminho_cv}")

    # Treinar no dataset completo e salvar
    print("\nTreinamento final (dataset completo):")
    print("-" * 50)
    treinar_e_salvar(modelos, X, y)

    print("\n✓ Treinamento concluído com sucesso!")
    print("=" * 60)


if __name__ == "__main__":
    main()
