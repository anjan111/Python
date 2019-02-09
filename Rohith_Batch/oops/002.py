class company():
    def __init__(self,capi,client,market):
        self.capi=capi
        self.client=client
        self.market=market
    def info(self):
        print self
        print self.capi
        print self.client
        print self.market
        
inst      =   company("5 LAC","Student","Digital")
software  =   company("20 lac","product","digital")

inst.info()
software.info()
