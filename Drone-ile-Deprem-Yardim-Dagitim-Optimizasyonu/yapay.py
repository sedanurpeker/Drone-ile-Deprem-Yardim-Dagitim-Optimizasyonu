import pandas as pd # type: ignore
import numpy as np # type: ignore
from sklearn.cluster import KMeans # type: ignore
import networkx as nx # type: ignore

# Excel dosyalarını yükle
file_path = r"E:\Üniversite Ders Notları\Üniversite Dersleri__5.YARIYIL\Yapay Öğrenmenin Temelleri\22010903062_22010903060\mesafe_tablosu.xlsx"
allocation_file_path = r"E:\Üniversite Ders Notları\Üniversite Dersleri__5.YARIYIL\Yapay Öğrenmenin Temelleri\22010903062_22010903060\ihtiyac_tablosu.xlsx"

distances_df = pd.read_excel(file_path)
allocation_df = pd.read_excel(allocation_file_path)

# Sadece ihtiyaç noktalarını belirle (Depoları hariç tut)
need_point_columns = [col for col in distances_df.columns if 'Ihtiyac_Noktasi_' in col]
need_points_data = distances_df[~distances_df['Unnamed: 0'].str.contains('Depo_')][need_point_columns].values

# Küme sayısını tanımla
num_clusters = 5

# K-Means kümeleme algoritmasını çalıştır
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(need_points_data)

# Sadece ihtiyaç noktalarını al
need_points = distances_df[~distances_df['Unnamed: 0'].str.contains('Depo_')].copy()

# Küme sonuçlarını ekle
need_points['Cluster'] = cluster_labels

# Kümeleme sonuçlarını terminalde yazdır
print("\nKümeleme Sonuçları:")
for cluster in range(num_clusters):
    cluster_points = need_points.loc[need_points['Cluster'] == cluster, 'Unnamed: 0'].tolist()
    print(f"Küme {cluster + 1}: {cluster_points}")

# Depoların kolonlarını ayır
depot_columns = [col for col in distances_df.columns if "Depo_" in col]

# 1. Her küme için uygun depoyu belirle
cluster_to_depot = {}
for cluster in range(num_clusters):
    cluster_points = need_points.loc[need_points['Cluster'] == cluster, 'Unnamed: 0'].tolist()
    nearest_depots = {}
    for point in cluster_points:
        distances_to_depots = distances_df.loc[distances_df['Unnamed: 0'] == point, depot_columns]
        nearest_depots[point] = distances_to_depots.idxmin(axis=1).values[0]
    # Kümedeki en sık geçen depo
    common_depot = pd.Series(nearest_depots.values()).mode()[0]
    cluster_to_depot[cluster] = common_depot

# 2. Grafiği oluştur ve mesafe tablosunu ekle
graph = nx.DiGraph()  # Yönlü bir grafik oluştur
nodes = list(distances_df['Unnamed: 0'])
graph.add_nodes_from(nodes)

for i, source in enumerate(nodes):
    for j, target in enumerate(nodes):
        if i != j:  # Kendine döngüyü engelle
            distance = distances_df.iloc[i, j + 1]  # Mesafe değerlerini al
            graph.add_edge(source, target, weight=distance)

# 3. Rota ve mesafe hesaplama fonksiyonu

def calculate_dijkstra_route_and_distance(graph, depot_name, relevant_points):
    subgraph = graph.subgraph([depot_name] + relevant_points)
    shortest_paths = nx.single_source_dijkstra_path_length(subgraph, depot_name, weight="weight")
    route = [depot_name]
    visited = set(route)
    current_node = depot_name
    total_distance = 0

    while len(visited) < len(relevant_points) + 1:
        next_node = min(
            (node for node in relevant_points if node not in visited),
            key=lambda node: shortest_paths[node]
        )
        route.append(next_node)
        visited.add(next_node)
        total_distance += graph[current_node][next_node]['weight']
        current_node = next_node

    route.append(depot_name)
    total_distance += graph[current_node][depot_name]['weight']
    return route, total_distance

# 4. Drone yönetimi fonksiyonu

def manage_drone_for_route(route, allocation_df):
    drone_capacity = 30
    total_demand = 0
    drones_used = 0

    for point in route:
        if point.startswith('Depo'):  # Depo başlangıcı veya dönüşü
            continue
        # İlgili noktadaki toplam ihtiyacı al
        demand = allocation_df.loc[allocation_df['Need Point'] == point, 'Medical Demand'].sum() + \
                 allocation_df.loc[allocation_df['Need Point'] == point, 'Food Demand'].sum()
        total_demand += demand

    while total_demand > 0:
        drones_used += 1
        if total_demand <= drone_capacity:
            print(f"{drones_used}. Drone yola çıktı ve toplam {total_demand} birim ihtiyaç karşıladı.")
            break
        else:
            print(f"{drones_used}. Drone yola çıktı ve maksimum {drone_capacity} birim taşıdı.")
            total_demand -= drone_capacity

# 5. Her küme için işlemleri uygula
for cluster, depot in cluster_to_depot.items():
    cluster_points = need_points.loc[need_points['Cluster'] == cluster, 'Unnamed: 0'].tolist()
    print(f"\nKüme {cluster + 1} için en uygun depo: {depot}")
    print(f"Küme {cluster + 1} için noktalar: {cluster_points}")

    # Rota ve mesafe hesaplama
    route, total_distance = calculate_dijkstra_route_and_distance(graph, depot, cluster_points)
    print(f"Küme {cluster + 1} için hesaplanan rota: {route}")
    print(f"Küme {cluster + 1} için toplam mesafe: {total_distance:.2f} km")

    # Drone yönetimi
    manage_drone_for_route(route, allocation_df)