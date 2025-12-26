import streamlit as st
import pandas as pd
from scipy.stats import binom

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Distribusi Probabilitas Diskrit",
    page_icon="📊",
    layout="centered"
)

# =========================
# HEADER
# =========================
st.title("📊 Distribusi Probabilitas Diskrit")
st.subheader("Distribusi Binomial")
st.caption("Menampilkan PMF dan CDF beserta grafiknya")

st.divider()

# =========================
# SIDEBAR INPUT
# =========================
st.sidebar.header("⚙️ Parameter Distribusi")

n = st.sidebar.number_input(
    "Banyaknya Percobaan (n)",
    min_value=1,
    step=1,
    value=1
)

p = st.sidebar.slider(
    "Peluang Kejadian Sukses (p)",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

x = st.sidebar.number_input(
    "Jumlah Kejadian (x)",
    min_value=0,
    max_value=n,
    step=1,
    value=0
)

# =========================
# PERHITUNGAN
# =========================
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

# =========================
# OUTPUT NILAI
# =========================
col1, col2 = st.columns(2)

with col1:
    st.metric("📌 PMF", round(pmf, 6))

with col2:
    st.metric("📌 CDF", round(cdf, 6))

st.info("PMF menunjukkan peluang tepat pada nilai x, sedangkan CDF menunjukkan peluang kumulatif hingga x.")

st.divider()

# =========================
# DATA UNTUK GRAFIK
# =========================
x_values = list(range(0, n + 1))
pmf_values = binom.pmf(x_values, n, p)
cdf_values = binom.cdf(x_values, n, p)

df_pmf = pd.DataFrame({
    "x": x_values,
    "PMF": pmf_values
}).set_index("x")

df_cdf = pd.DataFrame({
    "x": x_values,
    "CDF": cdf_values
}).set_index("x")

# =========================
# TABS GRAFIK
# =========================
tab1, tab2 = st.tabs(["📊 Grafik PMF", "📈 Grafik CDF"])

with tab1:
    st.subheader("Grafik Probability Mass Function (PMF)")
    st.bar_chart(df_pmf)

with tab2:
    st.subheader("Grafik Cumulative Distribution Function (CDF)")
    st.line_chart(df_cdf)

# =========================
# FOOTER
# =========================
st.divider()
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")
