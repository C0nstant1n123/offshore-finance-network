import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import networkx as nx
from networkx.algorithms.components import node_connected_component
import community as community_louvain
from collections import defaultdict
from collections import Counter






def resume_graphe(G, type_node_attr='type', type_edge_attr='relation'):
    """
    Affiche un résumé complet d'un graphe NetworkX.
    
    Args:
        G (nx.Graph ou nx.DiGraph): Le graphe à analyser.
        type_node_attr (str): Le nom de l'attribut qui définit le type de noeud (ex: 'entity_type', 'label').
                               Si inconnu, le script essaiera de deviner ou affichera les clés disponibles.
        type_edge_attr (str): Le nom de l'attribut qui définit le type de relation (ex: 'role', 'type').
    """
    print("-" * 30)
    print("📊 RÉSUMÉ DU GRAPHE")
    print("-" * 30)

    # 1. Volumétrie de base
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    print(f"🔹 Nombre total de noeuds : {n_nodes}")
    print(f"🔹 Nombre total d'arêtes : {n_edges}")
    
    # Densité
    density = nx.density(G)
    print(f"🔹 Densité du graphe     : {density:.6f}")
    
    # Composantes connexes (si le graphe n'est pas dirigé ou faiblement connexe pour dirigé)
    if G.is_directed():
        n_components = nx.number_weakly_connected_components(G)
        print(f"🔹 Composantes connexes (faibles) : {n_components}")
    else:
        n_components = nx.number_connected_components(G)
        print(f"🔹 Composantes connexes : {n_components}")

    print("\n" + "-" * 30)
    print("🏷️  ATTRIBUTS ET LABELS")
    print("-" * 30)

    if n_nodes > 0:
        # Récupérer un noeud exemple pour voir les clés
        sample_node = list(G.nodes(data=True))[0]
        print(f"📋 Exemples d'attributs sur un noeud : {list(sample_node[1].keys())}")
        
        # Analyser la distribution des types de noeuds
        # On vérifie si l'attribut spécifié existe, sinon on prend le premier attribut trouvé
        types_nodes = [d.get(type_node_attr, "Non défini") for n, d in G.nodes(data=True)]
        count_nodes = Counter(types_nodes)
        
        print(f"\n🔸 Répartition des types de noeuds (basé sur '{type_node_attr}') :")
        for type_n, count in count_nodes.most_common():
            print(f"   - {type_n}: {count}")

    if n_edges > 0:
        # Récupérer une arête exemple
        sample_edge = list(G.edges(data=True))[0]
        print(f"\n📋 Exemples d'attributs sur une arête : {list(sample_edge[2].keys())}")

        # Analyser la distribution des types d'arêtes
        types_edges = [d.get(type_edge_attr, "Non défini") for u, v, d in G.edges(data=True)]
        count_edges = Counter(types_edges)
        
        print(f"\n🔸 Répartition des types d'arêtes (basé sur '{type_edge_attr}') :")
        for type_e, count in count_edges.most_common():
            print(f"   - {type_e}: {count}")

    print("-" * 30)



def add_tax_haven_labels(G, paradis_fiscaux_codes, paradis_fiscaux_noms):
    for node in tqdm(G.nodes()):
        jurisdiction = G.nodes[node].get('country_codes', '')
        countries = G.nodes[node].get('countries', '')

        if jurisdiction in paradis_fiscaux_codes or countries in paradis_fiscaux_noms:
            G.nodes[node]['Is_Tax_Haven'] = "Yes"
        else:
            G.nodes[node]['Is_Tax_Haven'] = "No"


def add_betweenness_centrality(G):
    betweenness = nx.betweenness_centrality(G, k = 1000,normalized=False, weight=None)
    for node in tqdm(G.nodes()):
        G.nodes[node]['Betweenness'] = betweenness[node]

def add_degree(G):
    degree = dict(G.degree())
    for node in tqdm(G.nodes()):
        G.nodes[node]['Degree'] = degree[node]

def add_net_degree(G):
    net_degree = {}
    for node in G.nodes():
        in_deg = G.in_degree(node)
        out_deg = G.out_degree(node)
        net_degree[node] = out_deg - in_deg
    for node in tqdm(G.nodes()):
        G.nodes[node]['Net_Degree'] = net_degree[node]