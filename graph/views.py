import glob
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
import glob
import os
import pandas as pd
import excel2json
from pandas import read_csv
import plotly
import os
#import earthpy as et
import datetime
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
from pyxll import xl_func
import seaborn as sns
#import pandas_datareader as pdr
#from fbprophet.plot import plot_plotly
import plotly.offline as py
import plotly.graph_objs as go
from matplotlib.pylab import rcParams
#from pandas.stats.moments import ewma
import pandas as pd
import os
import glob
import math
import matplotlib.pyplot as plt
from datetime import datetime, date
import json
import time
import statistics
from time import strftime
from time import gmtime
import json


def index(request):
    return render(request, "graph/index.html")

def index2(request):
    return render(request, "graph/index2.html")

def index3(request):
    return render(request, "graph/index3.html")

def index4(request):
    return render(request, "graph/index4.html")


def accueil(request):
    return render(request, "graph/accueil.html")


def indextest(request):
    return render(request, "graph/indextest.html")

def indextest2(request):
    return render(request, "graph/indextest2.html")

def index5(request):
    return render(request, "graph/index5.html")


def test(request):
    return render(request, "graph/test.html")

# etude sur une na
def etude_na(request):
    options = ['ISUTI056-ISU_HIST_CONSO_ANN', 'ISUTI086-ISU_MDR_ECHE1_DETEC', 'ISUTI66K-ISU_IDENT_IBAN_ANONYM',
               'ISUTI502-FICA_TRAN_PIEC_FIGL',
               'ISUTI042B-ISU_OPTI_TURPE', 'ISUTI086-ISU_MDR_ECHE1_DETEC', 'ISUTI495-ISU_CALCUL_FACTURAT_ES',
               'ISUTI66L-ISU_ANONYM_IBAN',
               'NDEBJCHG', 'NDATE001-ISU_MAJ_ZDATE_NA', 'ISUTI50Q-ISU_PRE_ANLYSE_NA', 'ISUTI02W-ISU_GO_NA_HORS_HEBDO',
               'ISUTI400-ISU_NO_GO_NACOMP',
               'ISUTI440-ISU_SPLIT4_D21', 'ISUTI4A9-ISU_INT_IND_G', 'ISUTI411-ISU_CALCUL_FACTURAT',
               'ISUTI412-ISU_FACTURATION_ISU', 'ISUTI071-ISU_INT_MODIF_CONT',
               'ISUTI025-ISU_ITF_GINKO14', 'ISUTI62T-ISU_ITF_G14_GAZ', 'ISUTI420-ISU_ITF_GINKO13',
               'ISUTI421-ISU_ITF_GINKO10', 'ISUTI40K-ISU_MDR_SOUSC_G',
               'ISUTI054-FICA_RAPPROCHM_AUTO', 'ISUTI00Y-ISU_MDR_AF_PROC_PART', 'ISUTI069-FICA_CYCLE_RELANCE_PROP',
               'ISUTI057-FICA_CYCLE_RELANCE_ACT',
               'ISUTI01Z-ISU_PROG_AL_DFKKKOBW', 'ISUTI01E-FICA_MARQ_CREAN_DOU', 'ISUTI01F-FICA_TRAN_CREAN_DOU',
               'ISUTI065-FICA_ENCAISS_DECAISS1',
               'ISUTI42V-EDIT_ISU_SP_B_NRJ_XML', 'ISUTI42W-EDIT_CONCAT_FACT_XML', 'EDITE673', 'EDITESGL',
               'ISUTI018-ISU_PROG_MAJ_BP']

    # use glob to get all the csv files
    # in the folder
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "*.xlsx"))
    myHouse = np.array([])
    tiime_array = []
    c = len(csv_files)
    print(c)
    # loop over the list of csv files
    for f in csv_files:
        print(f)
        # read the csv file
        df = pd.read_excel(f)
        # print the location and filename
        print('Location:', f)
        print('File Name:', f.split("\\")[-1])
        #calcule du temps d'execution d'un job
        df['Run Time'] = df['End time'].sub(df['Start time'], axis=0)
        # selecting rows based on condition
        df_final = df[df['Name'].isin(options)]
        # print('\nResult dataframe :\n',df_final)
        # df_final.head()
        data = [go.Scatter(x=df_final['Name'], y=df_final['Run Time'])]
        x = df_final['Name']
        y = df_final['Run Time']
        # moyenne_start_time est calculé dans la fonction 'etude_par_job'
        y2 = moyenne_start_time
        plt.plot(x, y)  # plot first line
        plt.plot(y2)
        fig.show()
        #affichage du graph (job avec statut)
        data2 = [go.Scatter(x=df_final['Name'], y=df_final['Status'])]
        fig = go.Figure(data2)
        fig.show()
        # affichage du graph (job avec date de debut)
        data3 = [go.Scatter(x=df_final['Start time'], y=df_final['Name'])]
        fig = go.Figure(data3)
        fig.show()
        # affichage du graph (job avec date de fin)
        data4 = [go.Scatter(x=df_final['End time'], y=df_final['Name'])]
        fig = go.Figure(data4)
        fig.show()
        #calcule de temps d'execution de la NA
        for i in range(1):
            firstly = [df_final.iloc[:1, 1:2]]
            lastt = df_final.iloc[-1:, 2:3]
            tiime = lastt - firstly
            my_array_dur = np.array(tiime)
            str1 = ''.join(str(e) for e in my_array_dur[0])
            date = str1.split()[5]
            tiime_array.append(date)
            i + 1
    #import du json
    print(tiime_array)
    json_str = json.dumps(tiime_array)
    print(json_str)
    with open('durée_na.json', 'w') as json_file:
        json.dump(json_str, json_file
    return render(request, "graph/test.html")





#etude des NAs sur 1 mois
def etude_na_mois(request):
# use glob to get all the csv files
# in the folder
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "*.xlsx"))
    c = len(csv_files)
    my_array = []
    arr_date = []
    for f in csv_files:
        dff = pd.read_excel(f)
        dff['Run Time'] = dff['End time'].sub(dff['Start time'], axis=0)
        df_finall = dff[dff['Name'].isin(options)]
        total = df_finall['Run Time'].sum()
        fin = total.total_seconds()
        print('la durée de la NA est :',fin,'s')
        #print(fin)
        arr_date.append(fin)
    #tableau qui contient les durées des nuits applicatifs (NAs)
    print(arr_date)
    return render(request, "graph/test.html")




