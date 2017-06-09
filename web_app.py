from flask import Flask, render_template, request, jsonify
from sklearn.externals import joblib
import numpy as np
# from build_model import TextClassifier
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
#
# @app.route('/getdelay',methods=['POST','GET'])
# def get_delay():
# 	if request.method=='POST':
# 		result=request.form
#
# 		#Prepare the feature vector for prediction
#
# 		# new_vector = pd.read_csv('../data/example_clean.csv')
# 		new_vectors= [int(result['approx_payout_date']),int(result['body_length']),int(result['fb_published']),int(result['has_analytics']),int(result['listed']),int(result['num_order']),int(result['num_payouts']),int(result['show_map']),int(result['user_age']),int(result['user_type']),int(result['num_pre_payouts']),int(result['num_ticket_types'])]
# 		new_vector = np.array(new_vectors)
#
# 		model = joblib.load('../data/data_model.pkl')
# 		prediction = model.predict(new_vector)
#
# 		return render_template('result.html',prediction=prediction)

if __name__ == '__main__':
    app.run()
