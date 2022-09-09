from django.shortcuts import render
import glob
from pandas import read_excel
from django.http import JsonResponse
import json
import csv
from datetime import datetime
import os
from .models import History
from . import models
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib import  auth
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/graph/login')
def index(request):
    return render(request, "graph/index.html")



@login_required(login_url='/graph/login')

def index2(request):
    return render(request, "graph/index2.html")

@login_required(login_url='/graph/login')
def index3(request):
    return render(request, "graph/index3.html")

@login_required(login_url='/graph/login')
def index4(request,date,job):
    return render(request, "graph/index4.html")

@login_required(login_url='/graph/login')
def index14(request,date,job):
    return render(request, "graph/index14.html")

from django.db.models import Max


@login_required(login_url='/graph/login')
def accueil(request):
    data_index = History.objects.all().latest('order_date')

    data = History.objects.filter(order_date=data_index.order_date).order_by('-order_date')
    list_valid = []
    print(len(data))
    for k in data:
        if k.job_mem_name in jobs_list:
            list_valid.append(k)

    print("data here",list_valid)
    return render(request, "graph/accueil.html",{"context" : list_valid , 'last_insert' : data_index.order_date , 'type' : data_index.sched_table})


def logout(request):

        auth.logout(request)
        return redirect('/graph/login')



def recherche_accueil(request,date):
    string = date[0:2] + '/' + date[2:4] + '/' + date[4:8]
    print(string)
    data = History.objects.filter(order_date=string).order_by('-order_date')

    list_valid = []

    for x in data:

            if x.end_time == "" or x.end_time == "":
                diff=0
            else:
                d1 = datetime.strptime(x.end_time, '%d/%m/%Y %H:%M:%S')
                d2 = datetime.strptime(x.start_time, '%d/%m/%Y %H:%M:%S')
                diff=(d1 - d2)

            if x.job_mem_name in jobs_list:
                 list_valid.append({"job_mem_name" : x.job_mem_name,
                                    "order_date" : str(x.order_date),
                                    "start_time" : str(x.start_time),
                                    "end_time" : str(x.end_time),
                                    "exec_time" : str(diff),
                                    "status" : x.status
                                    })

    print(list_valid)
    return JsonResponse(json.dumps(list_valid), safe=False)


from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import pandas as pd
import codecs
import csv

def login(request):
    print(request.POST)

    if request.method == "POST":
        username  = request.POST.get("username")
        pwd = request.POST.get("password")



        user = authenticate(request, username=username, password=pwd)
        print("user here",user)
        if user is not None:
            auth.login(request, user)
            return redirect('graph/accueil')

        else:
              return redirect('/graph/login')

    else:
        return render(request, "graph/authentication-login.html")



def get_duration_per_task(request,date):
    data_ream = '{0}/{1}/{2}'.format(date[0:2], date[2:4], date[4:8])
    data= []
    data_= []
    for j in jobs_list:
        job_row = History.objects.filter(order_date=data_ream,job_mem_name=j,sched_table="ESMMTAV01")
        job_row_type2 = History.objects.filter(order_date=data_ream,job_mem_name=j,sched_table="ESMMPRE01")
        if job_row:
                print(job_row.values()[0]["start_time"])
                val = job_row.values()[0]
                if val["end_time"] != "" and val["start_time"] != "":

                    d1 = datetime.strptime(val["end_time"], '%d/%m/%Y %H:%M:%S')
                    d2 = datetime.strptime(val["start_time"], '%d/%m/%Y %H:%M:%S')
                    diff = (d1 - d2)
                    data.append({str(j) :str(diff) , "start_time" : val["start_time"]  , "end_time": val["end_time"]  })


        if job_row_type2 :
            val2 = job_row_type2.values()[0]
            if val2["end_time"] != "" and val2["start_time"] !="" :
                d1_ = datetime.strptime(val2["end_time"], '%d/%m/%Y %H:%M:%S')
                d2_ = datetime.strptime(val2["start_time"], '%d/%m/%Y %H:%M:%S')
                diff_ = (d1_ - d2_)
                data_.append({str(j) :str(diff_),"start_time" : val2["start_time"]  , "end_time": val2["end_time"] })
                print(len(data))


    print(len(data),len(data_))
    return JsonResponse({"ESMMTAV01" : json.dumps(data),
                         "ESMMPRE01" : json.dumps(data_)
                         },safe=False)

