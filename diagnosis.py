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
    plt.savefig('Co-morbid_{}.png'.format(diag1_code))

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

    ax = plt.subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis

    ax.table(cellText=df_desc.values, cellLoc = 'center', rowLoc = 'center',
          loc='center')
         # where df is your data frame
    # plt.title('Co-morbidity for {}'.format(title_desc))
    plt.figtext(.5,.9,'Co-morbidity for {}'.format(title_desc), fontsize=5, ha='center')

    plt.savefig('Co-morbid_{}_table.png'.format(diag1_code),dpi=900)
    print(len(df))
    print (unique)
    print(count_list)
    print(together)

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

    # gives amount of patients having each diagnosis
    # print(df_combo['Diag 1'].unique())
    # print(df_combo.info())

    # table_of_codes(df_combo)
    df_desc = df_combo[['Diag 1','Diag Desc 1']]
    df_desc = df_desc.drop_duplicates(subset='Diag 1', keep='last')

    #make a graph and table for each diagnosis
    lst_codes = df_combo['Diag 1'].astype(str)
    #there is a nan in position 1
    lst_codes = lst_codes.unique()[2:]

    for x in lst_codes:
        given_diagnosis(df_combo,x, df_desc)
