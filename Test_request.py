# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:05:55 2021

@author: flavi
"""
import requests

url = 'http://127.0.0.1:1200/predict'  # localhost and the defined port + endpoint
body = {
        "SpMax_L":4.170,
        "J_Dz(e)":2.1144,
        "nHM":0,
        "F01[N-N]":0,
        "NssssC":0,
        "nCb-":0,
        "C%":30.8,
        "nCp":1,
        "nO":1,
        "F03[C-N]":0,
        "SdssC":0.000,
        "HyWi_B(m)":2.461,
        "LOC":1.393,
        "F03[C-O]":1,
        "Me":0.989,
        "Mi":1.144,
        "nN-N":0,
        "nArNO2":0,
        "nCRX3":0,
        "SpPosA_B(p)":1.104,
        "nCIR":1,
        "B01[C-Br]":0,
        "B03[C-C1]":0,
        "N-073":0,
        "Psi_i_1d":-0.204,
        "B04[C-Br]":0,
        "SdO":0.000,
        "TI2_L":1.542,
        "nCrt":0,
        "C-026":0,
        "F02[C-N]":0,
        "nHDon":0,
        "SpMax_B(m)":3.315,
        "Psi_i_A":1.967,
        "nN":0,
        "nArCOOR":0,
        "nX":0
}
response = requests.post(url, data=body)
response.json()
