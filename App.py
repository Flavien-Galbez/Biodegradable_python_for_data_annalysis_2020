# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:02:56 2021

@author: flavi
"""
from flask import Flask
from flask_restful import Api, Resource, reqparse
from sklearn.externals import joblib
import numpy as np

APP = Flask(__name__)
API = Api(APP)

#On recharge les modeles
LOG_REG = joblib.load('modeles/logReg.joblib')
KNN = joblib.load('modeles/KNN.joblib')
RAND_FOREST = joblib.load('modeles/Rand_Forest.joblib')
SVM = joblib.load('modeles/SVM.joblib')
NN_RELU = joblib.load('modeles/NeuralNetworksRelu.joblib')
NN_LOG = joblib.load('modeles/NeuralNetworksLog.joblib')

class Predict(Resource):

    @staticmethod
    def post():
        #On cree un disctionnaire avec tout les parametres utilises dans les modeles
        parser = reqparse.RequestParser()
        parser.add_argument('SpMax_L')
        parser.add_argument('J_Dz(e)')
        parser.add_argument('nHM')
        parser.add_argument('F01[N-N]')
        parser.add_argument('NssssC')
        parser.add_argument('nCb-')
        parser.add_argument('C%')
        parser.add_argument('nCp')
        parser.add_argument('nO')
        parser.add_argument('F03[C-N]')
        parser.add_argument('SdssC')
        parser.add_argument('HyWi_B(m)')
        parser.add_argument('LOC')
        parser.add_argument('F03[C-O]')
        parser.add_argument('Me')
        parser.add_argument('Mi')
        parser.add_argument('nN-N')
        parser.add_argument('nArNO2')
        parser.add_argument('nCRX3')
        parser.add_argument('SpPosA_B(p)')
        parser.add_argument('nCIR')
        parser.add_argument('B01[C-Br]')
        parser.add_argument('B03[C-C1]')
        parser.add_argument('N-073')
        parser.add_argument('Psi_i_1d')
        parser.add_argument('B04[C-Br]')
        parser.add_argument('SdO')
        parser.add_argument('TI2_L')
        parser.add_argument('nCrt')
        parser.add_argument('C-026')
        parser.add_argument('F02[C-N]')
        parser.add_argument('nHDon')
        parser.add_argument('SpMax_B(m)')
        parser.add_argument('Psi_i_A')
        parser.add_argument('nN')
        parser.add_argument('nArCOOR')
        parser.add_argument('nX')
        args = parser.parse_args()

        X_new = np.fromiter(args.values(), dtype=float)  # converti nos input en nombre

        #Sortie avec les resultats des differents modeles
        out = {'Pred_Log_Reg': LOG_REG.predict([X_new])[0],
               'Pred_kNN': KNN.predict([X_new])[0],
               'Pred_Rand_Forest': RAND_FOREST.predict([X_new])[0],
               'Pred_SVM': SVM.predict([X_new])[0],
               'Pred_Neural_Networks_Relu': NN_RELU.predict([X_new])[0],
               'Pred_Neural_Networks_Log': NN_LOG.predict([X_new])[0]}

        return out, 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1200')