# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:36:52 2022

@author: amaad
"""

import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go

#Importing Libreries

import pandas as pd

from statsmodels.tsa.holtwinters import ExponentialSmoothing

import warnings


df=pd.read_csv('Gold_data.csv')

hwmModel=ExponentialSmoothing(df['price'],seasonal='mul',trend='add',seasonal_periods=24).fit()



def main():
    st.title("Gold Price Predictor")
    st.info("Let us predict the Price of GOLD for the Future")
  
    s = datetime.date(2021,12,23)
    e = st.date_input("Enter the ending Date to Predict the Gold Prices")
    diff=( (e-s).days+1)
   
    
   
    if st.button("PREDICT"):
        index_future_dates=pd.date_range(start= s ,end= e)
        pred=hwmModel.forecast(diff).rename('Price')
        pred.index=index_future_dates
        df = pd.DataFrame(pred)
        
        st.dataframe(df)
        
        st.line_chart(df)
        
        
                                    
st.sidebar.subheader("About the App")
st.sidebar.info("GOLD PRICE PREDICTION")

	
st.sidebar.subheader("By Group 1")
st.sidebar.text("ARNICA SAIKIA")  
st.sidebar.text("KAUSALENDRA SINGH")             
st.sidebar.text("AKASH KUNDU")
st.sidebar.text("AMAN KUMAR")            
st.sidebar.text("DHANLASHMI S")
st.sidebar.text("SHUBHAM")
st.sidebar.text("AMAAD A GAGROO")      


st.sidebar.subheader("Mentor:")
st.sidebar.info("KARTIK MUSKULA")
       
        
        
        
        
      

if __name__ == '__main__':
    main()   
        
        
    
