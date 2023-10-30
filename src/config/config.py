import os
from typing import Any
import json

# class made for storing system env data
class OsConfigProvider():
    # function for retrieving system env data
    @staticmethod
    def get_env(item_name: str) -> Any :
        value = os.getenv(item_name)
        return value


    @staticmethod
    def get_user():
       return os.getlogin()
    
class JSONConfigProvder():
    @staticmethod
    def json_loader(json_path):
        with open(json_path) as json_file:
            return json.load(json_file)
        
    @staticmethod
    def get_json_data(item_name: str) -> Any:
        val = JSONConfigProvder.json_loader("C:\\Users\\ASUS\\OneDrive\\Pulpit\\qatrain2\\qatrain2\\src\config\\sample_json.json")
        return val.get(item_name)
        

class Config:

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers
        self.conf_dict = {}

    

     


    def __getattr__(self, item_name : str) -> Any:
        if item_name not in self.conf_dict:
            raise AttributeError(f"Register '{item_name}' var before usage")
        
        return self.conf_dict[item_name]
    
    def register(self,item_name: str) -> None :
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None :
                self.conf_dict[item_name] = value
                return
        raise ValueError (f"{item_name} name is missing in config providers")  #if no value for parameter item_name name found - stop TEST FRAMEWOEK execution
            


config = Config([OsConfigProvider, JSONConfigProvder])
print(config.conf_dict)

            


