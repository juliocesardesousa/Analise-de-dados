"""
charts.py
----------------
Cada função recebe um DataFrame já filtrado e devolve uma figura
matplotlib pronta para ser renderizada no Streamlit (st.pyplot(fig)).

Separar os gráficos da interface permite reaproveitar essas funções
em outros contextos (ex: gerar um relatório em PDF) sem duplicar código.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd


def plot_faturamento_por_categoria(df: pd.DataFrame):
    faturamento = df.groupby("product_category")["revenue"].sum().sort_values()

    fig, ax = plt.subplots(figsize=(10, 5))
    barras = ax.barh(faturamento.index, faturamento.values, color="#1f77b4")

    ax.ticklabel_format(style="plain", axis="x")

    for barra in barras:
        largura = barra.get_width()
        ax.text(
            largura,
            barra.get_y() + barra.get_height() / 2,
            f"R$ {largura:,.2f}",
            va="center",
            fontsize=10,
        )

    ax.set_title("Faturamento Total por Categoria")
    ax.set_xlabel("Faturamento (R$)")
    ax.set_ylabel("Categoria")
    ax.set_xlim(0, faturamento.max() * 1.35)
    fig.tight_layout()
    return fig


def plot_evolucao_mensal(df: pd.DataFrame, meta_fixa: float = 30000):
    vendas_mensais = df.groupby("year_month_str")["revenue"].sum().reset_index()
    vendas_mensais = vendas_mensais.sort_values("year_month_str")

    acima_meta = vendas_mensais[vendas_mensais["revenue"] >= meta_fixa]
    abaixo_meta = vendas_mensais[vendas_mensais["revenue"] < meta_fixa]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        vendas_mensais["year_month_str"],
        vendas_mensais["revenue"],
        color="#888888",
        linewidth=1.2,
        zorder=1,
    )

    ax.scatter(
        acima_meta["year_month_str"],
        acima_meta["revenue"],
        color="#2ca02c",
        s=40,
        label="Acima/Igual à Meta",
        zorder=2,
    )
    ax.scatter(
        abaixo_meta["year_month_str"],
        abaixo_meta["revenue"],
        color="#d62728",
        s=40,
        label="Abaixo da Meta",
        zorder=2,
    )

    ax.axhline(
        y=meta_fixa,
        color="#171d91",
        linestyle="--",
        linewidth=1,
        label=f"Meta Fixa Mensal: R$ {meta_fixa:,.2f}",
    )

    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=15))
    ax.set_title("Evolução Mensal do Faturamento em Relação à Meta")
    ax.set_xlabel("Mês/Ano")
    ax.set_ylabel("Faturamento (R$)")
    plt.setp(ax.get_xticklabels(), rotation=45)
    ax.ticklabel_format(style="plain", axis="y")
    ax.legend(loc="upper right")
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


def plot_distribuicao_faturamento(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df["revenue"], bins=30, color="#ff7f0e", edgecolor="white", alpha=0.85)
    ax.set_title("Distribuição do Faturamento por Pedido")
    ax.set_xlabel("Valor do Pedido (R$)")
    ax.set_ylabel("Quantidade de Pedidos")
    ax.ticklabel_format(style="plain", axis="x")
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")
    fig.tight_layout()
    return fig


def plot_entrega_por_regiao(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x="region", y="delivery_days", hue="region", palette="Set2", legend=False, ax=ax)
    ax.set_title("Tempo de Entrega (Dias) por Região")
    ax.set_xlabel("Região")
    ax.set_ylabel("Dias de Entrega")
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")
    fig.tight_layout()
    return fig


def plot_preco_vs_avaliacao(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(
        data=df, x="unit_price", y="customer_rating", alpha=0.5, color="#9467bd", s=50, ax=ax
    )
    ax.set_title("Relação entre Preço Unitário e Avaliação do Cliente")
    ax.set_xlabel("Preço Unitário (R$)")
    ax.set_ylabel("Avaliação do Cliente (1 a 5)")
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


def plot_heatmap_regiao_categoria(df: pd.DataFrame):
    tabela_cruzada = pd.crosstab(
        df["region"], df["product_category"], values=df["revenue"], aggfunc="sum"
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        tabela_cruzada,
        annot=True,
        fmt=",.0f",
        cmap="YlGnBu",
        cbar_kws={"label": "Faturamento Total (R$)"},
        ax=ax,
    )
    ax.set_title("Faturamento Total: Região vs Categoria de Produto")
    ax.set_xlabel("Categoria do Produto")
    ax.set_ylabel("Região")
    fig.tight_layout()
    return fig