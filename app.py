# imort required packages
from flask import Flask,render_template,request
import requests
import joblib
import numpy as np
import sklearn 
from sklearn.preprocessing import StandardScaler

# Create a flask object
app = Flask("car_model")

# load ML model using joblib
model = joblib.load('finalized_car_model_new.pkl')

# define the route (basically url)to which we need to send http request
# HTTP GET request method
@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')

# creating object for standard scaler
sc = StandardScaler()

# define the route for post method
# HTTP POST methods
@app.route('/predict',methods = ['POST'])
# define the predict function which is to going to predict the result from ml model based on the given values through html form
def predict():
    # fuel type petrol used in html form and therefore we are initiating Fuel_type_diesel = 0
    #Use request.form to get the data from html form through post method.
    #these all are nothing but features of our dataset(ml model)
    Year = int(request.form['Year'])
    Year = 2021 - Year
    Present_Price=float(request.form['Present_Price'])
    Kms_Driven=int(request.form['Kms_Driven'])
    Kms_Driven2=np.log(Kms_Driven)
    Owner=int(request.form['Owner'])
    Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
    #Fuel_Type(feature) is categorised into petrol, diesel, cng, therefore we have done one-hot encoding on it while building model 
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
    #Seller_type(feature) is categorised into indivividual and dealer,therefore we have done one-hot encoding on it while building model
    Seller_Type_Individual=request.form['Seller_Type_Individual']
    if Seller_Type_Individual == 'Individual':
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0
    #Transmission mannual(feature) is categorised into mannual and automatic,therefore we have done one-hot encoding on it while building model
    Transmission_Mannual=request.form['Transmission_Mannual']
    if Transmission_Mannual == 'Mannual':
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0
        
    prediction = model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Transmission_Mannual,Seller_Type_Individual]])
    output=round(prediction[0],2)
    #condition for invalid values
    if output<0:
        return render_template('base.html',prediction_text='Sorry You Can Sell This Car')
    else:
        return render_template('base.html',prediction_text ='You Can Sell This Car At {} lakhs'.format(output))

if __name__ == '__main__':
    #run method starts our web service
    # #Debug : as soon as I save anything in my structure, server should start again
    app.run(debug = True)
