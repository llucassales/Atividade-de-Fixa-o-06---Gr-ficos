from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Gráfico de dispersão: altura x peso por sexo (dados_dispersao.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="altura_cm",
    y="peso_kg",
    hue="sexo",
    style="sexo",
    s=80,
    alpha=0.8,
    ax=ax,
)

ax.set_title("Relação entre Altura e Peso", fontsize=14, fontweight="bold")
ax.set_xlabel("Altura (cm)", fontsize=11)
ax.set_ylabel("Peso (kg)", fontsize=11)
ax.legend(title="Sexo", frameon=True)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "04_dispersao.png", dpi=300, bbox_inches="tight")
plt.show()
