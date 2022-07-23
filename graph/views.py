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
from pandas import read_excel
from django.http import JsonResponse
import json
import csv
from datetime import datetime
import os



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

def find_excel_files_end_start(file):
    df = read_excel(file).values.tolist()
    data =[]
    for line in df:
            print("line here",line[1],line[2])
            data.append({line[0]:{"start"  : str(line[1]) , "end" : str(line[2])}})

    return data




def find_excel_files_durée_all_files(file):
    df = read_excel(file).values.tolist()
    data =[]
    for line in df:
            print("line here",line[1],line[2])
            data.append({line[0]:str(line[2]- line[1])[7:]})

    return data




def find_excel_files(file):
    file_name = file
    df = read_excel(file_name)
    data = df.sort_values(by="Start time")
    data_end = df.sort_values(by="End time")
    rows_number = len(df)
    dure = data_end.iloc[rows_number-1]["End time"]-data.iloc[0]["Start time"]
    dur2 = str(dure)[7:]
    return dur2


jobs_list = ["ISUTI00Y-ISU_MDR_AF_PROC_PART",
    "ISUTI018-ISU_PROG_MAJ_BP",
    "ISUTI01E-FICA_MARQ_CREAN_DOU",
    "ISUTI01F-FICA_TRAN_CREAN_DOU",
    "ISUTI01Z-ISU_PROG_AL_DFKKKOBW",
    "ISUTI025-ISU_ITF_GINKO14",
    "ISUTI02W-ISU_GO_NA_HORS_HEBDO",
    "ISUTI054-FICA_RAPPROCHM_AUTO",
    "ISUTI056-ISU_HIST_CONSO_ANN",
    "ISUTI057-FICA_CYCLE_RELANCE_ACT",
    "ISUTI065-FICA_ENCAISS_DECAISS1",
    "ISUTI069-FICA_CYCLE_RELANCE_PROP",
    "ISUTI071-ISU_INT_MODIF_CONT",
    "ISUTI086-ISU_MDR_ECHE1_DETEC" ,
    "ISUTI400-ISU_NO_GO_NACOMP",
    "ISUTI40K-ISU_MDR_SOUSC_G",
    "ISUTI411-ISU_CALCUL_FACTURAT",
    "ISUTI412-ISU_FACTURATION_ISU",
    "ISUTI420-ISU_ITF_GINKO13",
    "ISUTI421-ISU_ITF_GINKO10",
    "ISUTI42V-EDIT_ISU_SP_B_NRJ_XML",
    "ISUTI42W-EDIT_CONCAT_FACT_XML",
    "ISUTI440-ISU_SPLIT4_D21",
    "ISUTI495-ISU_CALCUL_FACTURAT_ES" ,
    "ISUTI4A9-ISU_INT_IND_G",
    "ISUTI502-FICA_TRAN_PIEC_FIGL",
    "ISUTI50Q-ISU_PRE_ANLYSE_NA",
    "ISUTI62T-ISU_ITF_G14_GAZ",
    "ISUTI66K-ISU_IDENT_IBAN_ANONYM",
    "ISUTI66L-ISU_ANONYM_IBAN"
    ]

def search_name_job(df,name):
    for df_name in df:
        if name == df_name[0] :
            print("name df ",name,df_name[0])
            return df_name[2]-df_name[1]



def seach_file(files,x):
    data = []
    counter = 4
    for i in range(len(files)):
        extension = os.path.splitext(files[i])[1]
        if extension == ".xlsx" and counter != 0:
            df = read_excel(files[i]).values.tolist()
            s =search_name_job(df, x)
            data.append(str(s)[10:12])
            #data.append(str(s)[6:15])
        counter=-1
    return data


