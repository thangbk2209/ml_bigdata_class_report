## I) Cấu trúc file data
+ Tên file data: **_Loại model_** + **_tên model_** + **_số lượng hidden unit_**
+ Vd: _**pretraining_stae_hidden_1**_: Pretraining STAE với hidden size ở mỗi layer = 1
+ Mỗi file data là  1 bảng 30 * 5 trong đó:
    + 5 cột là model với số lượng hidden layer tương ứng:
    + 30 hàng là  30 kết quả MAE của tập test với model tương ứng
+ Vd:
    | 1_layer | 2_layer | 3_layer | 4_layer | 5_layer |
    |---------|---------|---------|---------|---------|
    | 3       | 2       | 1       | 5       | 1       |
    | 1       | 3       | 2       | 3       | 2       |
    | 4       | 3       | 4       | 3       | 1       |

## II) Cách chạy chương trình
### 1) Vẽ biểu đồ box plot (hình 1 trong paper):
+ Chạy script **plotbox_script.py**, truyền tham số đầu vào là tên model, loại model, hidden size
+ Output được lưu vào thư mục result với tên tướng ứng với tham số đầu vào.

### 2) Vẽ biểu đồ histogram (hình 2a, 2b trong paper):
+ Chạy script **plothist_script.py**, truyền tham số đầu vào là tên model, hidden size, layer size
+ Output được lưu vào thư mục result với tên tướng ứng với tham số đầu vào.
+ Chú ý tham số  **bins**, có thể điều chỉnh **bin** cho phù hợp.