#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
        self._condition="Used"
    
    @property
    def shoe_size(self):
        return self._size 
    
    @shoe_size.setter
    def shoe_size(self,value):
        if not isinstance(value,int):
            print("size must be an integer")
        else:
            self.shoe_size=value
    
    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition="New"

