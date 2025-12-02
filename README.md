# Phần mềm tìm đường đi trên bản đồ phường Giảng Võ - Nhóm 19

Đây là bài tập lớn môn **Nhập môn Trí tuệ Nhân tạo**.
Ứng dụng sử dụng thuật toán **A*** để tìm đường đi ngắn nhất và nhanh nhất giữa hai điểm trên bản đồ thực tế của phường Giảng Võ, Ba Đình, Hà Nội.

## 📋 Yêu cầu hệ thống

* Hệ điều hành: Windows, MacOS hoặc Linux.
* **Miniconda** hoặc **Anaconda** (Khuyên dùng để cài đặt thư viện `osmnx` không bị lỗi).
* Trình duyệt web (Chrome, Edge, Firefox...).

## 🚀 Hướng dẫn cài đặt

### Bước 1: Cài đặt môi trường

Mở **Anaconda Prompt** (hoặc Terminal trong VSCode) và chạy lần lượt các lệnh sau:

1. **Tạo môi trường ảo** (đặt tên là `map_giangvo`, python phiên bản 3.12):
   ```bash
   conda create -n map_giangvo python=3.12
2. **Kích hoạt môi trường:**

```Bash

conda activate map_giangvo
```
3. **Cài đặt các thư viện chính** (qua kênh conda-forge để ổn định nhất):
```
Bash

conda install -c conda-forge osmnx folium streamlit
```
4. **Cài đặt thư viện bổ trợ** (fix lỗi Import "streamlit_folium" could not be resolved):
```
Bash

pip install streamlit-folium
```
### Bước 2: Chuẩn bị dữ liệu bản đồ
Do bản đồ mặc định trong code cũ là Phương Mai, bạn cần tải bản đồ Giảng Võ về.

Đảm bảo file get_map.py đã có trong thư mục (nội dung lấy theo tọa độ hồ Giảng Võ).

Chạy lệnh sau để tải dữ liệu về file giangvo.graphml:
```
Bash

python get_map.py
```
Nếu thấy thông báo "Đã lưu bản đồ thành công: giangvo.graphml" là hoàn tất.

### Hướng dẫn chạy ứng dụng:

Sau khi đã cài đặt xong, mỗi lần muốn sử dụng, bạn làm như sau:

Mở Terminal tại thư mục dự án.

Kích hoạt môi trường (nếu chưa):
```
Bash

conda activate map_giangvo
```
Chạy ứng dụng bằng Streamlit:

```Bash

streamlit run map_app.py
```

Trình duyệt sẽ tự động mở địa chỉ http://localhost:8501 và hiển thị bản đồ.

🛠 Khắc phục lỗi thường gặp
1. Lỗi 'conda' is not recognized

Nguyên nhân: Chưa cài Miniconda hoặc chưa thêm vào PATH của Windows.

Khắc phục: Cài lại Miniconda và tích vào ô "Add Miniconda3 to my PATH environment variable" hoặc dùng Anaconda Prompt để chạy lệnh.

2. Lỗi Found no graph nodes within the requested polygon khi chạy get_map.py

Nguyên nhân: OpenStreetMap không tìm thấy ranh giới tên phường chính xác.

Khắc phục: Sử dụng hàm ox.graph_from_point với tọa độ (21.0287, 105.8192) thay vì tìm theo tên.

3. Lỗi ModuleNotFoundError: No module named 'streamlit_folium'

Khắc phục: Chạy lệnh pip install streamlit-folium.


---
👥 Thông tin nhóm
Môn học: Nhập môn Trí tuệ Nhân tạo

Mã lớp: 

Giảng viên: PGS.TS Trần Đình Khang

Nhóm thực hiện: 5