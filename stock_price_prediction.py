import streamlit as st
import pandas as pd
from pickle import load

def create_page():
	st.title('STOCK PRICE PREDICTION')
	#yr_val = st.date_input('enter date in day-month-year format')
	st.write(yr_val)
	

	data = {
		'year' :yr_val
		}

	df = pd.DataFrame(data,index=[0])
	return df

features = create_page()
st.write(features)

loaded_model = load(open('lstm_model.pkl','rb'))
res = loaded_model.predict(features)
st.write('CLOSING PRICE',res)


