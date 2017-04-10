class Car_report:
    '''
    defines methods to read makes and models
    and assign them as properties
    then generate a report summarizing those as key/value pairs

    '''
    #a report will have lists of makes and models
    def __init__(self):
        self.car_makes = list()
        self.car_models = list()

    #reads car-makes 
    def read_car_make(self):
        """Summary
             reads make file and appends each as make property on a report instance
        Returns:
            TYPE: list
        """
        #alias car-models file as 'car_models'
        with open('car-makes.py', 'r') as car_makes:
            for make in car_makes:
                #append, but strip new line character
                self.car_makes.append(make.replace('\n', ''))
            return self.car_makes

    #read models
    def read_car_model(self):
        """Summary
           reads make file and appends each as make property on a report instance 
        Returns:
            TYPE: list
        """
        #alias car-models file as 'car_models'
        with open('car-models.py', 'r') as car_models:
            for model in car_models:
                #append, but strip new line character
                self.car_models.append(model.replace('\n', ''))
            return self.car_models

    #call the readers above, iterate through them, set as key values in a dict
    def generate_dictionary(self):
        """Summary
            iterates through two lists (props on report instance)
            and sets items as key value pairs
        Returns:
            TYPE: dict
        """
        #get lists
        car_makes = self.read_car_make()
        car_models = self.read_car_model()
        car_dictionary = {}
        model_list = []
        for make in car_makes:
            #each time through the makes, clear the model_list
            model_list = []
            for model in car_models:
                #if they start with the same letter
                if make[0] == model[0]:
                    #append to the list everything after the 2nd character
                    model_list.append(model[2:])
            #now set the model_list as value of current make key
            car_dictionary[make] = model_list
        print('current inventory: {}'.format(car_dictionary))

if __name__ == '__main__':
    report = Car_report()
    report.generate_dictionary()