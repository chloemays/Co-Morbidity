import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas.tools.plotting import table
import wordcloud

def person_id(dataframes):
    for df in dataframes:
        df['Diag 4'] = df['Diag 4'].astype(str)
        df.replace(['300.0', 300.0, '311.0', 311.0, '305.0', 305.0], ['300.00', '300.00', '311', '311', '305.00', '305.00'], inplace=True)

        #replacing bipolar 1 codes
        df.replace(to_replace = ['296.40', '296.4', '296.41', '296.42', '296.43', '296.44', '296.45', '296.46', '296.50', '296.5', '296.51', '296.52', '296.54', '296.55', '296.56', '296.7', '296.02', '296.05', '296.60', '296.66', '296.00', '296.61', '296.64', '296.62', '296.63', '296.65'], value = '296.53', inplace = True)

        # replacing Major Depressive disorder
        df.replace(to_replace = ['296.20', '296.2', '296.21', '296.22', '296.23', '296.24', '296.25', '296.26', '296.30', '296.3', '296.31', '296.32', '296.34', '296.35', '296.36'], value = '296.33', inplace = True)

        #replacing Paranoid type schizophrenia
        df.replace(to_replace = ['295.33','295.35', '295.34', '295.32'], value = '295.30', inplace = True)

        #replacing schizoaffective disorder
        df.replace(to_replace = ['295.75','295.74', '295.72', '295.70'], value = '295.73', inplace = True)

        #replace Alcohol disorder to include all levels in one
        df.replace(['303.90', '303.9'], value = '305.00', inplace = True)

        #replace cannabus use disorder
        df.replace(['304.30', '304.3', '305.2'], value = '305.20', inplace = True)

        #replace Phencyclidine use disorder
        df.replace(['304.60', '304.6', '305.9'], value = '305.90', inplace = True)

        #replace Nondependent alcohol abuse
        df.replace(['305.02'], value = '305.01', inplace = True)

        #replace other hallucinogen use disorder
        df.replace(['304.50', '304.5', '305.3'], value = '305.30', inplace = True)

        #replace Opiod use disorder
        df.replace(['304.00', '304', '304.0', '305.5'], value = '305.50', inplace = True)

        #replace Sedative Hypnotic or Anxiolytic use disorder
        df.replace(['304.10', '304.1', '305.4'], value = '305.40', inplace = True)

        #replace stimulant use disorder Amphetamine-type substance/other
        df.replace(['304.4', '304.40', '305.7'], value = '305.70', inplace = True)

        #replace stimulant use disprder cocaine
        df.replace(['304.2', '304.20', '305.6'], value = '305.60', inplace = True)

        df['patient_id']= df.apply(lambda df: str(df['Birth Dt']) + df['Gender Desc'] + str(df['Diag 1']), axis=1)
        # df = df.groupby('patient_id')

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

    #matching descriptions with code
    df_desc.rename(columns={'Diag 1': 'code'}, inplace=True)
    together = pd.merge(together, df_desc, on= 'code', how='inner')

    #creating bar graph
    # my_colors = [(x/10.0, x/20.0, 0.75) for x in range(len(together))]
    my_colors = [(x/10.0, x/20.0, .75) for x in range(len(together))]
    fig = together.plot(x = 'Diag Desc 1', y = 'count', kind = 'barh', color = my_colors, figsize = (15,8))

    plt.yticks(wrap = True)
    plt.xlabel('Percent of Male age 81 to 110 Patients', fontsize = 13)
    plt.title('Co-morbidity for {}'.format(title_desc), fontsize = 13)
    plt.subplots_adjust(left=0.3)
    plt.savefig('static/Co-morbid_{0}_female_41_60_high_res.png'.format(title_desc), dpi = 600)

    plt.close('all')

    #creating word cloud

    # words = together['Diag Desc 1'].to_string(header=False,index=False)
    # replace_lst = ['other', 'and','without', 'nondependent', 'abuse','disorders', 'disorder', 'unspecified', 'classified', 'state', 'generalized', 'elsewhere', 'type']
    #
    # words = words.split()
    #
    # resultwords  = [word for word in words if word.lower() not in replace_lst]
    # result = ' '.join(resultwords)


    # print(words)
    # # print(result)
    # cloud = wordcloud.WordCloud()
    # #https://stackoverflow.com/q/38247648/2901002
    # cloud.generate(result)
    # plt.imshow(cloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.savefig('static/wordcloud_{}.png'.format(title_desc))

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
    print(together.info())


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

def graph_hist(df):
    plt.close('all')
    fig = df['Pat Age in Years'].hist(bins = 5)
    fig = df['Pat Age in Years'].hist(bins = 10)
    fig = df['Pat Age in Years'].hist(bins = 15)
    fig = df['Pat Age in Years'].hist(bins = 20)
    plt.title('Male Age Range in Data with 5,10,15,20 groups')
    plt.savefig('images/Co-morbid_age_hist_male')

    # plt.close('all')
    # df.plot.scatter(x= 'Doctor_Num', y='Pat Age in Years', figsize = (15, 10))
    # X = np.array(df['Doctor_Num'])
    # y = np.array(df['Pat Age in Years'])
    # plt.violinplot( X, y, widths=0.7, showmeans=True,
    #                   showextrema=True, showmedians=True, bw_method=0.5)
    # plt.title('Age Range in Data')
    # plt.savefig('images/Co-morbid_age_scatter')

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
    df_desc['Diag Desc 1'] = df_desc['Diag Desc 1'].apply(lambda x: x.split(',')[0])

    #make a graph and table for each diagnosis
    lst_codes = df_combo['Diag 1'].astype(str)
    #there is a nan in position 1
    lst_codes = list(lst_codes.unique())
    #removed symptoms from list of diagnosis
    removing1 = ('300.20','305.60', '300.9', '304.81','309.29' , '305.23' , '309.89' , '305.20' , '305.01', '308.3', '303.03', '303.90', '298.9', '300.00', '305.50', '304.22', '305.22', '303.91', '303.40', '312.9', '298.8', '304.01', '304.00')
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
    given_diagnosis(df_female_41_60, '296.90', df_desc)
    # graph_hist(df_male)

#index of list cod not working 1, 16, 17, 21
#goal of project
#data
    #cleaning
    #feature engineering
#EDA
#Methodology
#visualization
