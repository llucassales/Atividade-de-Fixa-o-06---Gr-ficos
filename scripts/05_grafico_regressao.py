from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Regressão linear: renda mensal x gasto mensal (dados_regressao.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_regressao.csv")

fig, ax = plt.subplots(figsize=(8, 5))

# Pontos + linha de regressão (com intervalo de confiança)
sns.regplot(
    data=df,
    x="renda_mensal",
    y="gasto_mensal",
    scatter_kws={"alpha": 0.6, "s": 50},
    line_kws={"color": "red", "linewidth": 2},
    ax=ax,
)

# Coeficiente de correlação de Pearson
r = df["renda_mensal"].corr(df["gasto_mensal"])
ax.annotate(f"Correlação (r) = {r:.2f}", xy=(0.05, 0.92), xycoords="axes fraction",
            fontsize=11, bbox=dict(boxstyle="round", fc="white", ec="gray"))

ax.set_title("Regressão: Renda Mensal x Gasto Mensal", fontsize=14, fontweight="bold")
ax.set_xlabel("Renda Mensal (R$)", fontsize=11)
ax.set_ylabel("Gasto Mensal (R$)", fontsize=11)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "05_regressao.png", dpi=300, bbox_inches="tight")
plt.show()
