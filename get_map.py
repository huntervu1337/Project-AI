import osmnx as ox

# Tọa độ trung tâm phường Giảng Võ (khu vực hồ Giảng Võ)
# Lat: 21.0287, Lon: 105.8192
point = (21.0287, 105.8192)

print(f"Đang tải bản đồ xung quanh tọa độ: {point}...")

try:
    # Tải bản đồ trong bán kính 1000m (1km) tính từ tâm
    # Bạn có thể tăng 'dist' lên 1500 hoặc 2000 nếu muốn bản đồ rộng hơn
    G = ox.graph_from_point(point, dist=2000, network_type='all')
    
    # Lưu thành file .graphml
    output_file = "giangvo.graphml"
    ox.save_graphml(G, filepath=output_file)
    print(f"Đã lưu bản đồ thành công: {output_file}")
    print(f"Tổng số nút (giao lộ): {len(G.nodes)}")
    
except Exception as e:
    print(f"Lỗi: {e}")