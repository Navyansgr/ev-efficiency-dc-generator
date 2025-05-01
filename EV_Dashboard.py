# File: EV_Dashboard.py
import panel as pn
import matplotlib.pyplot as plt
import numpy as np
pn.extension()

# Controls
gear = pn.widgets.IntSlider(name="Gear Ratio", value=5, start=1, end=10)
rpm = pn.widgets.IntSlider(name="Motor RPM", value=800, start=500, end=1200)

# Simple Plot for Testing
def create_plot(params):
    ratios = np.arange(1, 11)
    gen_rpm = ratios * params['rpm']
    fig, ax = plt.subplots()
    ax.plot(ratios, gen_rpm, 'ro-')
    ax.set_title(f"Gear {params['gear']}:1 → {gen_rpm[-1]} RPM")
    plt.close()
    return fig

# Layout
dashboard = pn.Row(
    pn.Column(gear, rpm),
    pn.pane.Matplotlib(pn.bind(create_plot, params=pn.bind(dict, gear=gear, rpm=rpm))
)

dashboard.servable()