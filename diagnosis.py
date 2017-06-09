import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas.tools.plotting import table

def person_id(dataframes):
    for df in dataframes:

        df.replace(['300.0', 300.0, '311.0', 311.0, '305.0', 305.0], ['300.00', '300.00', '311', '311', '305.00', '305.00'], inplace=True)
        df['patient_id']= df.apply(lambda df: str(df['Birth Dt']) + df['Gender Desc'] + str(df['Diag 1']), axis=1)
        # df = df.groupby('patient_id')
        df['Diag 4'] = df['Diag 4'].astype(str)
    return df

def dropping_duplicates(dataframes):
    for df in dataframes:
        df = df.drop_duplicates(subset='patient_id', keep='last')
    return df

def given_diagnosis(df, diag1_code, df_desc):
    plt.close('all')
    df = df.loc[df['Diag 1'] == diag1_code]
    # df = df[df['Doctor_Num'] == doc_num]
    count_list= []
    df_2 = df['Diag 2'].astype(str)
    df_3 = df['Diag 3'].astype(str)
    df_4 = df['Diag 4'].astype(str)
    unique = df_2.unique()
    index = np.argwhere(unique =='nan')
    unique = np.delete(unique, index)
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
    #I want to exclude any counts where it was only 1 person
    together = together[together['count'] != 1/len(df)*100]


    #Grab DataFrame rows where column has certain values
    title_desc1= df_desc[df_desc['Diag 1'] == diag1_code]
    title_desc = str(list(title_desc1['Diag Desc 1']))
    title_desc = title_desc.strip("['")
    title_desc = title_desc.strip("']")

    df_desc = df_desc[df_desc['Diag 1'].isin(together['code'])]

    plt.close('all')
    #creating bar graph
    fig = together.plot(x = 'code', y = 'count', kind = 'bar', color = 'b', figsize = (8,8))
    plt.ylabel('Percent of Patients')
    plt.title('Co-morbidity for {}'.format(diag1_code))
    plt.savefig('graphs_tables/Co-morbid_{0}_male_21_40.png'.format(diag1_code))

    plt.close('all')
    #
    # fig, ax = plt.subplots()
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)

    # table = plt.table(cellText=df_desc.values,
    #       cellLoc = 'center', rowLoc = 'center',
    #       loc='center')
    # table.set_fontsize(30)
    # table.scale(2.5,2)
    # plt.subplots_adjust(right=0.35)

    # ax = plt.subplot(111, frame_on=False) # no visible frame
    # ax.xaxis.set_visible(False)  # hide the x axis
    # ax.yaxis.set_visible(False)  # hide the y axis
    #
    # ax.table(cellText=df_desc.values, cellLoc = 'center', rowLoc = 'center',
    #       loc='center')
    #      # where df is your data frame
    # # plt.title('Co-morbidity for {}'.format(title_desc))
    # plt.figtext(.5,.9,'Co-morbidity for {}'.format(title_desc), fontsize=5, ha='center')
    #
    # plt.savefig('graphs_tables/Co-morbid_{}_table.png'.format(diag1_code),dpi=900)
    # return count_list

def given_diagnosis_by_doctor(df, diag1_code, df_desc):
    plt.close('all')
    df = df.loc[df['Diag 1'] == diag1_code]
    doc_list = [1,2,3,4,5,6,7,8,9,10,11]

    for x in doc_list:
        df = df[df['Doctor_Num'] == x]
        if df.dropna().empty == True:
            continue
        else:
            count_list= []
            df_2 = df['Diag 2'].astype(str)
            df_3 = df['Diag 3'].astype(str)
            df_4 = df['Diag 4'].astype(str)
            unique = df_2.unique()
            index = np.argwhere(unique =='nan')
            unique = np.delete(unique, index)
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
            #I want to exclude any counts where it was only 1 person
            together = together[together['count'] != 1/len(df)*100]


            #Grab DataFrame rows where column has certain values
            title_desc1= df_desc[df_desc['Diag 1'] == diag1_code]
            title_desc = str(list(title_desc1['Diag Desc 1']))
            title_desc = title_desc.strip("['")
            title_desc = title_desc.strip("']")

            df_desc = df_desc[df_desc['Diag 1'].isin(together['code'])]

            plt.close('all')
            #creating bar graph
            fig = together.plot(x = 'code', y = 'count', kind = 'bar', color = 'r', figsize = (8,8))
            plt.ylabel('Percent of Patients')
            plt.title('Co-morbidity for {}'.format(diag1_code))
            plt.savefig('graphs_tables/Co-morbid_{0}_doctor_{1}.png'.format(diag1_code, x))

