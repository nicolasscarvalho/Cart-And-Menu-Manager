from restaurant import GetRestaurantData, ProcessRestaurantData, ShowRestaurantData


data_denerator = GetRestaurantData()
data_process_engine = ProcessRestaurantData()
show_data_engine = ShowRestaurantData()

menu = data_denerator.get_menu_()

cart = data_process_engine.get_cart_(menu)
total_price = data_process_engine.get_total_price_(cart)

show_data_engine.show_order_(cart, total_price)