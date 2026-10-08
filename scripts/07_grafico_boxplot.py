from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Boxplot: distribuição de salários por departamento (dados_boxplot.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_boxplot.csv")

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="departamento",
    y="salario",
    hue="departamento",
    palette="Pastel1",
    legend=False,
    ax=ax,
)

ax.set_title("Distribuição dos Salários por Departamento", fontsize=14, fontweight="bold")
ax.set_xlabel("Departamento", fontsize=11)
ax.set_ylabel("Salário (R$)", fontsize=11)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "07_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()
