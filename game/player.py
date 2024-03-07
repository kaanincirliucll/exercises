class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return f"Player {self.name} with token {self.token}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value is None or len(value) < 1:
            raise ValueError("Value is not valid")
        self.__name = value

    @property
    def token(self):
        return self.__token
    
    @name.setter
    def token(self, value):
        self.__token = value