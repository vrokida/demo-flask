class Customer:

    identifier_types = ['celula', 'passport', 'ruc']

    def __init__(self, name, last_name, identifier_type='ruc'):

        if self.is_property_is_not_empty(name) and self.is_property_is_not_empty(last_name):
            self.__name = name
            self.__last_name = last_name
        else:
            raise Exception('The name or last name is empty')
        if not self.is_identifier_type_valid(identifier_type):
            raise Exception('The identifier type is not valid')
        else:
            self.__identifier_type = identifier_type

    def is_property_is_not_empty(self, property):
        if property and len(property) > 0:
            return True
        return False

    def is_identifier_type_valid(self, identifier_type):
        if identifier_type not in Customer.identifier_types:
            return False
        return True

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_identifier_type(self):
        return self.__identifier_type