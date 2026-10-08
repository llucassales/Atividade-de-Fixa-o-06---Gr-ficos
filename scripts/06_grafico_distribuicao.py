from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Histograma com KDE: distribuição da idade dos clientes (dados_distribuicao.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 5))

sns.histplot(data=df, x="idade", bins=15, kde=True, color="#4c72b0", ax=ax)

# Linha de referência com a média
media = df["idade"].mean()
ax.axvline(x=media, color="red", linestyle="--", label=f"Média ({media:.1f} anos)")

ax.set_title("Distribuição da Idade dos Clientes", fontsize=14, fontweight="bold")
ax.set_xlabel("Idade (anos)", fontsize=11)
ax.set_ylabel("Frequência", fontsize=11)
ax.legend(frameon=True)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "06_distribuicao.png", dpi=300, bbox_inches="tight")
plt.show()
