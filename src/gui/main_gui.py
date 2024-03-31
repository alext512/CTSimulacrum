from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectEntry, DirectButton, DirectFrame, OnscreenImage
from panda3d.core import TransparencyAttrib, LVector3, Texture
from controller.main_controller import MainController

class MainGUI(ShowBase):
    def __init__(self):
        super().__init__()
        # Controller setup
        self.controller = MainController(self)

        self.title = "CTSimulacrum"
        self.setBackgroundColor(0.1, 0.1, 0.1, 1)  # Dark background for dramatic effect

        # Input Field for Image Path
        self.entry = DirectEntry(text="", scale=0.05, pos=(-0.9, 0, 0.9), initialText="", numLines=1, width=20, overflow=True)

        
        # Load Button
        self.loadButton = DirectButton(text="Load", scale=0.05, pos=(-0.7, 0, 0.85), command=self.onLoadButtonClick)

        # Placeholder Frames for Images
        self.leftImageFrame = DirectFrame(frameColor=(0, 0, 0, 1), frameSize=(-0.4, 0.4, -0.4, 0.4), pos=(-0.5, 0, 0))
        self.rightImageFrame = DirectFrame(frameColor=(0, 0, 0, 1), frameSize=(-0.4, 0.4, -0.4, 0.4), pos=(0.5, 0, 0))
        
        # For demonstration, no images will be loaded initially
        self.leftImage = None
        self.rightImage = None

    def onLoadButtonClick(self):
        # Pass the path to the controller
        imagePath = self.entry.get()
        print(f"GUI passing path to controller: {imagePath}")
        self.controller.processImagePath(imagePath)



    def displayImages(self, leftImagePath, rightImagePath):
        # Remove existing images if any
        if self.leftImage:
            self.leftImage.destroy()
        if self.rightImage:
            self.rightImage.destroy()
        
        # Load and display the new images with nearest filtering
        self.leftImage = OnscreenImage(parent=self.leftImageFrame, image=leftImagePath, pos=LVector3(0, 0, 0), scale=0.4)
        self.leftImage.setTransparency(TransparencyAttrib.MAlpha)
        leftTexture = self.leftImage.getTexture()
        leftTexture.setMinfilter(Texture.FTNearest)
        leftTexture.setMagfilter(Texture.FTNearest)

        self.rightImage = OnscreenImage(parent=self.rightImageFrame, image=rightImagePath, pos=LVector3(0, 0, 0), scale=0.4)
        self.rightImage.setTransparency(TransparencyAttrib.MAlpha)
        rightTexture = self.rightImage.getTexture()
        rightTexture.setMinfilter(Texture.FTNearest)
        rightTexture.setMagfilter(Texture.FTNearest)

if __name__ == "__main__":
    guiApp = MainGUI()
    guiApp.run()
