import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

def person_id(dataframes):
    for df in dataframes:
        df.replace(['300.0', 300.0, '311.0', 311.0], ['300.00', '300.00', '311', '311'], inplace=True)
        df['patient_id']= df.apply(lambda df: str(df['Birth Dt']) + df['Gender Desc'] + str(df['Diag 1']), axis=1)
        # df = df.groupby('patient_id')
        df['Diag 4'] = df['Diag 4'].astype(str)
    return df

def dropping_duplicates(dataframes):
    for df in dataframes:
        df = df.drop_duplicates(subset='patient_id', keep='last')
        # for x in df['Diag 1']:
        #     if x = '300.0':

    return df

def given_diagnosis(df, diag1_code):
    plt.close('all')
    df = df.loc[df['Diag 1'] == diag1_code]
    count_list= []
    df_2 = df['Diag 2'].astype(str)
    df_3 = df['Diag 3'].astype(str)
    df_4 = df['Diag 4'].astype(str)
    unique = df_2.unique()[1:-1]
    for X in unique:
        count = 0
        for x in df_2:
            if X == x:
                count +=1
        for x in df_3:
            if X == x:
                count +=1
        for x in df_4:
            if X == x:
                count +=1
        count_list.append(count/len(df)*100)

    together = pd.DataFrame(
    {'code': unique,
     'count': count_list
    })
    together = together.sort_values(['count'], ascending=[False])

    # cnt_related_diag = df['Diag 2'].value_counts().fillna(0)+ df['Diag 3'].value_counts().fillna(0)
    # cnt_related_diag = pd.value_counts(df['Diag 2'].values, sort=False)

    together.plot(x = 'code', y = 'count', kind = 'bar', color = 'r')
    plt.ylabel('Percent of Patients')
    plt.title('Co-morbidity Percents')

    plt.savefig('Co-morbid314_01.png')
    print(len(df))
    print (unique)
    print(count_list)
    print(together)

if __name__== '__main__':
    df_jan = pd.read_csv('../data/Chloe Jan clean.csv')
    df_feb = pd.read_csv('../data/Chloe Feb clean.csv')
    df_mar = pd.read_csv('../data/Chloe March clean.csv')
    df_apr = pd.read_csv('../data/Chloe April clean.csv')
    df_may = pd.read_csv('../data/Chloe May clean.csv')
    df_jun = pd.read_csv('../data/Chloe June clean.csv')

    #to create unique id
    dataframes = (df_jan, df_feb, df_mar, df_apr, df_may, df_jun)
    person_id(dataframes)

    #to get rid of duplicate columns
    # dropping_duplicates(dataframes)
    frames = [df_jan, df_feb, df_mar,df_apr, df_may, df_jun]

    df_combo = pd.concat(frames)
    df_combo = df_combo.drop_duplicates(subset='patient_id', keep='last')

    # gives amount of patients having each diagnosis
    print(df_combo['Diag 1'].value_counts())
    print(df_combo.info())

    given_diagnosis(df_combo,'314.01')
