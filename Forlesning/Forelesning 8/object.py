class Color:
    def __init__(self, rgbvalue, colorname):
        
        # semi private
        self._rgbvalue = rgbvalue
        self._colorname = colorname
    
        
        # Public
        """ self.rgbvalue = rgbvalue
        self.colorname = colorname """
    
if __name__ == '__main__':
    c = Color(0xFF00FF, "lilla")
    
    #semi private
    print(c._rgbvalue)
    print(c._colorname)
    c._rgbvalue = 0x00FF00
    c._colorname = "grønn"
    print(c._rgbvalue)
    print(c._colorname)
    
    #Public
    """ print(c.rgbvalue)
    print(c.colorname)
    c.rgbvalue = 0x00FF00
    c.colorname = "grønn"
    print(c.rgbvalue)
    print(c.colorname) """
    