# extraction de la date a partir du nom du fichier
def date_na(request):
    folder_path = r'C:\Users\a866098\OneDrive - Atos\Bureau\atos2'
    file_type = r'\*xlsx'
    array_date = np.array([])
    for i in walk(r'C:\Users\a866098\OneDrive - Atos\Bureau\atos2'):
        fileList = glob.glob("*.xlsx")
        for f in fileList:
            date_na = f[4:6] + '/' + f[6:8] + '/' + f[0:4]
            array_date = np.append(date_na, array_date)
    final_array_date = []
    for element in array_date:
        if element not in final_array_date:
            final_array_date.append(element)
    #tab qui contient les dates des NA
    print(final_array_date)
    json_str = json.dumps(final_array_date)
    print(json_str)
    with open('date_na.json', 'w') as json_file:
        json.dump(json_str, json_file)
    return render(request, "graph/test.html")


#la date de la na avec sa durée
def date_duree_na(request):
    print(final_array_date)
    print(arr_date)
    t = pd.DataFrame({
                       'Durée de la NA': arr_date,
                       })

    t.insert(0, "Date de la NA", final_array_date)
    t.head()

    dataframe = [go.Scatter(x=t['Date de la NA'],y=t['Durée de la NA'])]
    plt = go.Figure(dataframe)
    plt.show()
    json_str = json.dumps(arr_date)
    print(json_str)
    with open('durée_na.json', 'w') as json_file:
        json.dump(json_str, json_file)
    return render(request, "graph/test.html")