def end_time_start_time(request,date):
    data_ream = '{0}/{1}/{2}'.format(date[0:2], date[2:4], date[4:8])
    data= []
    data_= []
    for j in jobs_list:
        job_row = History.objects.filter(order_date=data_ream,job_mem_name=j,sched_table="ESMMTAV01")
        job_row_type2 = History.objects.filter(order_date=data_ream,job_mem_name=j,sched_table="ESMMPRE01")
        if job_row:
            print(job_row.values()[0]["start_time"])
            val = job_row.values()[0]

            data.append({str(j) : j ,"start_time" : val["start_time"]  , "end_time": val["end_time"]})


        if job_row_type2 :
            val2 = job_row_type2.values()[0]
            data_.append({str(j) : j ,"start_time" : val2["start_time"]  , "end_time": val2["end_time"]})
            print(len(data))


    print(len(data),len(data_))
    return JsonResponse({"ESMMTAV01" : json.dumps(data),
                         "ESMMPRE01" : json.dumps(data_)
                         },safe=False)



@csrf_exempt
def update_dashboard(request):
    if request.method == 'POST':
        print(request.FILES)
        file = request.FILES['file']
        read = pd.read_csv(file).values.tolist()
        # print(read)
        for row in read:
            print('row here',row)
            try:
                data = str(row).split(';')
                # print("data",len(data))
                data = History.objects.create(job_mem_name=data[0][2:],
                                           start_time = data[4],
                                           sched_table = data[2],
                                           end_time=data[5],
                                           order_date=data[6][:-2],
                                           status=data[1],
                                           node_group=data[3]
                                              )



                data.save()
            except:
                continue


    return JsonResponse("hello",safe=False)
    return render(request, "graph/accueil.html",{"context" : data})


def filtre(request,date,job):
    data_ream = '{0}/{1}'.format(date[0:2], date[2:6])
    print("date ,",data_ream)
    data = models.History.objects.filter(order_date__icontains=data_ream,job_mem_name=job).order_by('order_date')

    data_month = []
    datas = []

    v01 = []

    pre = []

    for x in data:
                if x.end_time == "" or x.start_time == "":
                    continue
                d1 = datetime.strptime(x.end_time, '%d/%m/%Y %H:%M:%S')
                d2 = datetime.strptime(x.start_time, '%d/%m/%Y %H:%M:%S')
                diff = (d1 - d2)


                if x.sched_table == 'ESMMTAV01':
                    v01.append({'start_time' : x.start_time , "end_time" : x.end_time ,'date': str(x.order_date), "dure": str(diff) , "type":x.sched_table  })
                elif x.sched_table == 'ESMMPRE01':
                    pre.append({'start_time' : x.start_time , "end_time" : x.end_time ,'date': str(x.order_date), "dure": str(diff) , "type":x.sched_table  })

    return JsonResponse({"ESMMTAV01" : v01 , "ESMMPRE01" :pre })



def check_sup_1(first,last,count):
    dESMMTAV01 = datetime.strptime(data_day[max_1 - count].end_time, '%Y-%m-%d %H:%M:%S')
    dESMMTAV0l = datetime.strptime(data_day[0].start_time, '%Y-%m-%d %H:%M:%S')

    diff_2_ESMMTAV01 = (dESMMTAV01 - dESMMTAV0l)

    if diff_2_ESMMTAV01.days > 1:
        l = count  + 1
        check_sup_1(first,last,l)





