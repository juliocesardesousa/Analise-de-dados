# importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

df = pd.read_csv("ecommerce_sales_analytics_5000.csv")


# Gráfico de barras:
# 1. Agrupar o faturamento por categoria
faturamento = df.groupby("product_category")["revenue"].sum().sort_values()

# 2. Criar o gráfico
plt.figure(figsize=(10, 5))
barras = plt.barh(faturamento.index, faturamento.values, color="#1f77b4")

# 3. Formatar o eixo X para não exibir notação científica (ex: 1e6)
plt.ticklabel_format(style = "plain", axis = "x")

# 4. Adicionar os valores exatos formatados do lado de cada barra
for barra in barras:
    largura = barra.get_width()
    # Exibe formatado em Milhões (ex: R$ 1.83M) ou número completo
    texto = f"R$ {largura:,.2f}"
    plt.text(
        largura,
        barra.get_y() + barra.get_height() / 2,
        texto,
        va="center",
        fontsize=10,
    )

plt.title("Faturamento Total por Categoria")
plt.xlabel("Faturamento (R$)")
plt.ylabel("Categoria")

# Ajusta as margens para o texto não sair da tela
plt.xlim(0, faturamento.max() * 1.35)
plt.tight_layout()

plt.show()

# # 1. Converter a data e extrair o mês/ano
# df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")
# df["mes_ano"] = df["order_date"].dt.to_period("M")

# # 2. Agrupar por mês e calcular o faturamento mensal
# vendas_mensais = df.groupby("mes_ano")["revenue"].sum().reset_index()
# vendas_mensais["mes_ano_str"] = vendas_mensais["mes_ano"].dt.strftime("%m/%Y")

# # 3. Definir a meta fixa e separar as categorias de pontos
# meta_fixa = 30000

# acima_meta = vendas_mensais[vendas_mensais["revenue"] >= meta_fixa]
# abaixo_meta = vendas_mensais[vendas_mensais["revenue"] < meta_fixa]

# # 4. Plotar o gráfico
# fig, ax = plt.subplots(figsize=(12, 5))

# # Linha contínua cinza conectando a evolução de todos os meses
# ax.plot(
#     vendas_mensais["mes_ano_str"],
#     vendas_mensais["revenue"],
#     color = "#888888",
#     linewidth = 1.2,
#     linestyle = "-",
#     zorder = 1,
# )

# # Pontos Verdes (Acima ou Igual à Meta)
# ax.scatter(
#     acima_meta["mes_ano_str"],
#     acima_meta["revenue"],
#     color = "#2ca02c",
#     s = 40,
#     label = "Acima/Igual à Meta",
#     zorder = 2,
# )

# # Pontos Vermelhos (Abaixo da Meta)
# ax.scatter(
#     abaixo_meta["mes_ano_str"],
#     abaixo_meta["revenue"],
#     color = "#d62728",
#     s = 40,
#     label = "Abaixo da Meta",
#     zorder = 2,
# )

# # Linha de referência da Meta Fixa
# ax.axhline(
#     y = meta_fixa,
#     color = "#171d91",
#     linestyle = "--",
#     linewidth = 1,
#     label = f"Meta Fixa Mensal: R$ {meta_fixa:,.2f}",
# )

# # 5. Ajustes de eixos e formatação
# ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=15))
# plt.title("Evolução Mensal do Faturamento em Relação à Meta")
# plt.xlabel("Mês/Ano")
# plt.ylabel("Faturamento (R$)")
# plt.xticks(rotation=45)
# plt.ticklabel_format(style="plain", axis="y")
# plt.legend(loc="upper right")
# plt.grid(True, linestyle = "--", alpha = 0.5)
# plt.tight_layout()

# plt.show()

# # 1. Gerar o Histograma
# plt.figure(figsize=(10, 5))
# plt.hist(df["revenue"], bins=30, color="#ff7f0e", edgecolor="white", alpha=0.85)
# plt.title("Distribuição do Faturamento por Pedido")
# plt.xlabel("Valor do Pedido (R$)")
# plt.ylabel("Quantidade de Pedidos")
# plt.ticklabel_format(style="plain", axis="x")
# plt.grid(True, linestyle="--", alpha=0.5, axis="y")
# plt.tight_layout()

# plt.show()

# # 1. Gerar o Boxplot
# plt.figure(figsize=(10, 5))
# sns.boxplot(data = df, x = "region", y = "delivery_days", palette = "Set2")

# plt.title("Tempo de Entrega (Dias) por Região")
# plt.xlabel("Região")
# plt.ylabel("Dias de Entrega")
# plt.grid(True, linestyle = "--", alpha = 0.5, axis = "y")
# plt.tight_layout()

# plt.show()

# # 1. Gerar o Scatter Plot ****muita informação na tela
# plt.figure(figsize=(10, 5))
# sns.scatterplot(
#     data = df, x = "unit_price", y = "customer_rating", alpha = 0.5, color = "#9467bd", s = 50
# )

# plt.title("Relação entre Desconto (%) e Avaliação do Cliente")
# plt.xlabel("Percentual de Desconto")
# plt.ylabel("Avaliação do Cliente (1 a 5)")
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.tight_layout()

# plt.show()

# # 1. Criar a tabela cruzada
# tabela_cruzada = pd.crosstab(
#     df["region"], df["product_category"], values=df["revenue"], aggfunc="sum"
# )

# # 2. Gerar o Heatmap
# plt.figure(figsize=(10, 6))
# sns.heatmap(
#     tabela_cruzada,
#     annot = True,
#     fmt = ",.0f",
#     cmap = "YlGnBu",
#     cbar_kws = {"label": "Faturamento Total (R$)"},
# )

# plt.title("Faturamento Total: Região vs Categoria de Produto")
# plt.xlabel("Categoria do Produto")
# plt.ylabel("Região")
# plt.tight_layout()

# plt.show()
