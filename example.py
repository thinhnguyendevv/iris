from iris_classifier import IrisClassifier

clf = IrisClassifier()
sample = [5.1, 3.5, 1.4, 0.2]
result = clf.predict(sample)
print("Input:", sample)
print("Predicted class:", result)
if st.button("Dự đoán"):
    clf = IrisClassifier()
    result = clf.predict([sepal_length, sepal_width, petal_length, petal_width])
    
    st.success(f"🌼 Loài hoa dự đoán: **{result}**")
    
    # Hiển thị ảnh minh họa
    if result == 'setosa':
        st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fvi.m.wikipedia.org%2Fwiki%2FT%25E1%25BA%25ADp_tin%3AIris_setosa_2.jpg&psig=AOvVaw3WfvMvBsjaoU60KZMCWkpd&ust=1746369028672000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNjiwN7Bh40DFQAAAAAdAAAAABAE", caption="Iris Setosa")
    elif result == 'versicolor':
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", caption="Iris Versicolor")
    elif result == 'virginica':
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg", caption="Iris Virginica")
