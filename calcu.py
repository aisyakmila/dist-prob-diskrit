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
st.sidebar.title("📊 Distribusi Diskrit")
menu = st.sidebar.selectbox(
    "Pilih Distribusi",
    ["Home", "Binomial", "Hipergeometrik", "Geometrik", "Binomial Negatif", "Poisson"]
)

st.sidebar.markdown("---")
st.sidebar.caption("PMF & CDF Visualizer")

# ================== HOME ==================
if menu == "Home":
    st.title("📊 Kalkulator Distribusi Probabilitas Diskrit")
    st.markdown("""
    Aplikasi ini digunakan untuk menghitung dan memvisualisasikan:

    - **Probability Mass Function (PMF)**
    - **Cumulative Distribution Function (CDF)**

    dari beberapa distribusi diskrit berikut:
    1. Distribusi Binomial  
    2. Distribusi Hipergeometrik  
    3. Distribusi Geometrik  
    4. Distribusi Binomial Negatif  
    5. Distribusi Poisson  
    """)
    st.info("Silakan pilih jenis distribusi pada sidebar.")

# ================== BINOMIAL ==================
elif menu == "Binomial":
    st.title("Distribusi Binomial")

    n = st.sidebar.number_input("Jumlah Percobaan (n)", min_value=1, value=5, step=1)
    p = st.sidebar.slider("Peluang Sukses (p)", 0.0, 1.0, 0.5)
    x = st.sidebar.number_input("Jumlah Sukses (x)", min_value=0, max_value=n, value=0)

    if st.sidebar.button("🔢 Hitung"):
        x_vals = np.arange(0, n + 1)
        pmf_vals = stats.binom.pmf(x_vals, n, p)
        cdf_vals = stats.binom.cdf(x_vals, n, p)

        col1, col2 = st.columns(2)
        col1.metric("PMF", round(stats.binom.pmf(x, n, p), 6))
        col2.metric("CDF", round(stats.binom.cdf(x, n, p), 6))

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        tab1, tab2 = st.tabs(["📊 Grafik PMF", "📈 Grafik CDF"])
        tab1.bar_chart(df["PMF"])
        tab2.line_chart(df["CDF"])

# ================== HIPERGEOMETRIK ==================
elif menu == "Hipergeometrik":
    st.title("Distribusi Hipergeometrik")

    N = st.sidebar.number_input("Ukuran Populasi (N)", min_value=1, value=50)
    K = st.sidebar.number_input("Jumlah Sukses di Populasi (K)", min_value=1, value=20)
    n = st.sidebar.number_input("Ukuran Sampel (n)", min_value=1, value=10)
    x = st.sidebar.number_input("Sukses dalam Sampel (x)", min_value=0, value=0)

    if st.sidebar.button("🔢 Hitung"):
        max_x = min(n, K)
        x_vals = np.arange(0, max_x + 1)

        pmf_vals = stats.hypergeom.pmf(x_vals, N, K, n)
        cdf_vals = stats.hypergeom.cdf(x_vals, N, K, n)

        col1, col2 = st.columns(2)
        col1.metric("PMF", round(stats.hypergeom.pmf(x, N, K, n), 6))
        col2.metric("CDF", round(stats.hypergeom.cdf(x, N, K, n), 6))

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        tab1, tab2 = st.tabs(["📊 Grafik PMF", "📈 Grafik CDF"])
        tab1.bar_chart(df["PMF"])
        tab2.line_chart(df["CDF"])

# ================== GEOMETRIK ==================
elif menu == "Geometrik":
    st.title("Distribusi Geometrik")

    p = st.sidebar.slider("Peluang Sukses (p)", 0.0, 1.0, 0.5)
    x = st.sidebar.number_input("Percobaan ke-x", min_value=1, value=1)

    if st.sidebar.button("🔢 Hitung"):
        x_vals = np.arange(1, x + 15)

        pmf_vals = stats.geom.pmf(x_vals, p)
        cdf_vals = stats.geom.cdf(x_vals, p)

        col1, col2 = st.columns(2)
        col1.metric("PMF", round(stats.geom.pmf(x, p), 6))
        col2.metric("CDF", round(stats.geom.cdf(x, p), 6))

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        tab1, tab2 = st.tabs(["📊 Grafik PMF", "📈 Grafik CDF"])
        tab1.bar_chart(df["PMF"])
        tab2.line_chart(df["CDF"])

# ================== BINOMIAL NEGATIF ==================
elif menu == "Binomial Negatif":
    st.title("Distribusi Binomial Negatif")

    r = st.sidebar.number_input("Jumlah Sukses (r)", min_value=1, value=3)
    p = st.sidebar.slider("Peluang Sukses (p)", 0.0, 1.0, 0.5)
    x = st.sidebar.number_input("Jumlah Kegagalan", min_value=0, value=0)

    if st.sidebar.button("🔢 Hitung"):
        x_vals = np.arange(0, x + 15)

        pmf_vals = stats.nbinom.pmf(x_vals, r, p)
        cdf_vals = stats.nbinom.cdf(x_vals, r, p)

        col1, col2 = st.columns(2)
        col1.metric("PMF", round(stats.nbinom.pmf(x, r, p), 6))
        col2.metric("CDF", round(stats.nbinom.cdf(x, r, p), 6))

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        tab1, tab2 = st.tabs(["📊 Grafik PMF", "📈 Grafik CDF"])
        tab1.bar_chart(df["PMF"])
        tab2.line_chart(df["CDF"])

# ================== POISSON ==================
elif menu == "Poisson":
    st.title("Distribusi Poisson")

    mu = st.sidebar.number_input("Rata-rata Kejadian (λ)", min_value=0.0, value=3.0)
    x = st.sidebar.number_input("Jumlah Kejadian (x)", min_value=0, value=0)

    if st.sidebar.button("🔢 Hitung"):
        x_vals = np.arange(0, x + 15)

        pmf_vals = stats.poisson.pmf(x_vals, mu)
        cdf_vals = stats.poisson.cdf(x_vals, mu)

        col1, col2 = st.columns(2)
        col1.metric("PMF", round(stats.poisson.pmf(x, mu), 6))
        col2.metric("CDF", round(stats.poisson.cdf(x, mu), 6))

        df = pd.DataFrame({"PMF": pmf_vals, "CDF": cdf_vals}, index=x_vals)

        tab1, tab2 = st.tabs(["📊 Grafik PMF", "📈 Grafik CDF"])
        tab1.bar_chart(df["PMF"])
        tab2.line_chart(df["CDF"])

st.divider()
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")
