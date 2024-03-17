import ipywidgets as widgets
from IPython.display import display

# JanusScore formula
def calculate_janusscore(hx, hy):
    c = 0.005
    return hy * 10 * ((c + hx/hy)**0.3 - c**0.3) / 3

# widgets
hx_input = widgets.FloatText(value=1e7, description='VerusHash(CPU):')
hy_input = widgets.FloatText(value=1e8, description='SHA(GPU):')

calculate_button = widgets.Button(description="Calculate")

output = widgets.Output()

def on_calculate_button_clicked(b):
    hx = hx_input.value
    hy = hy_input.value
    result = calculate_janusscore(hx, hy)
    with output:
        output.clear_output()
        print(f"Result: {result:.2f}")

calculate_button.on_click(on_calculate_button_clicked)

display(widgets.VBox([hx_input, hy_input, calculate_button, output]))
