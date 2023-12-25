# This is a sample Python script.
# This is a sample Python script.
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from deap import base, creator, tools, algorithms
import random

Diastolic_BP=ctrl.Antecedent(np.arange(40, 140, 1), label="Diastolic Blood Pressure")
Systolic_BP=ctrl.Antecedent(np.arange(70, 200, 1), label="Systolic Blood Pressure")
Temperature=ctrl.Antecedent(np.arange(98, 108, 1), label="Temperature")
Health_care=ctrl.Consequent(np.arange(0,100,1),label="Health Care",defuzzify_method="centroid")


Diastolic_BP['Low']=fuzz.trimf(Diastolic_BP.universe, [40, 55, 70])
Diastolic_BP['Normal']=fuzz.trimf(Diastolic_BP.universe, [60, 72, 85])
Diastolic_BP['Pre Hypertension']=fuzz.trimf(Diastolic_BP.universe, [80, 87, 95])
Diastolic_BP['High BP Stage 1']=fuzz.trimf(Diastolic_BP.universe, [90, 97, 105])
Diastolic_BP['High BP Stage 2']=fuzz.trimf(Diastolic_BP.universe, [100, 115, 125])
Diastolic_BP['Emergency']=fuzz.trimf(Diastolic_BP.universe, [120, 130, 150])

Systolic_BP['Low']=fuzz.trimf(Systolic_BP.universe, [70, 85, 100])
Systolic_BP['Normal']=fuzz.trimf(Systolic_BP.universe, [90, 110, 130])
Systolic_BP['Pre Hypertension']=fuzz.trimf(Systolic_BP.universe, [120, 135, 150])
Systolic_BP['High BP Stage 1']=fuzz.trimf(Systolic_BP.universe, [140, 155, 170])
Systolic_BP['High BP Stage 2']=fuzz.trimf(Systolic_BP.universe, [160, 175, 190])
Systolic_BP['Emergency']=fuzz.trimf(Systolic_BP.universe, [180, 200, 220])

Temperature['Low']=fuzz.trimf(Temperature.universe, [94, 96, 98])
Temperature['Temp']=fuzz.trimf(Temperature.universe, [96, 98, 102])
Temperature['Temp High 1']=fuzz.trimf(Temperature.universe, [98, 104, 106])
Temperature['Temp High 2']=fuzz.trimf(Temperature.universe, [104, 106, 108])
Temperature['Emergency']=fuzz.trimf(Temperature.universe, [106, 108, 110])

Health_care.automf(5,names=['Good','Normal','Worst','Dangerous','High Emergency'])

diastolic_labels = ['Low', 'Normal', 'Pre Hypertension', 'High BP Stage 1', 'High BP Stage 2', 'Emergency']
systolic_labels = ['Low', 'Normal', 'Pre Hypertension', 'High BP Stage 1', 'High BP Stage 2', 'Emergency']
temperature_labels = ['Low', 'Temp', 'Temp High 1', 'Temp High 2', 'Emergency']
health_care_labels = ['Good', 'Normal', 'Worst','Dangerous','High Emergency']


rules = []

rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Low"] & Temperature["Low"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Low"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Low"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Low"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Low"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Normal"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Normal"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Normal"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Normal"] & Temperature["Temp High 2"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Normal"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Pre Hypertension"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 2"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Pre Hypertension"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 1"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 2"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 1"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 2"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["High BP Stage 2"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Emergency"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Emergency"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Emergency"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Emergency"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Low"] & Systolic_BP["Emergency"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Low"] & Temperature["Low"] ,Health_care["Good"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Low"] & Temperature["Temp"] ,Health_care["Good"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Low"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Low"] & Temperature["Temp High 2"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Low"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Normal"] & Temperature["Low"] ,Health_care["Good"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Normal"] & Temperature["Temp"] ,Health_care["Good"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Normal"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Normal"] & Temperature["Temp High 2"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Normal"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Pre Hypertension"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Pre Hypertension"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 1"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 1"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 2"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["High BP Stage 2"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Emergency"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Emergency"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Emergency"] & Temperature["Temp High 1"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Emergency"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Normal"] & Systolic_BP["Emergency"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Low"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Low"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Low"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Low"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Low"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Normal"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Normal"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Normal"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Normal"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Normal"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Pre Hypertension"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Pre Hypertension"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 1"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 1"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 2"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["High BP Stage 2"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
'''rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Emergency"] & Temperature["Low"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Emergency"] & Temperature["Temp"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Emergency"] & Temperature["Temp High 1"] ,Health_care["Dangerous"]))'''
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Pre Hypertension"] & Systolic_BP["Emergency"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Low"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Low"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Low"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Low"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Low"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Normal"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Normal"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Normal"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Normal"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Normal"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Pre Hypertension"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Pre Hypertension"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 1"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 1"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 2"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["High BP Stage 2"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Emergency"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Emergency"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Emergency"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Emergency"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 1"] & Systolic_BP["Emergency"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
'''rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Low"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Low"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Low"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Low"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Low"] & Temperature["Emergency"] ,Health_care["Worst"]))'''
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Normal"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Normal"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Normal"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Normal"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Normal"] & Temperature["Emergency"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Pre Hypertension"] & Temperature["Low"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 1"] ,Health_care["Normal"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Pre Hypertension"] & Temperature["Emergency"] ,Health_care["Worst"]))
'''rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 1"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 1"] ,Health_care["Worst"]))'''
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 1"]  ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 1"] & Temperature["Emergency"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 2"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 1"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["High BP Stage 2"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Emergency"] & Temperature["Low"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Emergency"] & Temperature["Temp"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Emergency"] & Temperature["Temp High 1"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Emergency"] & Temperature["Temp High 2"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["High BP Stage 2"] & Systolic_BP["Emergency"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
'''rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Low"] & Temperature["Low"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Low"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Low"] & Temperature["Temp High 1"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Low"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Low"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Normal"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Normal"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Normal"] & Temperature["Temp High 1"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Normal"] & Temperature["Temp High 2"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Normal"] & Temperature["Emergency"] ,Health_care["Dangerous"]))'''
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Pre Hypertension"] & Temperature["Low"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp"] ,Health_care["Worst"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 1"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Pre Hypertension"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Pre Hypertension"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 1"] ,Health_care["Dangerous"]))
'''rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 1"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 1"] & Temperature["Temp High 2"] ,Health_care["Dangerous"]))'''
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 1"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 2"] & Temperature["Low"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp"] ,Health_care["Dangerous"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 1"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 2"] & Temperature["Temp High 2"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["High BP Stage 2"] & Temperature["Emergency"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Emergency"] ,Health_care["High Emergency"]))
'''rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Emergency"] & Temperature["Temp"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Emergency"] & Temperature["Temp High 1"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Emergency"] & Temperature["Temp High 2"] ,Health_care["High Emergency"]))
rules.append(ctrl.Rule(Diastolic_BP["Emergency"] & Systolic_BP["Emergency"] & Temperature["Emergency"] ,Health_care["High Emergency"]))'''


# Create a control system
health_care_system = ctrl.ControlSystem(rules)
# GA begines from here
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Initialize the DEAP toolbox
toolbox = base.Toolbox()

# Define the genetic operators
toolbox.register("rule_strength", random.uniform, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.rule_strength, n=len(rules))  # Adjust the number of rules
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define the evaluation function
def evaluate(individual):
    # Apply rule strengths to the fuzzy system
    for i, rule_strength in enumerate(individual):
       rules[i].weight = rule_strength

    # Create a new control system
    health_care_system = ctrl.ControlSystem(rules)

    # Input values for the fuzzy system (adjust as needed)
    health_care_simulation = ctrl.ControlSystemSimulation(health_care_system)
    health_care_simulation.input['Diastolic Blood Pressure'] = 140
    health_care_simulation.input['Systolic Blood Pressure'] = 200
    health_care_simulation.input['Temperature'] = 108

    # Perform fuzzy inference
    health_care_simulation.compute()

    # Get the output value
    output_value = health_care_simulation.output['Health Care']

    # Assuming a simple fitness function (adjust as needed)
    fitness = abs(50 - output_value)

    return fitness,

toolbox.register("evaluate", evaluate)

