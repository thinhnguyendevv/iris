import streamlit as st
from iris_classifier import IrisClassifier

st.title("🌸 Dự đoán loài hoa Iris")

# Nhập liệu từ người dùng
sepal_length = st.slider("Chiều dài đài hoa (sepal length)", 4.0, 8.0, 5.1)
sepal_width  = st.slider("Chiều rộng đài hoa (sepal width)", 2.0, 4.5, 3.5)
petal_length = st.slider("Chiều dài cánh hoa (petal length)", 1.0, 7.0, 1.4)
petal_width  = st.slider("Chiều rộng cánh hoa (petal width)", 0.1, 2.5, 0.2)

# Dự đoán khi nhấn nút
if st.button("Dự đoán"):
    clf = IrisClassifier()
    result = clf.predict([sepal_length, sepal_width, petal_length, petal_width])
    st.success(f"🌼 Loài hoa dự đoán: **{result}**")

    # Hiển thị hình ảnh tương ứng
    if result == 0:
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/11/Iris_setosa_2.jpg", caption="Iris Setosa")
    elif result == 1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", caption="Iris Versicolor")
    elif result == 2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg", caption="Iris Virginica")
