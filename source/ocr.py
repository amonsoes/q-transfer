import cv2
import pytesseract as pyt


class CardProcessor:
    
    def __init__(self):
        self.char2num =  {
            'S':'5',
            'A':'4',
            'I':'1',
            'O':'0',
            'B':'8',
            'b':'6',
            'q':'9'
        }
        self.num2char = {num:char for char, num in self.char2num}
    
    def __call__(self, img):
        raw = pyt.image_to_string(img)
        details = {}
        for line in raw:
            if line.startswith('BIC'):
                details['BIC'] = line.split(':')[1]
            elif line.startswith('BAN') or line.startswith('IBAN'):
                details['IBAN'] = self.clean_iban(line.split(':')[1])
        return details
    
    def clean_iban(self, iban):
        country_code = iban[:2]
        number_code = iban[2:]
        return ''.join([self.num2char.get(num, num) for num in country_code]) + ''.join([self.char2num.get(char,char) for char in number_code])
        
    
if __name__ == '__main__':
    
    img = cv2.imread('./ex.JPG')
    print(pyt.image_to_string(img))