def table_of_codes(df):
    df_desc = df[['Diag 1','Diag Desc 1']]
    df_desc = df_desc.drop_duplicates(subset='Diag 1', keep='last')
    return df_desc


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
    dropping_col = ['Loc Name', 'City', 'Zip', 'Pat Age', 'Referring']
    #drop columns not used/needed
    df_combo = df_combo.drop((x for x in dropping_col), axis = 1)
    #drop rows that have no diagnosis information
    df_combo = df_combo[df_combo['Diag 1'].notnull()]

    # gives amount of patients having each diagnosis
    # print(df_combo['Diag 1'].unique())
    # print(df_combo.info())

    # table_of_codes(df_combo)
    df_desc = df_combo[['Diag 1','Diag Desc 1']]
    df_desc = df_desc.drop_duplicates(subset='Diag 1', keep='last')

    #make a graph and table for each diagnosis
    lst_codes = df_combo['Diag 1'].astype(str)
    #there is a nan in position 1
    lst_codes = list(lst_codes.unique())
    #removed symptoms from list of diagnosis
    removing1 = ('300.20','305.60', '300.29', '304.81','309.29' , '305.23' , '309.89' , '305.20' , '305.01', '308.3', '303.03', '303.90', '298.9', '300.00', '305.50', '304.22', '305.22', '303.91', '303.40', '312.9', '298.8', '304.01', '304.00')
    removing = ('293.1', '305.00', '304.80', 'V62.82', '304.02', '293.0', 'V70.1', '303.93', '305.02', '304.03', '303.92')
    lst_code_diag1 = [e for e in lst_codes if e not in removing1]
    lst_code_diag = [e for e in lst_code_diag1 if e not in removing]

    #Age groups
    df_age_0_20 = df_combo[df_combo["Pat Age in Years"] < 20]
    df_age_21_40 = df_combo[df_combo['Pat Age in Years'].between(21, 40, inclusive=True)]
    df_age_41_60 = df_combo[df_combo['Pat Age in Years'].between(41, 60, inclusive=True)]
    df_age_61_80 = df_combo[df_combo['Pat Age in Years'].between(61, 80, inclusive=True)]
    df_age_81_110 = df_combo[df_combo['Pat Age in Years'].between(81, 110, inclusive=True)]

    #gender groups
    df_female = df_combo[df_combo["Gender Desc"] == 'Female']
    df_male = df_combo[df_combo["Gender Desc"] == 'Male']

    #Age/Gender combo
    df_female_0_20 = df_age_0_20[df_age_0_20["Gender Desc"] == 'Female']
    df_female_21_40 = df_age_21_40[df_age_21_40["Gender Desc"] == 'Female']
    df_female_41_60 = df_age_41_60[df_age_41_60["Gender Desc"] == 'Female']
    df_female_61_80 = df_age_61_80[df_age_61_80["Gender Desc"] == 'Female']
    df_female_81_110 = df_age_81_110[df_age_81_110["Gender Desc"] == 'Female']

    df_male_0_20 = df_age_0_20[df_age_0_20["Gender Desc"] == 'Male']
    df_male_21_40 = df_age_21_40[df_age_21_40["Gender Desc"] == 'Male']
    df_male_41_60 = df_age_41_60[df_age_41_60["Gender Desc"] == 'Male']
    df_male_61_80 = df_age_61_80[df_age_61_80["Gender Desc"] == 'Male']
    df_male_81_110 = df_age_81_110[df_age_81_110["Gender Desc"] == 'Male']

    # count_list = []
    # max_count= []
    # for x in lst_code_diag[3:5]:
    #     given_diagnosis(df_age_0_20,x, df_desc)
        # max_count.append(max(count_list))
    # lst_df = [df_female_0_20,
    # df_female_21_40, df_female_41_60, df_female_61_80, df_male_0_20, df_male_21_40, df_male_41_60, df_male_61_80]
    # for x in lst_df:

    # given_diagnosis(df_female_41_60,'296.23', df_desc)
    given_diagnosis(df_male_21_40, '295.70', df_desc)

#index of list cod not working 1, 16, 17, 21
#goal of project
#data
    #cleaning
    #feature engineering
#EDA
#Methodology
#visualization
