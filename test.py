class car(object):
    def __init__(self,model,company,color,speed_limit):
        self.color = color 
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
        
    def start(self):
        print('started')

    def end(self):
        print('ended')

audi = car('2013','audi','black','50')
farari = car('2021','Farari','Red','50')
print(farari.model)
print(audi.color)