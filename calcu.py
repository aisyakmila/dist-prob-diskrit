import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Distribusi Probabilitas Diskrit",
    page_icon="📊",
    layout="centered"
)

# ================== SIDEBAR ==================
st.sidebar.title("📌 Distribusi Diskrit")
menu = st.sidebar.selectbox(
    "Pilih Distribusi",
    ["Home", "Binomial", "Hipergeometrik", "Geometrik", "Binomial Negatif", "Poisson"]
)

# ================== HOME ==================
if menu == "Home":
    st.title("📊 Kalkulator Distribusi Probabilitas Diskrit")
    st.markdown("""
    Aplikasi ini menghitung **Probability Mass Function (PMF)** dan  
    **Cumulative Distribution Function (CDF)** untuk distribusi diskrit:

    1. Distribusi Binomial  
    2. Distribusi Hipergeometrik  
    3. Distribusi Geometrik  
    4. Distribusi Binomial Negatif  
    5. Distribusi Poisson  
    """)
    st.caption("Gunakan menu di samping untuk mulai menghitung 📈")

# ================== BINOMIAL ==================
elif menu == "Binomial":
    st.title("Distribusi Binomial")

    n = st.number_input("Jumlah percobaan (n)", min_value=1, value=5, step=1)
    p = st.slider("Peluang sukses (p)", 0.0, 1.0, 0.5)
    x = st.number_input("Jumlah sukses (x)", min_value=0, max_value=n, value=0, step=1)

    if st.button("Hitung"):
        x_vals = np.arange(0, n + 1)
        pmf_vals = stats.binom.pmf(x_vals, n, p)
        cdf_vals = stats.binom.cdf(x_vals, n, p)

        st.success(f"PMF(x = {x}) = {stats.binom.pmf(x, n, p):.6f}")
        st.info(f"CDF(x ≤ {x}) = {stats.binom.cdf(x, n, p):.6f}")

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Grafik PMF")
            st.bar_chart(df["PMF"])
        with col2:
            st.subheader("📈 Grafik CDF")
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

        st.success(f"PMF(x = {x}) = {stats.hypergeom.pmf(x, N, K, n):.6f}")
        st.info(f"CDF(x ≤ {x}) = {stats.hypergeom.cdf(x, N, K, n):.6f}")

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Grafik PMF")
            st.bar_chart(df["PMF"])
        with col2:
            st.subheader("📈 Grafik CDF")
            st.line_chart(df["CDF"])

# ================== GEOMETRIK ==================
elif menu == "Geometrik":
    st.title("Distribusi Geometrik")

    p = st.slider("Peluang sukses (p)", 0.0, 1.0, 0.5)
    x = st.number_input("Percobaan ke-x", min_value=1, value=1)

    if st.button("Hitung"):
        x_vals = np.arange(1, x + 10)

        pmf_vals = stats.geom.pmf(x_vals, p)
        cdf_vals = stats.geom.cdf(x_vals, p)

        st.success(f"PMF(x = {x}) = {stats.geom.pmf(x, p):.6f}")
        st.info(f"CDF(x ≤ {x}) = {stats.geom.cdf(x, p):.6f}")

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Grafik PMF")
            st.bar_chart(df["PMF"])
        with col2:
            st.subheader("📈 Grafik CDF")
            st.line_chart(df["CDF"])

# ================== BINOMIAL NEGATIF ==================
elif menu == "Binomial Negatif":
    st.title("Distribusi Binomial Negatif")

    r = st.number_input("Jumlah sukses (r)", min_value=1, value=3)
    p = st.slider("Peluang sukses (p)", 0.0, 1.0, 0.5)
    x = st.number_input("Jumlah kegagalan", min_value=0, value=0)

    if st.button("Hitung"):
        x_vals = np.arange(0, x + 15)

        pmf_vals = stats.nbinom.pmf(x_vals, r, p)
        cdf_vals = stats.nbinom.cdf(x_vals, r, p)

        st.success(f"PMF(x = {x}) = {stats.nbinom.pmf(x, r, p):.6f}")
        st.info(f"CDF(x ≤ {x}) = {stats.nbinom.cdf(x, r, p):.6f}")

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Grafik PMF")
            st.bar_chart(df["PMF"])
        with col2:
            st.subheader("📈 Grafik CDF")
            st.line_chart(df["CDF"])

# ================== POISSON ==================
elif menu == "Poisson":
    st.title("Distribusi Poisson")

    mu = st.number_input("Rata-rata kejadian (λ)", min_value=0.0, value=3.0)
    x = st.number_input("Jumlah kejadian (x)", min_value=0, value=0)

    if st.button("Hitung"):
        x_vals = np.arange(0, x + 15)

        pmf_vals = stats.poisson.pmf(x_vals, mu)
        cdf_vals = stats.poisson.cdf(x_vals, mu)

        st.success(f"PMF(x = {x}) = {stats.poisson.pmf(x, mu):.6f}")
        st.info(f"CDF(x ≤ {x}) = {stats.poisson.cdf(x, mu):.6f}")

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Grafik PMF")
            st.bar_chart(df["PMF"])
        with col2:
            st.subheader("📈 Grafik CDF")
            st.line_chart(df["CDF"])

# ================== FOOTER ==================
st.divider()
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")
