from ui.intro_animation import play_intro_animation
from ui.main_ui import MainUI
from logic.logic_layer_api import LogicLayerAPI
from data.data_layer_api import DataLayerAPI

def main():
    """Entry point for the Banking System application"""
    # Initialize data and logic layers
    data_layer = DataLayerAPI()
    logic_layer = LogicLayerAPI(data_layer)
    # play_intro_animation()
    ui = MainUI(logic_layer)
    ui.run()

    
if __name__ == "__main__":
    main()
