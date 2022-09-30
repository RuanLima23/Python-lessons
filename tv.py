class tv:
    def __init__(self):
        self.ligada = False
        self.canal = 1
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':
    TV = tv()
    print('Televisão está ligada? {}'.format(TV.ligada))
    TV.power()
    print('Televisão está ligada? {}'.format(TV.ligada))
    print('Canal: {}'.format(TV.canal))
    TV.aumenta_canal()
    TV.aumenta_canal()
    print('Canal: {}'.format(TV.canal))
    TV.diminui_canal()
    print('Canal: {}'.format(TV.canal))
    TV.power()
    TV.aumenta_canal()
    TV.aumenta_canal()
    TV.aumenta_canal()
    print('Canal: {}'.format(TV.canal))
    TV.power()
    TV.aumenta_canal()
    TV.aumenta_canal()
    print('Canal: {}'.format(TV.canal))
    
