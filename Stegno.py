from PIL import Image


class Stegno():
    
    def __init__(self, img):
        self.image = img
        self.width, self.height = img.size
        self.size = self.width * self.height
        self.maskOne = 128
        self.maskZero = 127

    
    def read_bit(self, data):
        newd = []
        
        for i in data:
            newd.append(format(ord(i), '08b'))
        
        return newd
    
    def encode_img(self, img, data):
        
        datalist = self.read_bit(data)
        datalen = len(datalist)
        
        if 8 *datalen > self.size:
            raise ValueError('data is too large for the image')
        
        imdata = iter(img.getdata())
        
        pix = []
        for i in range(8*datalen):  # Modifiation in each pixel as inserting single bit in a pixel i.e 8 times the length of the message
            pix.append(imdata.__next__())
        
        pix2 = []
    
        for i in range(datalen):
            for j in range(0, 8):
                if(datalist[i][j] == '0'):
                    pix2.append(pix[j] & self.maskZero)
                else:
                    pix2.append(pix[j] | self.maskOne)
        
        return pix2
    
    def encode_enc(self, img, data):
        (x, y) = (0, 0)
        
        for Pix_val in self.encode_img(img, data):
            img.putpixel((x,y), Pix_val)
            if( x == self.width - 1):
                x = 0
                y += 1
            else:
                x += 1
    
    def encode(self, img):
        data = input("Enter the data to be encoded: ")
        if(len(data) == 0):
            raise ValueError('data is Empty')
        
        newimg = img.copy()
        self.encode_enc(newimg, data)
        new_img_name = input("Enter the name of the new image:")
        newimg.save(new_img_name, str(new_img_name.split(".")[1]))
        
    def decode(self):
        img = input("Enter image name(with extension) :") 
        image = Image.open(img, 'r')
        
        data = '' 
        imgdata = iter(image.getdata()) 
        
        pixels = []
        while True:
            try:
                pixels.append(imgdata.__next__())
            except StopIteration:
                break
            
        binstr = ''
        for i in pixels:
            if(i & 128 == 0):
                binstr += '0'
            else:
                binstr += '1'
        
        data2 = []        
        for i in range(1000):
            data2.append(binstr[i * 8:(8 + i * 8)])
            data += chr(int(data2[i], 2))
        
        return data
    
        
    
        
    
