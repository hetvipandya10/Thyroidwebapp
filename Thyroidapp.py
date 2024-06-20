import streamlit as st

st.title("Welcome to Thyroid App")

Age=st.slider("Select Age=",15,82)
Gender=st.slider("Select Gender=",0,1)
Smoking=st.slider("Select Smoking=",0,1)
HxSmoking=st.slider("Select HxSmoking=",0,1)
HxRadiothreapy=st.slider("Select HxRadiothreapy=",0,1)
ThyroidFunction=st.slider("Select ThyroidFunction=",0,4)
PhysicalExamination=st.slider("Select PhysicalExamination=",0,4)
Adenopathy=st.slider("Select Adenopathy=",0,5)
Pathology=st.slider("Select Pathology=",0,3)
Focality=st.slider("Select Focality=",0,1)
Risk=st.slider("Select Risk=",0,2)
T=st.slider("Select T=",0,6)
N=st.slider("Select N=",0,2)
M=st.slider("Select M=",0,1)
Stage=st.slider("Select Stage=",0,4)
Response=st.slider("Select Response=",0,4)

import pickle
model=pickle.load(open("Thyroid.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[Age,Gender,Smoking,HxSmoking,HxRadiothreapy,ThyroidFunction,PhysicalExamination,Adenopathy,Pathology,Focality,Risk,T,N,M,Stage,Response]])
    st.success("The Thyroid is "+ prd[0])

