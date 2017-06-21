from flask import Flask, render_template, request, jsonify
from sklearn.externals import joblib
import numpy as np
# from build_model import TextClassifier
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html', doctor = "/static/images/Co-morbid_age_scatter_doctors.png")
#
@app.route('/doctorresult',methods=['POST','GET'])
def doctorresult():
	if request.method=='POST':
		result=request.form

		if result['Diagnosis_Code'] == '296.90':
			doc1 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Unspecified episodic mood disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '296.80':
			doc1 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Bipolar disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '314.01':
			doc1 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Attention deficit disorder of childhood with hyperactivity_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '296.53':
			doc1 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Bipolar I disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '311':
			doc1 = "/static/comparing/Co-morbid_Depressive disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Depressive disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Depressive disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Depressive disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Depressive disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Depressive disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Depressive disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Depressive disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Depressive disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Depressive disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Depressive disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '300.02':
			doc1 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Generalized anxiety disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '296.33':
			doc1 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Major depressive affective disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '300.3':
			doc1 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Obsessive-compulsive disorders_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '296.89':
			doc1 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Other and unspecified bipolar disorders_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '300.01':
			doc1 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Panic disorder without agoraphobia_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '295.30':
			doc1 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Paranoid type schizophrenia_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		elif result['Diagnosis_Code'] == '309.81':
			doc1 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Posttraumatic stress disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)

		else:
			doc1 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_1.png"
			doc2 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_2.png"
			doc3 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_3.png"
			doc4 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_4.png"
			doc5 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_5.png"
			doc6 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_6.png"
			doc7 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_7.png"
			doc8 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_8.png"
			doc9 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_9.png"
			doc10 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_10.png"
			doc11 = "/static/comparing/Co-morbid_Schizoaffective disorder_doctor_11.png"
			return render_template('result.html', doc1 = doc1, doc2 = doc2, doc3 = doc3, doc4 = doc4, doc5 = doc5, doc6 = doc6, doc7 = doc7, doc8 = doc8, doc9 = doc9, doc10 = doc10, doc11 = doc11)


