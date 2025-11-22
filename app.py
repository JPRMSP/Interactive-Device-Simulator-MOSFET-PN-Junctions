import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🛠 Interactive Device Simulator: MOSFET & PN Junctions")

# ----------------- MOSFET Simulation -----------------
st.header("MOSFET I-V Characteristics")
Vgs = st.slider("Gate-Source Voltage Vgs (V)", 0.0, 5.0, 1.0, 0.1)
Vds_max = st.slider("Max Drain-Source Voltage Vds (V)", 0.0, 5.0, 2.0, 0.1)
Vds = np.linspace(0, Vds_max, 200)
# MOSFET Parameters
Vth = st.number_input("Threshold Voltage Vth (V)", 0.5, 2.0, 1.0)
Kn = st.number_input("Transconductance parameter Kn (mA/V^2)", 50, 500, 100)

# MOSFET I-V equation (simplified)
Ids = np.where(Vds < (Vgs - Vth),
               Kn * ((Vgs - Vth) * Vds - 0.5 * Vds**2),
               0.5 * Kn * (Vgs - Vth)**2)

fig1, ax1 = plt.subplots()
ax1.plot(Vds, Ids)
ax1.set_title("MOSFET I-V Curve")
ax1.set_xlabel("Vds (V)")
ax1.set_ylabel("Ids (mA)")
st.pyplot(fig1)

# ----------------- PN Junction Simulation -----------------
st.header("PN Junction Characteristics")
Is = st.number_input("Saturation Current Is (A)", 1e-12, 1e-6, 1e-12, format="%.1e")
V = np.linspace(-0.5, 0.7, 200)
I = Is * (np.exp(38.92 * V) - 1)  # Shockley equation, VT~26mV, simplified for room temp

fig2, ax2 = plt.subplots()
ax2.plot(V, I)
ax2.set_title("PN Junction I-V Curve")
ax2.set_xlabel("Voltage V (V)")
ax2.set_ylabel("Current I (A)")
ax2.grid(True)
st.pyplot(fig2)

# ----------------- Doping Profile -----------------
st.header("Doping Profile")
Nd = st.slider("Donor Concentration Nd (10^15 cm^-3)", 1, 100, 10)
Na = st.slider("Acceptor Concentration Na (10^15 cm^-3)", 1, 100, 10)
x = np.linspace(0, 1e-4, 200)  # position in cm
N = Nd * (x < 0.5e-4) + Na * (x >= 0.5e-4)

fig3, ax3 = plt.subplots()
ax3.plot(x*1e4, N)
ax3.set_title("Doping Profile")
ax3.set_xlabel("Position (µm)")
ax3.set_ylabel("Doping Concentration (10^15 cm^-3)")
st.pyplot(fig3)
