from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,oder):
        """初始化父类属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=oder

    def show_oder(self):
        for flavor in self.flavors:
            print(flavor)

ice=IceCreamStand("happy-restaurant","IceCreamStand",["apple-ice","orange-ice"])
ice.show_oder()