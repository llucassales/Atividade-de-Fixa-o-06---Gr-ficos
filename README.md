# Visualização de Dados com Matplotlib e Seaborn

Um script Python para cada arquivo de dados, gerando um gráfico por arquivo.

## Estrutura

```
.
├── dados/       # arquivos CSV de entrada
├── scripts/     # um script por gráfico
├── imagens/     # gráficos gerados (PNG, 300 dpi)
├── requirements.txt
└── README.md
```

## Gráficos

| Script | Dados | Gráfico | Biblioteca |
| :-- | :-- | :-- | :-- |
| `01_grafico_linhas.py` | `dados_linhas.csv` | Linhas (série temporal) | Seaborn |
| `02_grafico_barras.py` | `dados_barras.csv` | Barras agrupadas | Seaborn |
| `03_grafico_frequencia.py` | `dados_frequencia.csv` | Barras de frequência | Seaborn |
| `04_grafico_dispersao.py` | `dados_dispersao.csv` | Dispersão | Seaborn |
| `05_grafico_regressao.py` | `dados_regressao.csv` | Regressão linear | Seaborn |
| `06_grafico_distribuicao.py` | `dados_distribuicao.csv` | Histograma + KDE | Seaborn |
| `07_grafico_boxplot.py` | `dados_boxplot.csv` | Boxplot | Seaborn |
| `08_grafico_heatmap.py` | `dados_heatmap.csv` | Heatmap | Seaborn |
| `09_grafico_pizza.py` | `dados_pizza.csv` | Pizza | Matplotlib |

## Como executar

```bash
pip install -r requirements.txt
python scripts/01_grafico_linhas.py   # repita para cada script
```

Cada script lê o CSV correspondente, exibe o gráfico e salva o PNG em `imagens/`.
