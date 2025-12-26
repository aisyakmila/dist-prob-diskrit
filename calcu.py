import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats

st.sidebar.title("Distribusi Diskrit")
test = st.sidebar.selectbox(
    "Pilih Distribusi",
    ["Home", "Binomial", "Hipergeometrik", "Geometrik", "Binomial Negatif", "Poisson"]
)

# ================= HOME =================
if test == "Home":
    st.title("Kalkulator Distribusi Probabilitas Diskrit")
    st.markdown("---")
    st.markdown("""
    Web ini digunakan untuk menghitung **Probability Mass Function (PMF)**
    dan **Cumulative Distribution Function (CDF)** dari beberapa distribusi diskrit:

    1. Binomial  
    2. Hipergeometrik  
    3. Geometrik  
    4. Binomial Negatif  
    5. Poisson  
    """)

# ================= BINOMIAL =================
elif test == "Binomial":
    st.title("Distribusi Binomial")

    n = st.number_input("Jumlah percobaan (n)", min_value=1, value=5, step=1)
    p = st.number_input("Peluang sukses (p)", min_value=0.0, max_value=1.0, value=0.5)
    x = st.number_input("Jumlah sukses (x)", min_value=0, max_value=n, value=0, step=1)

    if st.button("Hitung"):
        x_vals = np.arange(0, n + 1)
        pmf_vals = stats.binom.pmf(x_vals, n, p)
        cdf_vals = stats.binom.cdf(x_vals, n, p)

        st.success(f"PMF = {stats.binom.pmf(x, n, p)}")
        st.info(f"CDF = {stats.binom.cdf(x, n, p)}")

        df = pd.DataFrame({"x": x_vals, "PMF": pmf_vals, "CDF": cdf_vals})

        st.subheader("Grafik PMF")
        st.bar_chart(df.set_index("x")["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df.set_index("x")["CDF"])

# ================= HIPERGEOMETRIK =================
elif test == "Hipergeometrik":
    st.title("Distribusi Hipergeometrik")

    N = st.number_input("Populasi (N)", min_value=1, value=50)
    K = st.number_input("Jumlah sukses di populasi (K)", min_value=1, value=20)
    n = st.number_input("Ukuran sampel (n)", min_value=1, value=10)
    x = st.number_input("Sukses dalam sampel (x)", min_value=0, value=0)

    if st.button("Hitung"):
        x_vals = np.arange(0, min(n, K) + 1)
        pmf_vals = stats.hypergeom.pmf(x_vals, N, K, n)
        cdf_vals = stats.hypergeom.cdf(x_vals, N, K, n)

        st.success(f"PMF = {stats.hypergeom.pmf(x, N, K, n)}")
        st.info(f"CDF = {stats.hypergeom.cdf(x, N, K, n)}")

        df = pd.DataFrame({"x": x_vals, "PMF": pmf_vals, "CDF": cdf_vals})

        st.subheader("Grafik PMF")
        st.bar_chart(df.set_index("x")["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df.set_index("x")["CDF"])

# ================= GEOMETRIK =================
elif test == "Geometrik":
    st.title("Distribusi Geometrik")

    p = st.number_input("Peluang sukses (p)", min_value=0.0, max_value=1.0, value=0.5)
    x = st.number_input("Percobaan ke-x", min_value=1, value=1)

    if st.button("Hitung"):
        x_vals = np.arange(1, x + 10)
        pmf_vals = stats.geom.pmf(x_vals, p)
        cdf_vals = stats.geom.cdf(x_vals, p)

        st.success(f"PMF = {stats.geom.pmf(x, p)}")
        st.info(f"CDF = {stats.geom.cdf(x, p)}")

        df = pd.DataFrame({"x": x_vals, "PMF": pmf_vals, "CDF": cdf_vals})

        st.subheader("Grafik PMF")
        st.bar_chart(df.set_index("x")["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df.set_index("x")["CDF"])

# ================= BINOMIAL NEGATIF =================
elif test == "Binomial Negatif":
    st.title("Distribusi Binomial Negatif")

    r = st.number_input("Jumlah sukses (r)", min_value=1, value=3)
    p = st.number_input("Peluang sukses (p)", min_value=0.0, max_value=1.0, value=0.5)
    x = st.number_input("Jumlah kegagalan", min_value=0, value=0)

    if st.button("Hitung"):
        x_vals = np.arange(0, x + 15)
        pmf_vals = stats.nbinom.pmf(x_vals, r, p)
        cdf_vals = stats.nbinom.cdf(x_vals, r, p)

        st.success(f"PMF = {stats.nbinom.pmf(x, r, p)}")
        st.info(f"CDF = {stats.nbinom.cdf(x, r, p)}")

        df = pd.DataFrame({"x": x_vals, "PMF": pmf_vals, "CDF": cdf_vals})

        st.subheader("Grafik PMF")
        st.bar_chart(df.set_index("x")["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df.set_index("x")["CDF"])

# ================= POISSON =================
elif test == "Poisson":
    st.title("Distribusi Poisson")

    mu = st.number_input("Rata-rata kejadian (λ)", min_value=0.0, value=3.0)
    x = st.number_input("Jumlah kejadian (x)", min_value=0, value=0)

    if st.button("Hitung"):
        x_vals = np.arange(0, x + 15)
        pmf_vals = stats.poisson.pmf(x_vals, mu)
        cdf_vals = stats.poisson.cdf(x_vals, mu)

        st.success(f"PMF = {stats.poisson.pmf(x, mu)}")
        st.info(f"CDF = {stats.poisson.cdf(x, mu)}")

        df = pd.DataFrame({"x": x_vals, "PMF": pmf_vals, "CDF": cdf_vals})

        st.subheader("Grafik PMF")
        st.bar_chart(df.set_index("x")["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df.set_index("x")["CDF"])
