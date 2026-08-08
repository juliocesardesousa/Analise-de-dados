"""
data_loader.py
----------------
Responsável por carregar o dataset e aplicar as transformações
necessárias (tipagem de datas, colunas auxiliares, filtros).

Mantendo essa lógica separada do app.py, fica fácil trocar a fonte
de dados no futuro (ex: banco de dados, API) sem mexer na interface.
"""

import pandas as pd
import streamlit as st

DATA_PATH = "data/ecommerce_sales.csv"


@st.cache_data
def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Carrega o CSV, ajusta tipos e cria colunas auxiliares de data."""
    df = pd.read_csv(path)

    df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")
    df["year_month"] = df["order_date"].dt.to_period("M")
    df["year_month_str"] = df["year_month"].dt.strftime("%m/%Y")

    return df


def filter_data(
    df: pd.DataFrame,
    categories: list[str] | None = None,
    regions: list[str] | None = None,
    date_range: tuple | None = None,
) -> pd.DataFrame:
    """Aplica os filtros selecionados na sidebar do dashboard."""
    filtered = df.copy()

    if categories:
        filtered = filtered[filtered["product_category"].isin(categories)]

    if regions:
        filtered = filtered[filtered["region"].isin(regions)]

    if date_range and len(date_range) == 2:
        start, end = date_range
        filtered = filtered[
            (filtered["order_date"] >= pd.to_datetime(start))
            & (filtered["order_date"] <= pd.to_datetime(end))
        ]

    return filtered


def get_kpis(df: pd.DataFrame) -> dict:
    """Calcula os indicadores principais exibidos no topo do dashboard."""
    return {
        "faturamento_total": df["revenue"].sum(),
        "ticket_medio": df["revenue"].mean(),
        "total_pedidos": len(df),
        "avaliacao_media": df["customer_rating"].mean(),
        "prazo_medio_entrega": df["delivery_days"].mean(),
    }