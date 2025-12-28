import asyncio
from typing import TypeVar
from mage_config.mage_class import Mage


def main():
    classes_list: list[str] = ['mage']
    user_class: str = ""
    class_accepted: bool = user_class in classes_list
    character_name:str = ""
    character_creation: bool = False
    while not character_creation:
        while not class_accepted:
            user_class: str = input(f"Please select a class. Possible classes:   {', '.join([c for c in classes_list])} ->")
            class_accepted: bool = user_class.lower().strip() in classes_list
            if not class_accepted:
                print("Class not available!")
        
        while not character_name:
            character_name: str = input(f"Please input character name: ")
            
        
        finish_char_creation = input('Character creation finished y/n ?')
        if finish_char_creation.lower().strip() == 'n':
            class_accepted = False
            character_name = ""
        else:
            break
        
if __name__ == "__main__":
    main()