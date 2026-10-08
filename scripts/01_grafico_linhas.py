from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Gráfico de linhas: evolução diária das vendas (dados_linhas.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_linhas.csv", parse_dates=["data"])

fig, ax = plt.subplots(figsize=(11, 5))

# Linha da tendência diária + pontos coloridos pela loja responsável
sns.lineplot(data=df, x="data", y="vendas", color="gray", linewidth=1.5, alpha=0.7, ax=ax)
sns.scatterplot(data=df, x="data", y="vendas", hue="loja", palette="Set1", s=50, ax=ax)

# Linha de referência com a média do período
media = df["vendas"].mean()
ax.axhline(y=media, color="red", linestyle="--", linewidth=1, label=f"Média ({media:.1f})")

ax.set_title("Evolução Diária das Vendas (Jan–Mar 2026)", fontsize=14, fontweight="bold")
ax.set_xlabel("Data", fontsize=11)
ax.set_ylabel("Vendas", fontsize=11)
ax.legend(title="Loja", frameon=True)
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "01_linhas.png", dpi=300, bbox_inches="tight")
plt.show()
