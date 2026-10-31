# Main app entry
import base64
import io
import re
import numpy as np
from PIL import Image, ImageOps
from flask import Flask, render_template, request, jsonify

from model import load_model

app = Flask(__name__)

# ----- Khởi tạo mô hình một lần khi server chạy -----
MODEL_PATH = "best_model.keras"
print(f"[INFO] Đang nạp mô hình từ: {MODEL_PATH}")
model = load_model(MODEL_PATH)
print("[INFO] Nạp mô hình thành công!")

# Hàm tiện xử lý ảnh từ canvas sang định dạng chuẩn MNIST
def preprocess_image(data_url: str) -> np.ndarray:
    """
    Nhận data URL base64 từ canvas (vd: 'data:image/png;base64,...')
    Trả về mảng numpy shape (1, 28, 28, 1) đã chuẩn hóa theo MNIST.
    """
    # 1) Tách base64
    match = re.match(r"data:image/png;base64,(.*)", data_url, re.DOTALL)
    if not match:
        raise ValueError("Dữ liệu ảnh không hợp lệ (phải là data URL PNG).")
    img_bytes = base64.b64decode(match.group(1))

    # 2) Đọc ảnh, chuyển grayscale
    img = Image.open(io.BytesIO(img_bytes)).convert("L")

    # 3) Canvas nền đen – nét trắng giống MNIST.
    #    Nếu nền sáng, đảo màu.
    arr = np.array(img)
    if arr.mean() > 127:
        img = ImageOps.invert(img)

    # 4) Cắt biên quanh nét vẽ
    bbox = img.getbbox()
    if bbox is None:
        raise ValueError("Canvas trống, chưa có nét vẽ nào.")
    img = img.crop(bbox)

    # 5) Resize về 20x20 giữ tỉ lệ, pad 4px mỗi cạnh -> 28x28 (chuẩn MNIST)
    w, h = img.size
    if w > h:
        new_w, new_h = 20, int(round(h * 20 / w))
    else:
        new_h, new_w = 20, int(round(w * 20 / h))
    img = img.resize((new_w, new_h), Image.LANCZOS)

    canvas28 = Image.new("L", (28, 28), 0)
    canvas28.paste(img, ((28 - new_w) // 2, (28 - new_h) // 2))

    # 6) Chuẩn hóa [0,255] -> [0,1]
    arr = np.array(canvas28, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=-1)   # (28,28,1)
    arr = np.expand_dims(arr, axis=0)    # (1,28,28,1)
    return arr


@app.route("/", methods=["GET"])
def index():
    return render_template("digits.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data or "image" not in data:
            return jsonify({"error": "Thiếu dữ liệu 'image'."}), 400

        x = preprocess_image(data["image"])

        # Dự đoán
        probs = model.predict(x, verbose=0)[0]      # vector 10 phần tử
        pred = int(np.argmax(probs))
        confidence = float(probs[pred])

        return jsonify({
            "prediction": pred,
            "confidence": round(confidence * 100, 2),
            "probabilities": [round(float(p) * 100, 2) for p in probs]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)