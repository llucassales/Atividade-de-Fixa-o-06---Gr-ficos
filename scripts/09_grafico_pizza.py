from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Gráfico de pizza: faturamento por canal de venda (dados_pizza.csv).

O Seaborn não possui gráfico de pizza, então usamos plt.pie do Matplotlib
com uma paleta do Seaborn.
"""
df = pd.read_csv(BASE / "dados" / "dados_pizza.csv")

fig, ax = plt.subplots(figsize=(7, 7))

ax.pie(
    df["faturamento"],
    labels=df["canal_venda"],
    autopct="%1.1f%%",
    startangle=90,
    counterclock=False,
    colors=sns.color_palette("Set2", len(df)),
    wedgeprops={"edgecolor": "white", "linewidth": 2},
    textprops={"fontsize": 11},
)

ax.set_title("Faturamento por Canal de Venda", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(BASE / "imagens" / "09_pizza.png", dpi=300, bbox_inches="tight")
plt.show()
