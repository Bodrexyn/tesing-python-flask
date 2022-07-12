from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def run_model(X_train, X_test, y_train, y_test, array):
    # Membuat model Naive Bayes terhadap Training set
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Memprediksi hasil test set
    y_pred = model.predict(X_test)

    # Menghitung tingkat akurasi
    accuracy_score(y_test, y_pred)

    # Memasukkan data training pada fungsi klasifikasi naive bayes
    nbtrain = model.fit(X_train, y_train)

    # Menentukan hasil prediksi dari x_test
    y_pred = nbtrain.predict(X_test)
    # array = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    testing_pred = model.predict([array])

    return testing_pred