# Define the genetic operators
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Set up the GA parameters
population_size = 10
num_generations = 10
mutation_rate = 0.1

# Create the initial population
population = toolbox.population(n=population_size)

# Run the GA
algorithms.eaMuPlusLambda(population, toolbox, mu=population_size, lambda_=population_size,
                           cxpb=0.7, mutpb=mutation_rate, ngen=num_generations, stats=None, halloffame=None, verbose=True)

# Get the best individual from the final population
best_individual = tools.selBest(population, k=1)[0]

# Print the best individual
print("Best Individual:", best_individual)

best_output = evaluate(best_individual)
print("Best Health Care Output:", best_output)





'''class FuzzyGui:
    def __init__(self, master):
        self.master = master
        master.title("Fuzzy Health Care System")

        original_image =Image.open("C:/Users/DELL/Downloads/medical.jpg")

        # Resize the image to match the window size
        width, height = master.winfo_width(), master.winfo_height()
        resized_image = original_image.resize((width, height),  Image.BICUBIC)

        # Convert the resized image to Tkinter PhotoImage
        self.background_image = ImageTk.PhotoImage(resized_image)

        label = tk.Label(master, image=self.background_image)
        label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        # Create a label to hold the background image
        background_label = ttk.Label(master, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)



        # Create frames
        self.frame = ttk.Frame(master, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Diastolic Blood Pressure combo box
        self.label_diastolic = Label(master, text="Diastolic Blood Pressure:")
        self.label_diastolic.grid(row=0, column=0, padx=50, pady=50)
        self.combo_diastolic = ttk.Combobox(master, values=[str(i) for i in range(50, 151)])
        self.combo_diastolic.grid(row=0, column=1, padx=50, pady=50)

        # Systolic Blood Pressure combo box
        self.label_systolic = Label(master, text="Systolic Blood Pressure:")
        self.label_systolic.grid(row=1, column=0, padx=50, pady=30)
        self.combo_systolic = ttk.Combobox(master, values=[str(i) for i in range(70, 221)])
        self.combo_systolic.grid(row=1, column=1, padx=50, pady=30)

        # Temperature combo box
        self.label_temperature = Label(master, text="Temperature:")
        self.label_temperature.grid(row=2, column=0, padx=50, pady=30)
        self.combo_temperature = ttk.Combobox(master, values=[str(i) for i in range(94, 111)])
        self.combo_temperature.grid(row=2, column=1, padx=50, pady=30)

        # Calculate button
        self.calculate_button = Button(master, text="Calculate Health Care", command=self.calculate_health_care)
        self.calculate_button.grid(row=3, columnspan=2, pady=50)

        # Result label
        self.result_label = Label(master, text="")
        self.result_label.grid(row=4, columnspan=2, pady=50)

    def calculate_health_care(self):
        try:
            diastolic_value = float(self.combo_diastolic.get())
            systolic_value = float(self.combo_systolic.get())
            temperature_value = float(self.combo_temperature.get())

            print(f"Debug: Diastolic={diastolic_value}, Systolic={systolic_value}, Temperature={temperature_value}")

            # Input values
            inputs = {
                'Diastolic Blood Pressure': diastolic_value,
                'Systolic Blood Pressure': systolic_value,
                'Temperature': temperature_value
            }

            # Create a ControlSystemSimulation object
            health_care_sim = ctrl.ControlSystemSimulation(health_care_ctrl, flush_after_run=True)

            # Pass the input values to the simulation
            health_care_sim.input['Diastolic Blood Pressure'] = diastolic_value
            health_care_sim.input['Systolic Blood Pressure'] = systolic_value
            health_care_sim.input['Temperature'] = temperature_value

            # Compute the fuzzy output
            health_care_sim.compute()

            # Get the crisp output
            defuzzified_value = health_care_sim.output['Health Care']

            # Display the result
            self.result_label.config(text=f'Health Care: {defuzzified_value:.2f}')

        except ValueError as e:
            print(f"Debug: Error - {e}")
            self.result_label.config(text='Invalid input. Please enter numeric values.')


# Create the Tkinter window
root = Tk()
root.geometry("500x500")
app = FuzzyGui(root)
root.mainloop()'''







