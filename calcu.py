import streamlit as st
import numpy as np

test = st.sidebar.selectbox("Distribusi Diskrit", ['Home', 'Binomial', 'Hipergeometrik', 'Geometrik', 'Binomial Negatif','Poisson'])

if (test == "Home"):
    st.title("Menghitung Probabilitas Distribusi Diskrit")
    st.markdown("---")
    st.markdown("""
        Distribusi probabilitas diskrit adalah suatu daftar atau distribusi di mana variabel 
        randomnya mengasumsikan masing-masing nilainya dengan probabilitas tertentu. Variabel 
        diskrit memiliki jumlah nilai kemungkinan yang terbatas atau jumlah yang tak terhingga 
        dari nilai-nilai yang dapat dihitung
        
        Melalui web apps ini anda dapat menghitung probabilitas dari beberapa macam
        distribusi probabilitas diskrit, yaitu
        1. Distribusi Binomial
        2. Hipergeometrik
        3. Geometrik
        4. Binomial Negatif
        5. Poisson

        """)

if (test == "Binomial"):
    st.title("Distribusi Binomial")

    n = st.number_input("Banyaknya Percobaan (n)", value=1, min_value=1, step=1)
    p = st.number_input("Peluang Kejadian Sukses (p)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    x = st.number_input("Jumlah Kejadian (x)", value=0, min_value=0, step=1)
    hitung = st.button ("Hitung Probabilitas")

    if hitung :
        pmf = stats.binom.pmf(x, n, p)
        cdf = stats.binom.cdf(x, n, p)

        st.write("Probability Mass Function (PMF):", pmf)
        st.write("Cumulative Distribution Function (CDF):", cdf)

if (test == "Hipergeometrik"):
    st.title("Distribusi Hipergeometrik")

    N = st.number_input("Jumlah Populasi (N)", value=100, min_value=1, step=1)
    K = st.number_input("Jumlah Sukses dalam Populasi (K)", value=50, min_value=1, step=1)
    n = st.number_input("Jumlah Sampel (n)", value=10, min_value=1, step=1)
    x = st.number_input("Banyaknya Sukses dalam Sampel (x)", value=0, min_value=0, step=1)
    hitung = st.button ("Hitung Probabilitas")

    if hitung :
        pmf = stats.hypergeom.pmf(x, N, K, n)
        cdf = stats.hypergeom.cdf(x, N, K, n)

        st.write("Probability Mass Function (PMF):", pmf)
        st.write("Cumulative Distribution Function (CDF):", cdf)

if (test == "Geometrik"):
    st.title("Distribusi Geometrik")

    p = st.number_input("Probabilitas Sukses (p)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    x = st.number_input("Banyaknya Percobaan sampai Sukses Pertama (x)", value=1, min_value=1, step=1)
    hitung = st.button ("Hitung Probabilitas")

    if hitung :
        pmf = stats.geom.pmf(x, p)
        cdf = stats.geom.cdf(x, p)

        st.write("Probability Mass Function (PMF):", pmf)
        st.write("Cumulative Distribution Function (CDF):", cdf)

if (test == "Binomial Negatif"):
    st.title("Distribusi Binomial Negatif")

    n = st.number_input("Jumlah Sukses yang Muncul (k)", value=1, min_value=1, step=1)
    p = st.number_input("Peluang Sukses (p)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    x = st.number_input("Jumla Percobaan Sampai Mendapatkan Sukses ke-k (x)", value=0, min_value=0, step=1)
    hitung = st.button ("Hitung Probabilitas")

    if hitung :
        pmf = stats.nbinom.pmf(x, n, p)
        cdf = stats.nbinom.cdf(x, n, p)

        st.write("Probability Mass Function (PMF):", pmf)
        st.write("Cumulative Distribution Function (CDF):", cdf)

if test == "Poisson":
    st.title("Distribusi Poisson")

    mu = st.number_input("Rata-rata kejadian sukses (lambda)", value=1.0, min_value=0.0, step=0.01)
    x = st.number_input("Banyaknya Sukses yang terjadi dalam suatu selan waktu (x)", value=0, min_value=0, step=1)
    hitung = st.button ("Hitung Probabilitas")

    if hitung :
        pmf = stats.poisson.pmf(x, mu)
        cdf = stats.poisson.cdf(x, mu)

        st.write("Probability Mass Function (PMF):", pmf)
        st.write("Cumulative Distribution Function (CDF):", cdf)
