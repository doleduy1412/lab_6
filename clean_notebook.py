import nbformat as nbf

# Tên notebook hiện tại của bạn
# Nếu bạn đã đổi thành lab6_transformers.ipynb thì giữ nguyên
# Nếu vẫn tên khác (như "Bản_sao_của_Untitled6.ipynb"), sửa lại cho đúng
in_path = "lab6_transformers.ipynb"
out_path = "lab6_transformers_clean.ipynb"

# Đọc notebook
nb = nbf.read(in_path, as_version=4)

# Xoá metadata.widgets ở mức notebook nếu có
if "widgets" in nb.get("metadata", {}):
    print("Found notebook-level metadata.widgets -> removing it")
    del nb["metadata"]["widgets"]

# Xoá metadata.widgets ở từng cell nếu có
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell["metadata"]:
        print("Found cell-level widgets metadata -> removing it")
        del cell["metadata"]["widgets"]

# Ghi ra file mới
nbf.write(nb, out_path)
print(f"Saved cleaned notebook to: {out_path}")
