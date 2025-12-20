# Mapping offshore finance as a network

Graph analysis of the **ICIJ Offshore Leaks database** (Panama Papers, Paradise Papers and
related leaks), asking what the structure of offshore finance looks like once it is treated
as a single network.

Course project, *Complex Networks* (P. Borgnat & R. Cazabet), M2 Physics of Complex Systems,
ENS de Lyon — **Roman Beauvallet** and **Constantin Deumier**, December 2025.

📄 **[Read the report (PDF, in French)](rapport_Beauvallet_Deumier.pdf)**

## The data

| | |
|---|---|
| Entities (offshore companies) | ~815,000 |
| Officers (people and companies behind them) | ~771,000 |
| Relationships | ~3.3 million |
| Raw size | ~600 MB of CSV |

Source: [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/pages/database).
The raw files are not redistributed here.

## What the analysis does

- **A country-level view.** Aggregating the graph by country gives a net degree per country,
  separating sources of capital from sinks, and a betweenness centrality that reveals which
  jurisdictions act as passage points rather than destinations.
- **A measure of "star-shaped" structure**, to quantify how far a jurisdiction behaves as a
  hub with many one-off satellites.
- **A multilayer view by node type.** Companies, officers, intermediaries and addresses do not
  play the same role; splitting the graph by type, and projecting the bipartite
  officer–company structure, separates tightly knit clans from isolated silos.
- **Structural signatures.** Degree distributions (scale-free behaviour), clustering
  coefficients, and what they say about the social structure behind the shell companies.
- **Community detection (Louvain)** — and the question the communities answer: are they
  national, or do they cut across borders?

## Contents

| File | What it is |
|---|---|
| `rapport_Beauvallet_Deumier.pdf` | The report — full analysis, figures and conclusions |
| `Conmplex_Network_3.ipynb` | Main analysis: graph construction, centralities, Louvain, country flows |
| `ComplexNetworks2.ipynb` | Earlier exploration: k-cores, components, clustering |
| `pythonfile.py` | Helper functions |

## Running it

Download the ICIJ CSV dump into the repository root, then:

```bash
pip install networkx python-louvain pandas matplotlib
jupyter notebook Conmplex_Network_3.ipynb
```

Python (NetworkX, Pandas, python-louvain); graphs exported to GEXF and visualised in
[Gephi](https://gephi.org).