def filtre_NA(request, date):
    # 082022
    data_ream = '{0}/{1}'.format(date[0:2], date[2:5])
    print('ream date', data_ream)
    data_1 = models.History.objects.filter(order_date__icontains=data_ream,
                                           sched_table='ESMMTAV01').order_by("start_time")
    data_2 = models.History.objects.filter(order_date__icontains=data_ream,
                                           sched_table='ESMMPRE01').order_by("start_time")


    k = []
    datas_ESMMTAV01 = []

    position = 0
    counter = 0
    match = []
    print(len(data_1))
    start_time = ""
    end_time = ""
    for ESMMTAV01 in data_1:
        position = int(str(ESMMTAV01.order_date)[0:2])

        if match == []:
            if ESMMTAV01.job_mem_name == "ISUTI50Q-ISU_PRE_ANLYSE_NA"  and  ESMMTAV01.start_time != "":
                start_time = datetime.strptime(ESMMTAV01.start_time, '%d/%m/%Y %H:%M:%S')

            if (ESMMTAV01.job_mem_name == "FINNA501-ISU_PROG_FIN_NA" or ESMMTAV01.job_mem_name =="FINNA521-BW_PROG_FIN_NA"  or ESMMTAV01.job_mem_name=="FINNA511-CRM_PROG_FIN_NA") and  ESMMTAV01.end_time != "":
                end_time = datetime.strptime(ESMMTAV01.end_time, '%d/%m/%Y %H:%M:%S')

            if end_time == "" or  start_time == "":
                continue

            match.append((position, ESMMTAV01.start_time))
            print("dad",start_time,end_time)
            diff_2_ESMMTAV01 = (end_time - start_time)

            datas_ESMMTAV01.append({str(ESMMTAV01.order_date) :
                        str(diff_2_ESMMTAV01)})

            start_time = ""
            end_time = ""

        if match[0][0] != position:


            if ESMMTAV01.job_mem_name == "ISUTI50Q-ISU_PRE_ANLYSE_NA"  and  ESMMTAV01.start_time != "":
                start_time = datetime.strptime(ESMMTAV01.start_time, '%d/%m/%Y %H:%M:%S')

            if (ESMMTAV01.job_mem_name == "FINNA501-ISU_PROG_FIN_NA" or ESMMTAV01.job_mem_name == "FINNA521-BW_PROG_FIN_NA" or ESMMTAV01.job_mem_name == "FINNA511-CRM_PROG_FIN_NA") and ESMMTAV01.end_time != "":
                end_time = datetime.strptime(ESMMTAV01.end_time, '%d/%m/%Y %H:%M:%S')

            if start_time == "" or end_time == "":
                continue

            diff_2_ESMMTAV01 = (end_time - start_time)

            datas_ESMMTAV01.append({str(ESMMTAV01.order_date):
                                        str(diff_2_ESMMTAV01)})
            match = []
            match.append((position, ESMMTAV01.start_time))
            start_time = ""
            end_time = ""

        counter = counter + 1

    # if datas_ESMMTAV01 == [] and len(data_1) != 0:
    #     print("hihih here")
    #     le = len(data_1)
    #     if data_1[le - 1].end_time != "" and data_1[0].start_time != "":
    #         print(data_1[le - 1].end_time,data_1[0].start_time)
    #         end_time = datetime.strptime(data_1[le - 1].end_time, '%d/%m/%Y %H:%M:%S')
    #         start_time = datetime.strptime(data_1[0].start_time, '%d/%m/%Y %H:%M:%S')
    #         diff_2_ESMMTAV01 = (end_time - start_time)
    #         datas_ESMMTAV01.append({str(data_1[0].order_date) : str(diff_2_ESMMTAV01)})

    print("chikola hna ",datas_ESMMTAV01)


    k = []
    datas_ESMMTAV01_2 = []
    position = 0
    counter = 0
    match = []
    for ESMMTAV01 in data_2:
        position = int(str(ESMMTAV01.order_date)[0:2])
        if match == []:
            if ESMMTAV01.job_mem_name == "ISUTI50Q-ISU_PRE_ANLYSE_NA" and ESMMTAV01.start_time != "":
                start_time = datetime.strptime(ESMMTAV01.start_time, '%d/%m/%Y %H:%M:%S')

            if (ESMMTAV01.job_mem_name == "FINNA501-ISU_PROG_FIN_NA" or ESMMTAV01.job_mem_name == "FINNA521-BW_PROG_FIN_NA" or ESMMTAV01.job_mem_name == "FINNA511-CRM_PROG_FIN_NA") and ESMMTAV01.end_time != "":
                end_time = datetime.strptime(ESMMTAV01.end_time, '%d/%m/%Y %H:%M:%S')

            if end_time == "" or start_time == "":
                continue

            match.append((position, ESMMTAV01.start_time))
            diff_2_ESMMTAV01 = (end_time - start_time)

            datas_ESMMTAV01_2.append({str(ESMMTAV01.order_date):
                                        str(diff_2_ESMMTAV01)})

            start_time = ""
            end_time = ""


        if match[0][0] != position:
            if ESMMTAV01.job_mem_name == "ISUTI50Q-ISU_PRE_ANLYSE_NA" and ESMMTAV01.start_time != "":
                start_time = datetime.strptime(ESMMTAV01.start_time, '%d/%m/%Y %H:%M:%S')

            if (
                    ESMMTAV01.job_mem_name == "FINNA501-ISU_PROG_FIN_NA" or ESMMTAV01.job_mem_name == "FINNA521-BW_PROG_FIN_NA" or ESMMTAV01.job_mem_name == "FINNA511-CRM_PROG_FIN_NA") and ESMMTAV01.end_time != "":
                end_time = datetime.strptime(ESMMTAV01.end_time, '%d/%m/%Y %H:%M:%S')

            if end_time == "" or start_time == "":
                continue

            diff_2_ESMMTAV01 = (end_time - start_time)
            datas_ESMMTAV01_2.append({str(ESMMTAV01.order_date) :  str(diff_2_ESMMTAV01)})
            match = []
            match.append((position, ESMMTAV01.start_time))

        counter = counter + 1


    # if datas_ESMMTAV01_2 == [] and len(data_2) != 0:
    #     le = len(data_2)
    #     if data_2[le - 1].end_time == "" or data_2[0].start_time == "":
    #         end_time = datetime.strptime(data_1[le - 1].end_time, '%d/%m/%Y %H:%M:%S')
    #         start_time = datetime.strptime(data_1[0].start_time, '%d/%m/%Y %H:%M:%S')
    #         diff_2_ESMMTAV01 = (end_time - start_time)
    #         datas_ESMMTAV01_2.append({str(data_1[0].order_date): str(diff_2_ESMMTAV01)})
    #


    return JsonResponse({"ESMMTAV01": json.dumps(datas_ESMMTAV01), "ESMMPRE01": json.dumps(datas_ESMMTAV01_2)},
                        safe=False)


