import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
# model = pickle.load(open(r'C:\Users\kashy\Desktop\Django\MithilaHeritage\MithilaHeritage\blog\spam.pkl','rb'))
# cv=pickle.load(open(r'C:\Users\kashy\Desktop\Django\MithilaHeritage\MithilaHeritage\blog\vectorizer.pkl','rb'))

# model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open(r"blog\vectorizer.pkl","rb"))
model=pickle.load(open(r"blog\spam.pkl","rb"))
def detectSpam(msg):
	print(msg)
	data=[msg]
	print(data)
	vec=cv.transform(data).toarray()
	result=model.predict(vec)
	if result[0]==0:
		return False
	else:
		return True
#detectSpam("Congratulations ur awarded 500 of CD vouchers or 125gift guaranteed & Free entry 2 100 wkly draw txt MUSIC to 87066 TnCs www.Ldew.com1win150ppmx3age16			")