def get_last_4csv2(request):
    files_path = os.path.join(os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2'), '*')
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    data = []
    for x in jobs_list:
         data.append({str(x) :seach_file(files,x)})
    response =  JsonResponse(json.dumps(data),safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


def get_last_4csv(request):

    csv_file = glob.glob(os.path.join(os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2')))
    latest_csv = max(glob.glob('C:/Users/a866098/OneDrive - Atos/Bureau/atos2/*.xlsx'), key=os.path.getctime)
    latest_csv2 = max(glob.glob('C:/Users/a866098/OneDrive - Atos/Bureau/atos2/*.xlsx'), key=os.path.getctime)

    # print("hello",latest_csv)
    # print("hello",latest_csv2)

    folder_path = "/Users/sachin/Desktop/Files/"

    files_path = os.path.join(os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2'), '*')
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    print("files",files)

    data = []
    for i in range(len(files)):
        extension = os.path.splitext(files[i])[1]
        if extension == ".xlsx":
            dure = find_excel_files(files[i])
            print("durehnaya",dure)
            data.append(dure)



    response =  JsonResponse(json.dumps(data),safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


def etude_na2(request):

    jobs_list = ["ISUTI00Y-ISU_MDR_AF_PROC_PART",
    "ISUTI018-ISU_PROG_MAJ_BP",
    "ISUTI01E-FICA_MARQ_CREAN_DOU",
    "ISUTI01F-FICA_TRAN_CREAN_DOU",
    "ISUTI01Z-ISU_PROG_AL_DFKKKOBW",
    "ISUTI025-ISU_ITF_GINKO14",
    "ISUTI02W-ISU_GO_NA_HORS_HEBDO",
    "ISUTI054-FICA_RAPPROCHM_AUTO",
    "ISUTI056-ISU_HIST_CONSO_ANN",
    "ISUTI057-FICA_CYCLE_RELANCE_ACT",
    "ISUTI065-FICA_ENCAISS_DECAISS1",
    "ISUTI069-FICA_CYCLE_RELANCE_PROP",
    "ISUTI071-ISU_INT_MODIF_CONT",
    "ISUTI086-ISU_MDR_ECHE1_DETEC" ,
    "ISUTI400-ISU_NO_GO_NACOMP",
    "ISUTI40K-ISU_MDR_SOUSC_G",
    "ISUTI411-ISU_CALCUL_FACTURAT",
    "ISUTI412-ISU_FACTURATION_ISU",
    "ISUTI420-ISU_ITF_GINKO13",
    "ISUTI421-ISU_ITF_GINKO10",
    "ISUTI42V-EDIT_ISU_SP_B_NRJ_XML",
    "ISUTI42W-EDIT_CONCAT_FACT_XML",
    "ISUTI440-ISU_SPLIT4_D21",
    "ISUTI495-ISU_CALCUL_FACTURAT_ES" ,
    "ISUTI4A9-ISU_INT_IND_G",
    "ISUTI502-FICA_TRAN_PIEC_FIGL",
    "ISUTI50Q-ISU_PRE_ANLYSE_NA",
    "ISUTI62T-ISU_ITF_G14_GAZ",
    "ISUTI66K-ISU_IDENT_IBAN_ANONYM",
    "ISUTI66L-ISU_ANONYM_IBAN"
    ]

    path = os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2',)
    data = []
    for root, dirs, files in os.walk(path):
            # print(root,dirs,files)
            for f in files :
                extension = os.path.splitext(f)[1]
                if extension == ".xlsx":
                    file_data= find_excel_files_durée_all_files(os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2',f))
                    data.append({str(f)[0:-5] : file_data})
    response =  JsonResponse(json.dumps(data),safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


def etude_na3(request):

    jobs_list = ["ISUTI00Y-ISU_MDR_AF_PROC_PART",
    "ISUTI018-ISU_PROG_MAJ_BP",
    "ISUTI01E-FICA_MARQ_CREAN_DOU",
    "ISUTI01F-FICA_TRAN_CREAN_DOU",
    "ISUTI01Z-ISU_PROG_AL_DFKKKOBW",
    "ISUTI025-ISU_ITF_GINKO14",
    "ISUTI02W-ISU_GO_NA_HORS_HEBDO",
    "ISUTI054-FICA_RAPPROCHM_AUTO",
    "ISUTI056-ISU_HIST_CONSO_ANN",
    "ISUTI057-FICA_CYCLE_RELANCE_ACT",
    "ISUTI065-FICA_ENCAISS_DECAISS1",
    "ISUTI069-FICA_CYCLE_RELANCE_PROP",
    "ISUTI071-ISU_INT_MODIF_CONT",
    "ISUTI086-ISU_MDR_ECHE1_DETEC" ,
    "ISUTI400-ISU_NO_GO_NACOMP",
    "ISUTI40K-ISU_MDR_SOUSC_G",
    "ISUTI411-ISU_CALCUL_FACTURAT",
    "ISUTI412-ISU_FACTURATION_ISU",
    "ISUTI420-ISU_ITF_GINKO13",
    "ISUTI421-ISU_ITF_GINKO10",
    "ISUTI42V-EDIT_ISU_SP_B_NRJ_XML",
    "ISUTI42W-EDIT_CONCAT_FACT_XML",
    "ISUTI440-ISU_SPLIT4_D21",
    "ISUTI495-ISU_CALCUL_FACTURAT_ES" ,
    "ISUTI4A9-ISU_INT_IND_G",
    "ISUTI502-FICA_TRAN_PIEC_FIGL",
    "ISUTI50Q-ISU_PRE_ANLYSE_NA",
    "ISUTI62T-ISU_ITF_G14_GAZ",
    "ISUTI66K-ISU_IDENT_IBAN_ANONYM",
    "ISUTI66L-ISU_ANONYM_IBAN"
    ]

    path = os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2',)
    data = []
    for root, dirs, files in os.walk(path):
            # print(root,dirs,files)
            for f in files :
                extension = os.path.splitext(f)[1]
                if extension == ".xlsx":
                    file_data= find_excel_files_end_start(os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2',f))
                    data.append({str(f)[0:-5] : file_data})

    return JsonResponse(json.dumps(data),safe=False)


def etude_na(request):
    path = os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2',)
    print("path hna",path)
    data = []
    for root, dirs, files in os.walk(path):
            # print(root,dirs,files)
            for f in files :
                print("files here",root)
                extension = os.path.splitext(f)[1]
                if extension == ".xlsx":
                    dur= find_excel_files(os.path.join('C:', os.sep, 'Users', 'a866098' , 'OneDrive - Atos','Bureau','atos2',f))
                    data.append({str(f)[0:-5] : dur})

    return JsonResponse(json.dumps(data),safe=False)

