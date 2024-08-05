import streamlit as st
import pandas as pd
from pickle import load
import datetime
import numpy as np

def create_page():
	st.title('STOCK PRICE PREDICTION')
	yr_val = st.date_input('enter date in day-month-year format')
	st.write(yr_val)
	timestamp = datetime.datetime.combine(yr_val,datetime.datetime.min.time()).timestamp()

	data = {
		'year' :[timestamp]
		}

	df = pd.DataFrame(data,index=[0])
	return df

features = create_page()
st.write(features)
X_lstm = np.array([features['year'].values] * 10).reshape(1, 10, 1)



loaded_model = load(open('lstm_model.pkl','rb'))
res = loaded_model.predict(features)
st.write('CLOSING PRICE',res)


