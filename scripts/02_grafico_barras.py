from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Gráfico de barras: vendas médias por categoria e região (dados_barras.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_barras.csv")

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=df,
    x="categoria",
    y="vendas_medias",
    hue="regiao",
    palette="Set2",
    errorbar=None,
    ax=ax,
)

ax.set_title("Vendas Médias por Categoria e Região", fontsize=14, fontweight="bold")
ax.set_xlabel("Categoria", fontsize=11)
ax.set_ylabel("Vendas Médias", fontsize=11)
# Legenda fora da área do gráfico para não cobrir as barras
ax.legend(title="Região", frameon=True, loc="upper left", bbox_to_anchor=(1.02, 1))

plt.tight_layout()
plt.savefig(BASE / "imagens" / "02_barras.png", dpi=300, bbox_inches="tight")
plt.show()