@login_required(login_url='/graph/login')
def indextest(request,date2,date):
    return render(request, "graph/indextest.html")

@login_required(login_url='/graph/login')
def indextest11(request,date2,date):
    return render(request, "graph/indextest11.html")


@login_required(login_url='/graph/login')
def indextest2(request,date):
    return render(request, "graph/indextest2.html")

@login_required(login_url='/graph/login')
def indextest22(request,date):
    return render(request, "graph/indextest22.html")

@login_required(login_url='/graph/login')
def index5(request):
    return render(request, "graph/index5.html")

@login_required(login_url='/graph/login')
def index52(request):
    return render(request, "graph/index52.html")

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


def get_last_4csv2(request):
    ESMMTAV01_data = []
    ESMMPRE01_data = []

    dz = History.objects.filter(start_time__gt=0, end_time__gt=0).distinct('order_date').order_by('-order_date')[:4]

    for x in jobs_list:

        for z in dz:
            ESMMTAV01 = History.objects.filter(sched_table='ESMMTAV01', order_date=z.order_date, start_time__gt=0,
                                               end_time__gt=0)

            for d in ESMMTAV01:
                if x == d.job_mem_name:
                    if d.start_time == "" or d.end_time == "":
                        continue


                    start_time = datetime.strptime(d.start_time, '%d/%m/%Y %H:%M:%S')
                    end_time = datetime.strptime(d.end_time, '%d/%m/%Y %H:%M:%S')
                    ESMMTAV01_data.append({x: str(end_time - start_time)})



    for x in jobs_list:
        for zd in dz:
            ESMMPRE01 = History.objects.filter(sched_table='ESMMPRE01', order_date=zd.order_date, start_time__gt=0,
                                               end_time__gt=0)

            for kk in ESMMPRE01:
                if x == kk.job_mem_name:
                    if kk.start_time == "" or kk.end_time == "":
                        continue
                    start_time = datetime.strptime(kk.start_time, '%d/%m/%Y %H:%M:%S')
                    end_time = datetime.strptime(kk.end_time, '%d/%m/%Y %H:%M:%S')
                    ESMMPRE01_data.append({x: str(end_time - start_time)})



    response = JsonResponse(json.dumps({"ESMMTAV01": ESMMTAV01_data, "ESMMPRE01": ESMMPRE01_data}), safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


def get_last_4csv(request):
    fina_data = []
    d = History.objects.filter(start_time__gt=0, end_time__gt=0).distinct('order_date').order_by('-order_date')[:4]

    for x in d:
        print(x.start_time, x.end_time)
        zz = History.objects.filter(order_date=x.order_date, start_time__gt=0, end_time__gt=0)
        start_time = ""
        end_time = ""
        for ob in zz:
            if ob.job_mem_name == "ISUTI50Q-ISU_PRE_ANLYSE_NA" and ob.start_time != "":
                start_time = datetime.strptime(ob.start_time, '%d/%m/%Y %H:%M:%S')

            if (
                    ob.job_mem_name == "FINNA501-ISU_PROG_FIN_NA" or ob.job_mem_name == "FINNA521-BW_PROG_FIN_NA" or ob.job_mem_name == "FINNA511-CRM_PROG_FIN_NA") and ob.end_time != "":
                end_time = datetime.strptime(ob.end_time, '%d/%m/%Y %H:%M:%S')

            if end_time == "" or start_time == "":
                continue

        if end_time != "" and start_time != "":
            # fina_data.append({"order_date" : x.order_date , "dure" :str(end_time-start_time)})
            fina_data.append(str(end_time - start_time))

    print(fina_data)
    response = JsonResponse(json.dumps(fina_data), safe=False)
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



# def update_rows(request):
#     data = History.objects.all()
#
#
#
#     for d in data:
#         string = d.order_date
#         new_string = string[6:8] + '/' + string [4:6] + '/' + string[0:4]
#         d.order_date = new_string
#         d.save()
#
#     return JsonResponse(new_string,safe=False)
