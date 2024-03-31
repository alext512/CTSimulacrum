# In controller/main_controller.py

class MainController:
    def __init__(self, gui):
        self.gui = gui

    def processImagePath(self, imagePath):
        print(f"Controller received image path: {imagePath}")
        # Simulate processing and tell the GUI to display images
        # In a real scenario, this would involve image loading and processing logic
        self.gui.displayImages(imagePath, imagePath)
