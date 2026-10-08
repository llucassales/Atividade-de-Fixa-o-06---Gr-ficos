from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid")

"""Heatmap: movimento de clientes por dia da semana e horário (dados_heatmap.csv)."""
df = pd.read_csv(BASE / "dados" / "dados_heatmap.csv")

# Transforma em matriz (dias x horários), na ordem natural da semana
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
matriz = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
matriz = matriz.reindex(ordem_dias)

fig, ax = plt.subplots(figsize=(10, 5))

sns.heatmap(
    matriz,
    annot=True,
    fmt="d",
    cmap="YlOrRd",
    linewidths=0.5,
    cbar_kws={"label": "Clientes"},
    ax=ax,
)

ax.set_title("Movimento de Clientes por Dia e Horário", fontsize=14, fontweight="bold")
ax.set_xlabel("Horário", fontsize=11)
ax.set_ylabel("Dia da Semana", fontsize=11)

plt.tight_layout()
plt.savefig(BASE / "imagens" / "08_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
