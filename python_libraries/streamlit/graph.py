import streamlit as sl
from matplotlib import pyplot as plt
import numpy as np

sl.title("Graphs")
sl.markdown("---")
sl.sidebar.markdown("<h1>Side Bar</h1>", unsafe_allow_html=True)
x = np.linspace(0, 10, 100)
opt = sl.sidebar.radio("select graph", options=("line", "bar", "H-bar"))
if opt == "line":
    fig = plt.figure()
    plt.style.use('ggplot')
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    sl.write(fig)


