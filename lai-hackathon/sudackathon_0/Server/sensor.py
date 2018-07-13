# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:26:04 2018

"""
import grovepi
from abc import ABCMeta, abstractmethod

 # センサを管理するクラス
class Sensors() :
    pass

class Sensor(metaclass = ABCMeta) :
    def __init__(self, port):
        self.port = port
    
    @abstractmethod
    def getValue(self) :
        pass

class UltraSonicSensor(Sensor) :
    def getValue(self) :
        return grovepi.ultrasonicRead(self.port)