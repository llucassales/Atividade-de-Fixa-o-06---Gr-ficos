from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Barras de frequência: chamados por tipo de atendimento (dados_frequencia.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_frequencia.csv")

# Ordena da categoria mais frequente para a menos frequente
ordem = df["tipo_atendimento"].value_counts().index

fig, ax = plt.subplots(figsize=(8, 5))

sns.countplot(
    data=df,
    x="tipo_atendimento",
    order=ordem,
    hue="tipo_atendimento",
    hue_order=ordem,
    palette="Blues_r",
    legend=False,
    ax=ax,
)

ax.margins(y=0.1)  # folga no topo para o rótulo

# Rótulo com a contagem sobre cada barra
for container in ax.containers:
    ax.bar_label(container, fontsize=10, padding=3)

ax.set_title("Frequência de Chamados por Tipo de Atendimento", fontsize=14, fontweight="bold")
ax.set_xlabel("Tipo de Atendimento", fontsize=11)
ax.set_ylabel("Quantidade de Chamados", fontsize=11)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "03_frequencia.png", dpi=300, bbox_inches="tight")
plt.show()
