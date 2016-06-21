class Car(object):
    """class for modelling car activities
    """

    def __init__(self, name='General', model='GM', cartype=None):
        self.name = name
        self.model = model

        self.num_of_doors = 4

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        self.cartype = cartype

        if self.cartype != 'trailer':
            self.cartype = 'saloon'

        self.num_of_wheels = 4

        if self.cartype == 'trailer':
            self.num_of_wheels = 8

        self.speed = 0

    def is_saloon(self):
        """true if cartype is not trailer
        """
        return self.cartype == 'saloon'

    def drive(self, drive):
        """change speed depending on cartype * drive
        """
        if self.cartype == 'trailer':
            self.speed = drive * 77 / 7
        else:
            self.speed = drive * 1000 / 3

        return self