#etude pas Job
def etude_par_job(request):
    options = np.array(['ISUTI056-ISU_HIST_CONSO_ANN', 'ISUTI086-ISU_MDR_ECHE1_DETEC', 'ISUTI66K-ISU_IDENT_IBAN_ANONYM',
                        'ISUTI502-FICA_TRAN_PIEC_FIGL',
                        'ISUTI042B-ISU_OPTI_TURPE', 'ISUTI086-ISU_MDR_ECHE1_DETEC', 'ISUTI495-ISU_CALCUL_FACTURAT_ES',
                        'ISUTI66L-ISU_ANONYM_IBAN',
                        'NDEBJCHG', 'NDATE001-ISU_MAJ_ZDATE_NA', 'ISUTI50Q-ISU_PRE_ANLYSE_NA',
                        'ISUTI02W-ISU_GO_NA_HORS_HEBDO', 'ISUTI400-ISU_NO_GO_NACOMP',
                        'ISUTI440-ISU_SPLIT4_D21', 'ISUTI4A9-ISU_INT_IND_G', 'ISUTI411-ISU_CALCUL_FACTURAT',
                        'ISUTI412-ISU_FACTURATION_ISU', 'ISUTI071-ISU_INT_MODIF_CONT',
                        'ISUTI025-ISU_ITF_GINKO14', 'ISUTI62T-ISU_ITF_G14_GAZ', 'ISUTI420-ISU_ITF_GINKO13',
                        'ISUTI421-ISU_ITF_GINKO10', 'ISUTI40K-ISU_MDR_SOUSC_G',
                        'ISUTI054-FICA_RAPPROCHM_AUTO', 'ISUTI00Y-ISU_MDR_AF_PROC_PART', 'ISUTI069-FICA_CYCLE_RELANCE_PROP',
                        'ISUTI057-FICA_CYCLE_RELANCE_ACT',
                        'ISUTI01Z-ISU_PROG_AL_DFKKKOBW', 'ISUTI01E-FICA_MARQ_CREAN_DOU', 'ISUTI01F-FICA_TRAN_CREAN_DOU',
                        'ISUTI065-FICA_ENCAISS_DECAISS1',
                        'ISUTI42V-EDIT_ISU_SP_B_NRJ_XML', 'ISUTI42W-EDIT_CONCAT_FACT_XML', 'EDITE673', 'EDITESGL',
                        'ISUTI018-ISU_PROG_MAJ_BP'])

    # use glob to get all the csv files
    # in the folder
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "*.xlsx"))
    myHouse2 = np.array([])
    c = len(csv_files)
    # print(c)
    # print(df_final)
    # loop over the list of csv files
    runtime_array = []
    starttime_array = []
    endtime_array = []
    runtime_array_final_array = []
    starttime_final_array = []
    endtime_final_array = []
    my_arra = []
    datetimee_array = []
    datetimee_array1 = []
    datetimee_array2 = []

    df = pd.DataFrame()
    for f in csv_files:
        # print(c)
        datee = (f[31:39])
        # print(datee)
        res = df_final.isin(['ISUTI056-ISU_HIST_CONSO_ANN']).any().any()
        res2 = df_final.isin(['ISUTI086-ISU_MDR_ECHE1_DETEC']).any().any()
        res3 = df_final.isin(['ISUTI66K-ISU_IDENT_IBAN_ANONYM']).any().any()
        res4 = df_final.isin(['ISUTI502-FICA_TRAN_PIEC_FIGL']).any().any()
        res5 = df_final.isin(['ISUTI042B-ISU_OPTI_TURPE']).any().any()
        res6 = df_final.isin(['ISUTI086-ISU_MDR_ECHE1_DETEC']).any().any()
        res7 = df_final.isin(['ISUTI495-ISU_CALCUL_FACTURAT_ES']).any().any()
        res8 = df_final.isin(['ISUTI66L-ISU_ANONYM_IBAN']).any().any()
        res9 = df_final.isin(['NDEBJCHG']).any().any()
        res10 = df_final.isin(['NDATE001-ISU_MAJ_ZDATE_NA']).any().any()
        res11 = df_final.isin(['ISUTI50Q-ISU_PRE_ANLYSE_NA']).any().any()
        res12 = df_final.isin(['ISUTI02W-ISU_GO_NA_HORS_HEBDO']).any().any()
        res13 = df_final.isin(['ISUTI400-ISU_NO_GO_NACOMP']).any().any()
        res14 = df_final.isin(['ISUTI440-ISU_SPLIT4_D21']).any().any()
        res15 = df_final.isin(['ISUTI4A9-ISU_INT_IND_G']).any().any()
        res16 = df_final.isin(['ISUTI411-ISU_CALCUL_FACTURAT']).any().any()
        res17 = df_final.isin(['ISUTI412-ISU_FACTURATION_ISU']).any().any()
        res18 = df_final.isin(['ISUTI071-ISU_INT_MODIF_CONT']).any().any()
        res19 = df_final.isin(['ISUTI025-ISU_ITF_GINKO14']).any().any()
        res20 = df_final.isin(['ISUTI62T-ISU_ITF_G14_GAZ']).any().any()
        res21 = df_final.isin(['ISUTI420-ISU_ITF_GINKO13']).any().any()
        res22 = df_final.isin(['ISUTI421-ISU_ITF_GINKO10']).any().any()
        res23 = df_final.isin(['ISUTI40K-ISU_MDR_SOUSC_G']).any().any()
        res24 = df_final.isin(['ISUTI054-FICA_RAPPROCHM_AUTO']).any().any()
        res25 = df_final.isin(['ISUTI00Y-ISU_MDR_AF_PROC_PART']).any().any()
        res26 = df_final.isin(['ISUTI069-FICA_CYCLE_RELANCE_PROP']).any().any()
        res27 = df_final.isin(['ISUTI057-FICA_CYCLE_RELANCE_ACT']).any().any()
        res28 = df_final.isin(['ISUTI01Z-ISU_PROG_AL_DFKKKOBW']).any().any()
        res29 = df_final.isin(['ISUTI01E-FICA_MARQ_CREAN_DOU']).any().any()
        res30 = df_final.isin(['ISUTI01F-FICA_TRAN_CREAN_DOU']).any().any()
        res31 = df_final.isin(['ISUTI065-FICA_ENCAISS_DECAISS1']).any().any()
        res32 = df_final.isin(['ISUTI42V-EDIT_ISU_SP_B_NRJ_XML']).any().any()
        res33 = df_final.isin(['ISUTI42W-EDIT_CONCAT_FACT_XML']).any().any()
        res34 = df_final.isin(['EDITE673']).any().any()
        res35 = df_final.isin(['EDITESGL']).any().any()
        res36 = df_final.isin(['ISUTI018-ISU_PROG_MAJ_BP']).any().any()

        if res:
            m = df_final[df_final['Name'] == 'ISUTI056-ISU_HIST_CONSO_ANN'].index.values
            p = m[0]
            # print(p)
            # run_time = df_final.iloc[p:p+1 , 4:5]
            # print(run_time)
            # print(type(run_time))
            for i in range(1):
                run_time = df_final.iloc[p:p + 1, 4:5]
                runtime_array.append(run_time)
                str1 = ''.join(str(e) for e in runtime_array)
                date = str1.split()
                run_date_final = date[5]
                runtime_array_final_array.append(run_date_final)
                i + 1
            # print(runtime_array_final_array)
            # start_time = df_final.iloc[p:p+1 , 1:2]
            # print(start_time)
            for i in range(1):
                start_time = df_final.iloc[p:p + 1, 1:2]
                starttime_array.append(start_time)
                str1 = ''.join(str(e) for e in starttime_array)
                date = str1.split()
                starttime_final = date[4]
                starttime_final_array.append(starttime_final)
                i + 1
            # print(starttime_final_array)
            # end_time = df_final.iloc[p:p+1 , 2:3]
            # print(end_time)
            for i in range(1):
                end_time = df_final.iloc[p:p + 1, 2:3]
                endtime_array.append(end_time)
                str1 = ''.join(str(e) for e in endtime_array)
                date = str1.split()
                endtime_final = date[4]
                endtime_final_array.append(endtime_final)
                i + 1
            # print(endtime_array)

    # creating the dataframe
    df.insert(0, "Date de la NA", final_array_date)
    df.insert(0, "Run Time", runtime_array_final_array)
    df.insert(0, "Start Time", starttime_final_array)
    df.insert(0, "End Time", endtime_final_array)
    # print(df)
    print('le Job : ISUTI056-ISU_HIST_CONSO_ANN')
    df.head()

    # Calcule de la moyenne du temps d'execution du Job

    for p in range(c):
        datetimee = datetime.strptime(runtime_array_final_array[p], '%H:%M:%S')
        # print(datetimee)
        DN = (datetimee - datetime(1900, 1, 1)).total_seconds()
        datetimee_array.append(DN)
    moyenne_run_time = statistics.mean(datetimee_array)
    moyenne_run_time_final = strftime("%H:%M:%S", gmtime(moyenne_run_time))
    print(df)
    print('la moyenne du temps d\'execution de notre Job est : ', moyenne_run_time_final)

    # Calcule de la moyenne de l'heure de debut du Job

    for p in range(c):
        datetimee1 = datetime.strptime(starttime_final_array[p], '%H:%M:%S')
        # print(datetimee1)
        DN = (datetimee1 - datetime(1900, 1, 1)).total_seconds()
        datetimee_array1.append(DN)
    moyenne_start_time = statistics.mean(datetimee_array1)
    moyenne_start_time_final = strftime("%H:%M:%S", gmtime(moyenne_start_time))

    # print(df)
    print('la moyenne de l\'heure de debut de notre Job est : ', moyenne_start_time_final)

    # Calcule de la moyenne de l'heure de fin du Job

    for p in range(c):
        datetimee2 = datetime.strptime(endtime_final_array[p], '%H:%M:%S')
        # print(datetimee2)
        DN = (datetimee2 - datetime(1900, 1, 1)).total_seconds()
        datetimee_array2.append(DN)
    moyenne_end_time = statistics.mean(datetimee_array2)
    moyenne_end_time_final = strftime("%H:%M:%S", gmtime(moyenne_end_time))
    # print(df)
    print('la moyenne de l\'heure de fin de notre Job est : ', moyenne_end_time_final)

    # affichage graphique du temps d'execution du job selon la date de la NA

    data = [go.Scatter(x=df['Date de la NA'], y=df['Run Time'])]
    fig = go.Figure(data)
    fig.show()
    fig, ax = plt.subplots()
    ax.hlines(y=moyenne_run_time_final, xmin=final_array_date[0], xmax=final_array_date[2], linewidth=2, color='r')

    json_str = json.dumps(final_array_date)
    print(json_str)
    with open('personal.json', 'w') as json_file:
        json.dump(json_str, json_file)
    return render(request, "graph/test.html")

# calcule de la durée de la derniere NA
def etude_fichier_du_jour(request):
    csv_file = glob.glob(os.path.join(path, "*.xlsx"))
    latest_csv = max(glob.glob('C:/Users/a866098/OneDrive - Atos/Bureau/atos2/*.xlsx'), key=os.path.getctime)
    date_na_jour = latest_csv[46:50] + '/' + latest_csv[50:52] + '/' + latest_csv[52:54]
    print(date_na_jour)
    dff = pd.read_excel(latest_csv)
    dff['Run Time'] = dff['End time'].sub(dff['Start time'], axis=0)
    print(dff)
    total = dff['Run Time'].sum()
    fin = total.total_seconds()
    print('la durée de la NA est :',fin,'s')
    dict = dff.to_dict()
    with open('myfileday.txt', 'w') as f:
        print(dict, file=f)
    return render(request, "graph/test.html")