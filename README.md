# 📊 Dashboard de Análise de Vendas — E-commerce

Dashboard interativo desenvolvido em **Python + Streamlit** para análise de mais de
5.000 pedidos de um e-commerce, com filtros dinâmicos, KPIs e visualizações que
respondem a perguntas de negócio como: quais categorias faturam mais, como o
faturamento evolui mês a mês em relação a uma meta, e como o prazo de entrega
varia por região.

## 🎯 Objetivo

Projeto de portfólio construído durante minha formação em Análise e Desenvolvimento
de Sistemas, aplicando análise exploratória de dados (EDA) e visualização de dados
a um cenário de negócio realista.

## 🗂️ Estrutura do projeto

```
ecommerce-dashboard/
├── app.py                  # Interface Streamlit (filtros, KPIs, layout)
├── src/
│   ├── data_loader.py      # Carregamento, tipagem e filtragem dos dados
│   └── charts.py           # Funções de geração de cada gráfico (matplotlib/seaborn)
├── data/
│   └── ecommerce_sales.csv # Dataset (5.000 pedidos)
├── requirements.txt
└── README.md
```

A separação entre `data_loader.py`, `charts.py` e `app.py` segue o princípio de
responsabilidade única: dados, visualizações e interface não se misturam, o que
facilita manutenção, testes e reuso das funções em outros contextos (ex: geração
de relatório em PDF).

## 📈 Análises disponíveis

- **Faturamento total por categoria** — quais categorias de produto mais faturam
- **Evolução mensal do faturamento** — comparado a uma meta configurável
- **Distribuição do valor dos pedidos** — histograma de ticket por pedido
- **Tempo de entrega por região** — boxplot comparando regiões
- **Preço unitário x avaliação do cliente** — existe relação entre preço e nota?
- **Heatmap Região x Categoria** — cruzamento de faturamento

Todos os gráficos respondem aos filtros de **categoria**, **região** e
**período**, selecionáveis na barra lateral.

## 🚀 Como rodar localmente

```bash
# 1. Clonar o repositório
git clone https://github.com/juliocesardesousa/Analise-de-dados.git
cd ecommerce-dashboard

# 2. Criar e ativar um ambiente virtual (opcional, recomendado)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Rodar o dashboard
streamlit run app.py
```

O app abre automaticamente no navegador em `http://localhost:8501`.

## 🧰 Tecnologias

- Python 3.11+
- Streamlit
- Pandas
- Matplotlib / Seaborn

## 📊 Sobre os dados

Dataset com 5.000 registros de pedidos, contendo: data do pedido, categoria do
produto, região, quantidade, preço unitário, desconto, forma de pagamento, prazo
de entrega, avaliação do cliente e faturamento.

## 👤 Autor

Projeto desenvolvido como parte de portfólio para vaga de estágio em Análise de
Dados / TI.
