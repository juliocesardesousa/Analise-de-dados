"""
app.py
----------------
Ponto de entrada do dashboard. Só cuida de interface (filtros, layout,
KPIs) e chama as funções de src/data_loader.py e src/charts.py.
 
Rodar com: streamlit run app.py
"""
 
import streamlit as st
 
from src.data_loader import load_data, filter_data, get_kpis
from src.charts import (
    plot_faturamento_por_categoria,
    plot_evolucao_mensal,
    plot_distribuicao_faturamento,
    plot_entrega_por_regiao,
    plot_preco_vs_avaliacao,
    plot_heatmap_regiao_categoria,
)
 
st.set_page_config(
    page_title="Dashboard de Vendas E-commerce",
    page_icon="📊",
    layout="wide",
)
 
# ---------- Carregar dados ----------
df = load_data()
 
# ---------- Sidebar: filtros ----------
st.sidebar.header("Filtros")
 
categorias = st.sidebar.multiselect(
    "Categoria do produto",
    options=sorted(df["product_category"].unique()),
    default=None,
)
 
regioes = st.sidebar.multiselect(
    "Região",
    options=sorted(df["region"].unique()),
    default=None,
)
 
data_min, data_max = df["order_date"].min(), df["order_date"].max()
periodo = st.sidebar.date_input(
    "Período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max,
)
 
df_filtrado = filter_data(
    df,
    categories=categorias if categorias else None,
    regions=regioes if regioes else None,
    date_range=periodo if isinstance(periodo, tuple) and len(periodo) == 2 else None,
)
 
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
    st.stop()
 
# ---------- Cabeçalho ----------
st.title("📊 Dashboard de Vendas — E-commerce")
st.caption(f"{len(df_filtrado):,} pedidos analisados de um total de {len(df):,}")
 
# ---------- KPIs ----------
kpis = get_kpis(df_filtrado)
 
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Faturamento Total", f"R$ {kpis['faturamento_total']:,.2f}")
col2.metric("Ticket Médio", f"R$ {kpis['ticket_medio']:,.2f}")
col3.metric("Total de Pedidos", f"{kpis['total_pedidos']:,}")
col4.metric("Avaliação Média", f"{kpis['avaliacao_media']:.2f} ⭐")
col5.metric("Prazo Médio de Entrega", f"{kpis['prazo_medio_entrega']:.1f} dias")
 
st.divider()
 
# ---------- Tabs de gráficos ----------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Faturamento por Categoria",
        "Evolução Mensal",
        "Distribuição de Pedidos",
        "Entrega por Região",
        "Preço x Avaliação",
        "Região x Categoria",
    ]
)
 
with tab1:
    st.pyplot(plot_faturamento_por_categoria(df_filtrado))
 
with tab2:
    meta = st.number_input("Meta mensal de faturamento (R$)", value=30000, step=1000)
    st.pyplot(plot_evolucao_mensal(df_filtrado, meta_fixa=meta))
 
with tab3:
    st.pyplot(plot_distribuicao_faturamento(df_filtrado))
 
with tab4:
    st.pyplot(plot_entrega_por_regiao(df_filtrado))
 
with tab5:
    st.pyplot(plot_preco_vs_avaliacao(df_filtrado))
 
with tab6:
    st.pyplot(plot_heatmap_regiao_categoria(df_filtrado))
 
st.divider()
with st.expander("Ver dados filtrados (tabela)"):
    st.dataframe(df_filtrado, use_container_width=True)
 



