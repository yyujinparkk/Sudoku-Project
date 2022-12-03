class Cow:

    def __init__(self, name):       # Initializes a cow object with name and image to be None
        self.name = name
        self.image = None

    def get_name(self):     # Returns the name of the cow.
        return self.name

    def get_image(self):        # Returns the image used to display the cow
        return self.image

    def set_image(self, image):     # Sets the image used to display the cow
        self.image = image
