import streamlit as st
import pickle
import numpy as np

# import model
pipe = pickle.load(open('pipe.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))


st.title("Laptop Pridictor")

# Laptop Brand
Company = st.selectbox('Brand',data['Company'].unique())

# Laptop Type
Type = st.selectbox('Type',data['TypeName'].unique())

# Laptop Ram
Ram = st.selectbox('Ram(in GB)',[2,4,8,12,16,24,32,64])

# Laptop Weight
Weight = st.number_input('Weight of the Laptop')

# TouchScreen
Touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# Ips Display
Ips_Display = st.selectbox('Ips_Panel',['No','Yes'])

# Laptop Screen Size
Screen_Size = st.number_input("Screen Size")

# Screen Resolution
Screen_Resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# Cpu Brand
cpu = st.selectbox('Brand',data['Cpu_Brand'].unique())

# Hardrive
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD(in GB)',[0,128,256,512,1024])

# GPU
gpu = st.selectbox('GPU',data['Gpu_Brand'].unique())

# Operating System
os = st.selectbox('OS',data['os'].unique())


if st.button('Pridict Price'):
    
    #query
    PricePerInches = None
    if Touchscreen== 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0
    
    if Ips_Display =='Yes':
        Ips_Display=1
    else:
        Ips_Display=0
    
    # calculate PricePerInches
    X_res = int(Screen_Resolution.split('x')[0])
    Y_res = int(Screen_Resolution.split('x')[1])
    
    PricePerInches = ((X_res**2)+(Y_res**2))*0.5/Screen_Size
    
    query = np.array([Company,Type,Ram,Weight,Touchscreen,Ips_Display,PricePerInches,cpu,hdd,ssd,gpu,os])
    query = query.reshape(1,12)
    pipe.predict(query)
    st.title("The Predicted Price of this Configuration is: " + str(int(np.exp(pipe.predict(query)[0]))))