@app.route('/getdelay',methods=['POST','GET'])
def get_delay():
	if request.method=='POST':
		result=request.form

		#Prepare the feature vector for prediction

		# new_vector = pd.read_csv('../data/example_clean.csv')
		# new_vectors= [int(result['approx_payout_date']),int(result['body_length']),int(result['fb_published']),int(result['has_analytics']),int(result['listed']),int(result['num_order']),int(result['num_payouts']),int(result['show_map']),int(result['user_age']),int(result['user_type']),int(result['num_pre_payouts']),int(result['num_ticket_types'])]
		# new_vector = np.array(new_vectors)
		#
		# model = joblib.load('../data/data_model.pkl')
		# prediction = model.predict(new_vector)

		#above is past code
		if result['Gender Desc'] == 'Female':
			if int(result['Age in Years']) <= 20:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_female_0_20.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_female_0_20.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_female_0_20.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_female_0_20.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = None
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = None
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_female_0_20.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = None
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = None
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = None
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_female_0_20.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = None
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = None
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
			elif 21 <= int(result['Age in Years']) <= 40:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_female_21_40.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_female_21_40.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_female_21_40.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_female_21_40.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_female_21_40.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_female_21_40.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_female_21_40.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_female_21_40.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_female_21_40.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_female_21_40.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_female_21_40.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_female_21_40.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_female_21_40.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 41 <= int(result['Age in Years']) <= 60:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_female_41_60.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_female_41_60.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_female_41_60.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_female_41_60.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_female_41_60.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_female_41_60.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_female_41_60.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_female_41_60.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_female_41_60.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_female_41_60.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_female_41_60.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_female_41_60.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_female_41_60.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 61 <= int(result['Age in Years']) <= 80:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_female_61_80.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_female_61_80.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_female_61_80.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_female_61_80.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_female_61_80.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_female_61_80.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_female_61_80.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_female_61_80.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_female_61_80.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_female_61_80.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_female_61_80.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_female_61_80.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_female_61_80.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 81 <= int(result['Age in Years']) <= 110:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_female_81_110.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_female_81_110.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_female_81_110.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_female_81_110.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_female_81_110.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_female_81_110.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_female_81_110.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_female_81_110.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_female_81_110.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_female_81_110.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_female_81_110.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_female_81_110.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_female_81_110.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)


		if result['Gender Desc'] == 'Male':
			if int(result['Age in Years']) <= 20:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_Male_0_20.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_Male_0_20.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_Male_0_20.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_Male_0_20.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = None
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = None
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_Male_0_20.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = None
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = None
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = None
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_Male_0_20.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = None
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_Male_0_20.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 21 <= int(result['Age in Years']) <= 40:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_Male_21_40.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_Male_21_40.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_Male_21_40.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_Male_21_40.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_Male_21_40.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_Male_21_40.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 41 <= int(result['Age in Years']) <= 60:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_Male_41_60.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_Male_41_60.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_Male_41_60.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_Male_41_60.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_Male_41_60.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_Male_41_60.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 61 <= int(result['Age in Years']) <= 80:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_Male_61_80.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_Male_61_80.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_Male_61_80.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_Male_61_80.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_Male_61_80.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_Male_61_80.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)
			elif 81 <= int(result['Age in Years']) <= 110:
				if result['Diagnosis_Code'] == '296.90':
					prediction = "/static/Co-morbid_Unspecified episodic mood disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Unspecified episodic mood disorder.png"
					word_cloud = "/static/wordcloud_Unspecified episodic mood disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '314.01':
					prediction = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity_Male_81_110.png"
					normal = "/static/Co-morbid_Attention deficit disorder of childhood with hyperactivity.png"
					word_cloud ="/static/wordcloud_Attention deficit disorder of childhood with hyperactivity.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.80':
					prediction = "/static/Co-morbid_Bipolar disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Bipolar disorder.png"
					word_cloud ="/static/wordcloud_Bipolar disorder.png"
					return render_template('results.html', data = prediction , pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.53':
					prediction = "/static/Co-morbid_Bipolar I disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Bipolar I disorder.png"
					word_cloud ="/static/wordcloud_Bipolar I disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '311':
					prediction = "/static/Co-morbid_Depressive disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Depressive disorder.png"
					word_cloud = "/static/wordcloud_Depressive disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.02':
					prediction = "/static/Co-morbid_Generalized anxiety disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Generalized anxiety disorder.png"
					word_cloud = "/static/wordcloud_Generalized anxiety disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.33':
					prediction = "/static/Co-morbid_Major depressive affective disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Major depressive affective disorder.png"
					word_cloud = "/static/wordcloud_Major depressive affective disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.3':
					prediction = "/static/Co-morbid_Obsessive-compulsive disorders_Male_81_110.png"
					normal = "/static/Co-morbid_Obsessive-compulsive disorders.png"
					word_cloud = "/static/wordcloud_Obsessive-compulsive disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '296.89':
					prediction = "/static/Co-morbid_Other and unspecified bipolar disorders_Male_81_110.png"
					normal = "/static/Co-morbid_Other and unspecified bipolar disorders.png"
					word_cloud = "/static/wordcloud_Other and unspecified bipolar disorders.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '300.01':
					prediction = "/static/Co-morbid_Panic disorder without agoraphobia_Male_81_110.png"
					normal = "/static/Co-morbid_Panic disorder without agoraphobia.png"
					word_cloud = "/static/wordcloud_Panic disorder without agoraphobia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.30':
					prediction = "/static/Co-morbid_Paranoid type schizophrenia_Male_81_110.png"
					normal = "/static/Co-morbid_Paranoid type schizophrenia.png"
					word_cloud = "/static/wordcloud_Paranoid type schizophrenia.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '309.81':
					prediction = "/static/Co-morbid_Posttraumatic stress disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Posttraumatic stress disorder.png"
					word_cloud = "/static/wordcloud_Posttraumatic stress disorder.png"
					return render_template('results.html', data = prediction, pred = normal, cloud = word_cloud)
				elif result['Diagnosis_Code'] == '295.73':
					prediction = "/static/Co-morbid_Schizoaffective disorder_Male_81_110.png"
					normal = "/static/Co-morbid_Schizoaffective disorder.png"
					word_cloud = "/static/wordcloud_Schizoaffective disorder.png"
					return render_template('results.html', data = prediction,  pred = normal, cloud = word_cloud)
				else:
					prediction = None
					return render_template('results.html', data = prediction)


		# return render_template('results.html', data = prediction)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 8105, threaded=True)
