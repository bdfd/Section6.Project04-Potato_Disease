'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-09 10:41:57
LastEditors  : BDFD
Description  : 
FilePath     : \predict\predict.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template, request
import pandas as pd
import numpy as np
import tempproj as temp
import execdata as exe
predict = Blueprint('predict', __name__,
                    static_folder='static', template_folder='templates')

df = pd.read_csv(
    'https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_Preprocessed_Data.csv',
    encoding="utf-8")
seniorcitizen_lists = df['SeniorCitizen'].unique().tolist()
seniorcitizen_lists.sort()
partner_lists = df['Partner'].unique().tolist()
partner_lists.sort()
dependents_lists = df['Dependents'].unique().tolist()
dependents_lists.sort()
onlinesecurity_lists = df['OnlineSecurity'].unique().tolist()
onlinesecurity_lists.sort()
techsupport_lists = df['TechSupport'].unique().tolist()
techsupport_lists.sort()
contract_lists = df['Contract'].unique().tolist()
contract_lists.sort()
paperlessbilling_lists = df['PaperlessBilling'].unique().tolist()
paperlessbilling_lists.sort()
paymentmethod_lists = df['PaymentMethod'].unique().tolist()
paymentmethod_lists.sort()


@predict.route('/', methods=["POST", "GET"])
def predict_index():
    mingzi = ' '
    SeniorCitizen = ' '
    Partner = ' '
    Dependents = ' '
    tenure = ' '
    OnlineSecurity = ' '
    TechSupport = ' '
    Contract = ' '
    PaperlessBilling = ' '
    PaymentMethod = ' '
    MonthlyCharges = ' '
    if request.method == "GET":
        return render_template('homepage/predict_index.html', mingzi=mingzi, SeniorCitizen=SeniorCitizen,
                               Partner=Partner, Dependents=Dependents, tenure=tenure, OnlineSecurity=OnlineSecurity,
                               TechSupport=TechSupport, Contract=Contract, PaperlessBilling=PaperlessBilling,
                               PaymentMethod=PaymentMethod, MonthlyCharges=MonthlyCharges,
                               seniorcitizen_lists=seniorcitizen_lists,
                               partner_lists=partner_lists, dependents_lists=dependents_lists,
                               onlinesecurity_lists=onlinesecurity_lists, techsupport_lists=techsupport_lists,
                               contract_lists=contract_lists, paperlessbilling_lists=paperlessbilling_lists,
                               paymentmethod_lists=paymentmethod_lists)
    else:
        mingzi = request.form['mingzi']
        para_list = []
        SeniorCitizen = request.form['SeniorCitizen']
        para_list.append(SeniorCitizen)
        Partner = request.form['Partner']
        para_list.append(Partner)
        Dependents = request.form['Dependents']
        para_list.append(Dependents)
        tenure = exe.convint(request.form['tenure'])
        para_list.append(tenure)
        OnlineSecurity = request.form['OnlineSecurity']
        para_list.append(OnlineSecurity)
        TechSupport = request.form['TechSupport']
        para_list.append(TechSupport)
        Contract = request.form['Contract']
        para_list.append(Contract)
        PaperlessBilling = request.form['PaperlessBilling']
        para_list.append(PaperlessBilling)
        PaymentMethod = request.form['PaymentMethod']
        para_list.append(PaymentMethod)
        MonthlyCharges = request.form['MonthlyCharges']
        para_list.append(MonthlyCharges)
        result = temp.supervised_classification.Tele_Customer_Churn_0602(
            para_list)
        if result:
            result = 'Will Be Churned.'
        else:
            result = 'Will Be Stay With Us.'
        return render_template('homepage/predict_index.html', result=result, mingzi=mingzi, SeniorCitizen=SeniorCitizen,
                               Partner=Partner, Dependents=Dependents, tenure=tenure, OnlineSecurity=OnlineSecurity,
                               TechSupport=TechSupport, Contract=Contract, PaperlessBilling=PaperlessBilling,
                               PaymentMethod=PaymentMethod, MonthlyCharges=MonthlyCharges,
                               seniorcitizen_lists=seniorcitizen_lists,
                               partner_lists=partner_lists, dependents_lists=dependents_lists,
                               onlinesecurity_lists=onlinesecurity_lists, techsupport_lists=techsupport_lists,
                               contract_lists=contract_lists, paperlessbilling_lists=paperlessbilling_lists,
                               paymentmethod_lists=paymentmethod_lists)
