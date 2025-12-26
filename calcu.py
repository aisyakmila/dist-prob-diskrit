import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats

# ================== SIDEBAR ==================
st.sidebar.title("Distribusi Diskrit")
menu = st.sidebar.selectbox(
    "Pilih Distribusi",
    ["Home", "Binomial", "Hipergeometrik", "Geometrik", "Binomial Negatif", "Poisson"]
)

# ================== HOME ==================
if menu == "Home":
    st.title("Kalkulator Distribusi Probabilitas Diskrit")
    st.markdown("""
    Aplikasi ini menghitung:
    - **Probability Mass Function (PMF)**
    - **Cumulative Distribution Function (CDF)**

    untuk distribusi diskrit:
    1. Binomial  
    2. Hipergeometrik  
    3. Geometrik  
    4. Binomial Negatif  
    5. Poisson  
    """)

# ================== BINOMIAL ==================
elif menu == "Binomial":
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

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        st.subheader("Grafik PMF")
        st.bar_chart(df["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df["CDF"])

# ================== HIPERGEOMETRIK ==================
elif menu == "Hipergeometrik":
    st.title("Distribusi Hipergeometrik")

    N = st.number_input("Ukuran populasi (N)", min_value=1, value=50)
    K = st.number_input("Jumlah sukses di populasi (K)", min_value=1, value=20)
    n = st.number_input("Ukuran sampel (n)", min_value=1, value=10)
    x = st.number_input("Sukses dalam sampel (x)", min_value=0, value=0)

    if st.button("Hitung"):
        max_x = min(n, K)
        x_vals = np.arange(0, max_x + 1)

        pmf_vals = stats.hypergeom.pmf(x_vals, N, K, n)
        cdf_vals = stats.hypergeom.cdf(x_vals, N, K, n)

        st.success(f"PMF = {stats.hypergeom.pmf(x, N, K, n)}")
        st.info(f"CDF = {stats.hypergeom.cdf(x, N, K, n)}")

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        st.subheader("Grafik PMF")
        st.bar_chart(df["PMF"])

        st.subheader("Grafik CDF")
        st.line_chart(df["CDF"])

# ====
