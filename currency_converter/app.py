import dearpygui.dearpygui as dpg
import model

dpg.create_context()
dpg.create_viewport(title='Currency Converter', width=600, height=300)

with dpg.window(label="Currency Converter",width=600,height=300):
    dpg.add_text("Welcome to the Currency Converter.")
    dpg.add_input_float(label="Amount", default_value=1.0,width=100)
    dpg.add_combo(model.currencies, default_value=model.default_from,label="From",
        width=250)
    dpg.add_combo(model.currencies,label="To",
        width=250,default_value=model.default_to)
    dpg.add_button(label="Convert")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()