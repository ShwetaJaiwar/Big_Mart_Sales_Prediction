import streamlit as st

st.title("Start Predicting for your Organization")


Item_weight=st.text_input(" Enter Item Weight")
#Item_visibility=st.text_input(" Enter Item Visibility")
#Fat_content=st.radio(" Select Fat Content",["Low Fat","Regular Fat","High Fat"])
Item_type=st.selectbox(" Select Item Type ",["Baking Goods","Breads","Breakfast","Canned","Dairy","Fruits and Vegetables","Hard Drinks","Health and Hygiene","Household","Meat","Others","Seafood","Snack Foods","Soft Drinks","Starchy Foods"])
Item_mrp=st.text_input(" Enter Item MRP")
Outlet_size=st.selectbox("Outlet Size",["Small","Medium","Large"])
Outlet_Type=st.radio(" Select Outlet Type",["Grocery Store","Supermarket Type 1","Supermarket Type 2"])
#Outlet_Location=st.selectbox("Outlet Location Type",["Tier 1","Tier 2","Tier 3"])


Establish_date=st.date_input("Established Date")
#time=st.time_input("Time")

#accept=st.checkbox("Accept the terms",value=False)


if st.button("Predict"):
    st.write("Predicting")

if st.button("Reset"):
    st.write("Resetting")    
