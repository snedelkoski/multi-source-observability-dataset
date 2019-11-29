import pandas as pd
import json
#from bs4 import BeautifulSoup
import fnmatch
from pprint import pprint
import csv
import seaborn as sns
from datetime import datetime
from tqdm import tqdm
import os
import argparse



# Working Parser for skipping DB calls and writing to a dataframe object.

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path to the traces")
ap.add_argument("-o", "--out", required=True,
        help="outputpath to save csv-dump")
args = vars(ap.parse_args())

print(args)



def create_df(data_dir,output_file):
    #creating a null dataframe before starting to fill it
    df_name = pd.DataFrame(columns=['Host', 'Name', 'Service', 'Project', 'Timestamp', 'Iteration_id','Trace_id', 'Parent_id', 'Base_id'])
    list_trace_files=os.listdir(data_dir)
    # tqdm is used to visualize the progress.
    for x in tqdm(list_trace_files):
        #data_folder = 'traces_data/boot_delete_config/traces_new/api_faults/'
        file_to_read = data_dir+'/'+x
        try:
            with open(file_to_read) as trace_file:
                dict_train = json.load(trace_file)
                print("Processing trace_file:",file_to_read)
                #print name of the iteration_id
                #print(os.path.splitext(os.path.basename(file_to_read))[0])
                #print(os.path.splitext(str(list_trace_files)[0]))
                df_name = df_name.from_dict(parser(dict_train,df_name,os.path.splitext(os.path.basename(file_to_read))[0]))
        except:
            print("Error parsing file:",file_to_read)
            print("Saving Data-Frame partially")
            df_name.to_csv(output_file)
            print("--done--")
			
    print("Saving Data-Frame")
    df_name.to_csv(output_file)
    print("--done--")

# Working Parser for skipping DB calls and writing to a dataframe object.

# Working Parser for skipping DB calls and writing to a dataframe object.

def parser(dict_train,dfObj,iteration_id):

    substring ='db'
    pattern = 'meta.raw_payload.*'

    for x in range(len(dict_train['children'])):
        if not dict_train['children'][x]['children']:
            #print("Stage-1")
            #print("No-children present in index", x)
            #print("parent_id:",dict_train['children'][x]['parent_id'])
            #print("trace_id:",dict_train['children'][x]['trace_id'])
            # print("--- Printing Payload information ---")
            # print("Host:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['info']['host'])
            # print("Name:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['name'])
            # print("Service:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['service'])
            # print("Timestamp:",datetime.strptime(dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
            # print("Parent_id:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['parent_id'])
            # print("Trace_id:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['trace_id'])
            # print("Base_id:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['base_id'])
            # print("Project:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['project'])
            dfObj = dfObj.append({'Host': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['info']['host'], 'Name': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['name'], 'Service': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['service'], 'Project': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['trace_id'], 'Parent_id': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['parent_id'], 'Base_id': dict_train['children'][x]['info']['meta.raw_payload.wsgi-start']['base_id']}, ignore_index=True)

            # print("Host:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['info']['host'])
            # print("Name:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['name'])
            # print("Service:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['service'])
            # print("Timestamp:",datetime.strptime(dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
            # print("Parent_id:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['parent_id'])
            # print("Trace_id:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['trace_id'])
            # print("Base_id:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['base_id'])
            # print("Project:",dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['project'])
            dfObj = dfObj.append({'Host': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['info']['host'], 'Name': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['name'], 'Service': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['service'], 'Project': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['trace_id'], 'Parent_id': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['parent_id'], 'Base_id': dict_train['children'][x]['info']['meta.raw_payload.wsgi-stop']['base_id']}, ignore_index=True)


        else:


            #print("Children present in index", x)
            for y in range(len(dict_train['children'][x]['children'])):
                #print("Stage-2")
                #print(len(dict_train['children'][x]['children']))

                if not dict_train['children'][x]['children'][y]['children']:
                    #print("No children to further process in Stage-1")
                    meta_raw_payload_name_stage_1 = fnmatch.filter(dict_train['children'][x]['children'][y]['info'],pattern)
                    #print("List of payload types:",meta_raw_payload_name_stage_1)

                    for k in range(len(meta_raw_payload_name_stage_1)):
                        if substring in meta_raw_payload_name_stage_1[k]:
                            #compute something
                            pass
                            #print("Payload are DB-calls stage-2 , Skipping...",meta_raw_payload_name_stage_1[k])
                        else:

                            # print("--- Printing Payload information ---")
                            # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_1[k])
                            # print("Host:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['info']['host'])
                            # print("Name:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['name'])
                            # print("Service:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['service'])
                            # print("Project:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['project'])
                            # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                            # print("Trace_id:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['trace_id'])
                            # print("Parent_id:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['parent_id'])
                            # print("Base_id:",dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['base_id'])
                            dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['info'][meta_raw_payload_name_stage_1[k]]['base_id']}, ignore_index=True)




                else:
                    #print("Children present in stage-2 index", x,y)
                    for z in range(len(dict_train['children'][x]['children'][y]['children'])):
                        #print("Stage-3")
                        #print(len(dict_train['children'][x]['children'][y]['children']))

                        if not dict_train['children'][x]['children'][y]['children'][z]['children']:
                            #print("No children to further process in Stage-2")
                            meta_raw_payload_name_stage_2 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['info'],pattern)
                            #print("List of payload types:",meta_raw_payload_name_stage_2)
                            for k in range(len(meta_raw_payload_name_stage_2)):
                                if substring in meta_raw_payload_name_stage_2[k]:
                                    #compute something
                                    pass
                                    #print("Payload are DB-calls stage-3 , Skipping...",meta_raw_payload_name_stage_2[k])
                                else:
                                    # print("--- Printing Payload information ---")
                                    # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_2[k])
                                    # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['info']['host'])
                                    # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['name'])
                                    # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['service'])
                                    # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['project'])
                                    # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                    # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['trace_id'])
                                    # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['parent_id'])
                                    # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['base_id'])
                                    dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['info'][meta_raw_payload_name_stage_2[k]]['base_id']}, ignore_index=True)





                        else:
                            #print("Children present in stage-3 index", x,y,z)

                            for a in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'])):
                                #print("Stage-4")
                                #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children']))

                                if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children']:
                                    #print("No children to further process in Stage-3")
                                    meta_raw_payload_name_stage_3 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'],pattern)
                                    #print("List of payload types:",meta_raw_payload_name_stage_3)
                                    for k in range(len(meta_raw_payload_name_stage_3)):
                                        if substring in meta_raw_payload_name_stage_3[k]:
                                            #compute something
                                            pass
                                            #print("Payload are DB-calls stage-4 , Skipping...",meta_raw_payload_name_stage_3[k])
                                        else:
                                            # print("--- Printing Payload information ---")
                                            # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_3[k])
                                            # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['info']['host'])
                                            # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['name'])
                                            # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['service'])
                                            # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['project'])
                                            # #print("Timestamp:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['timestamp'])
                                            # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                            # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['trace_id'])
                                            # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['parent_id'])
                                            # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['base_id'])
                                            dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['info'][meta_raw_payload_name_stage_3[k]]['base_id']}, ignore_index=True)




                                else:
                                    #print("Children present in stage-4 index", x,y,z,a)
                                    for b in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'])):
                                        #print("Stage-5")
                                        #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children']))
                                        if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children']:
                                            #print("No children to further process in Stage-4")
                                            meta_raw_payload_name_stage_4 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'],pattern)
                                            #print("List of payload types:",meta_raw_payload_name_stage_4)
                                            for k in range(len(meta_raw_payload_name_stage_4)):
                                                if substring in meta_raw_payload_name_stage_4[k]:
                                                    #compute something
                                                    pass
                                                    #print("Payload are DB-calls stage-5 , Skipping...",meta_raw_payload_name_stage_4[k])
                                                else:
                                                    # print("--- Printing Payload information ---")
                                                    # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_4[k])
                                                    # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['info']['host'])
                                                    # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['name'])
                                                    # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['service'])
                                                    # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['project'])
                                                    #
                                                    # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                    # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['trace_id'])
                                                    # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['parent_id'])
                                                    # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['base_id'])

                                                    dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['info'][meta_raw_payload_name_stage_4[k]]['base_id']}, ignore_index=True)



                                        else:
                                            #print("Children present in stage-5 index", x,y,z,a,b)
                                            for c in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'])):
                                                #print("Stage-6")
                                                #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children']))
                                                if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']:
                                                    #print("No children to further process in Stage-5")
                                                    meta_raw_payload_name_stage_5 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'],pattern)
                                                    #print("List of payload types:",meta_raw_payload_name_stage_5)
                                                    for k in range(len(meta_raw_payload_name_stage_5)):
                                                        if substring in meta_raw_payload_name_stage_5[k]:
                                                            #compute something
                                                            pass
                                                            #print("Payload are DB-calls stage-6 , Skipping...",meta_raw_payload_name_stage_5[k])
                                                        else:
                                                            # print("--- Printing Payload information ---")
                                                            # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_5[k])
                                                            # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['info']['host'])
                                                            # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['name'])
                                                            # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['service'])
                                                            # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['project'])
                                                            #
                                                            # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                            # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['trace_id'])
                                                            # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['parent_id'])
                                                            # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['base_id'])

                                                            dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['info'][meta_raw_payload_name_stage_5[k]]['base_id']}, ignore_index=True)




                                                else:
                                                    #print("Children present in stage-6 index", x,y,z,a,b,c)
                                                    for d in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'])):
                                                        #print("Stage-7")
                                                        #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']))
                                                        if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children']:
                                                            #print("No children to further process in Stage-6")
                                                            meta_raw_payload_name_stage_6 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'],pattern)
                                                            #print("List of payload types:",meta_raw_payload_name_stage_6)
                                                            for k in range(len(meta_raw_payload_name_stage_6)):
                                                                if substring in meta_raw_payload_name_stage_6[k]:
                                                                    #compute something
                                                                    pass
                                                                    #print("Payload are DB-calls stage-7 , Skipping...",meta_raw_payload_name_stage_6[k])
                                                                else:
                                                                    # print("--- Printing Payload information ---")
                                                                    # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_6[k])
                                                                    # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['info']['host'])
                                                                    # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['name'])
                                                                    # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['service'])
                                                                    # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['project'])
                                                                    # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                    # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['trace_id'])
                                                                    # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['parent_id'])
                                                                    # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['base_id'])

                                                                    dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['info'][meta_raw_payload_name_stage_6[k]]['base_id']}, ignore_index=True)





                                                        else:

                                                            for e in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'])):
                                                                #print("Stage-8")
                                                                if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children']:
                                                                    meta_raw_payload_name_stage_7 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'],pattern)
                                                                    for k in range(len(meta_raw_payload_name_stage_7)):
                                                                        if substring in meta_raw_payload_name_stage_7[k]:
                                                                            #compute something
                                                                            pass
                                                                            #print("Payload are DB-calls stage-8 , Skipping...",meta_raw_payload_name_stage_7[k])
                                                                        else:
                                                                            # print("--- Printing Payload information ---")
                                                                            # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_7[k])
                                                                            # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['info']['host'])
                                                                            # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['name'])
                                                                            # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['service'])
                                                                            # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['project'])
                                                                            # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                            # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['trace_id'])
                                                                            # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['parent_id'])
                                                                            # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['base_id'])

                                                                            dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['info'][meta_raw_payload_name_stage_7[k]]['base_id']}, ignore_index=True)




                                                                else:
                                                                    #print("Children present in stage-8 index", x,y,z,a,b,c,d,e)

                                                                    for f in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'])):
                                                                        #print("Stage-9")
                                                                        #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']))
                                                                        if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children']:
                                                                            #print("No children to further process in Stage-6")
                                                                            meta_raw_payload_name_stage_8 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'],pattern)
                                                                            #print("List of payload types:",meta_raw_payload_name_stage_6)
                                                                            for k in range(len(meta_raw_payload_name_stage_8)):
                                                                                if substring in meta_raw_payload_name_stage_8[k]:
                                                                                    #compute something
                                                                                    pass
                                                                                    #print("Payload are DB-calls stage-9 , Skipping...",meta_raw_payload_name_stage_8[k])
                                                                                else:
                                                                                    # print("--- Printing Payload information ---")
                                                                                    # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_8[k])
                                                                                    # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['info']['host'])
                                                                                    # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['name'])
                                                                                    # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['service'])
                                                                                    # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['project'])
                                                                                    # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                                    # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['trace_id'])
                                                                                    # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['parent_id'])
                                                                                    # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['base_id'])

                                                                                    dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['info'][meta_raw_payload_name_stage_8[k]]['base_id']}, ignore_index=True)




                                                                        else:
                                                                            #print("Children present in stage-9 index", x,y,z,a,b,c,d,e,f)

                                                                            for g in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'])):
                                                                                #print("Stage-10")
                                                                                #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']))
                                                                                if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children']:
                                                                                    #print("No children to further process in Stage-6")
                                                                                    meta_raw_payload_name_stage_9 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'],pattern)
                                                                                    #print("List of payload types:",meta_raw_payload_name_stage_6)
                                                                                    for k in range(len(meta_raw_payload_name_stage_9)):
                                                                                        if substring in meta_raw_payload_name_stage_9[k]:
                                                                                            #compute something
                                                                                            pass
                                                                                            #print("Payload are DB-calls stage-10 , Skipping...",meta_raw_payload_name_stage_9[k])
                                                                                        else:
                                                                                            # print("--- Printing Payload information ---")
                                                                                            # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_9[k])
                                                                                            # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['info']['host'])
                                                                                            # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['name'])
                                                                                            # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['service'])
                                                                                            # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['project'])
                                                                                            # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                                            # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['trace_id'])
                                                                                            # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['parent_id'])
                                                                                            # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['base_id'])

                                                                                            dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['info'][meta_raw_payload_name_stage_9[k]]['base_id']}, ignore_index=True)




                                                                                else:
                                                                                    #print("Children present in stage-10 index", x,y,z,a,b,c,d,e,f,g)

                                                                                    for h in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'])):
                                                                                        #print("Stage-11")
                                                                                        #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']))
                                                                                        if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children']:
                                                                                            #print("No children to further process in Stage-6")
                                                                                            meta_raw_payload_name_stage_10 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'],pattern)
                                                                                            #print("List of payload types:",meta_raw_payload_name_stage_6)
                                                                                            for k in range(len(meta_raw_payload_name_stage_10)):
                                                                                                if substring in meta_raw_payload_name_stage_10[k]:
                                                                                                    #compute something
                                                                                                    pass
                                                                                                    #print("Payload are DB-calls stage-11 , Skipping...",meta_raw_payload_name_stage_10[k])
                                                                                                else:
                                                                                                    # print("--- Printing Payload information ---")
                                                                                                    # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_10[k])
                                                                                                    # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['info']['host'])
                                                                                                    # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['name'])
                                                                                                    # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['service'])
                                                                                                    # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['project'])
                                                                                                    # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                                                    # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['trace_id'])
                                                                                                    # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['parent_id'])
                                                                                                    # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['base_id'])

                                                                                                    dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['info'][meta_raw_payload_name_stage_10[k]]['base_id']}, ignore_index=True)




                                                                                        else:
                                                                                            #print("Children present in stage-11 index", x,y,z,a,b,c,d,e,f,g,h)

                                                                                            for i in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'])):
                                                                                                # print("Stage-12")
                                                                                                #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']))
                                                                                                if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children']:
                                                                                                    #print("No children to further process in Stage-6")
                                                                                                    meta_raw_payload_name_stage_11 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'],pattern)
                                                                                                    #print("List of payload types:",meta_raw_payload_name_stage_6)
                                                                                                    for k in range(len(meta_raw_payload_name_stage_11)):
                                                                                                        if substring in meta_raw_payload_name_stage_11[k]:
                                                                                                            #compute something
                                                                                                            pass
                                                                                                            #print("Payload are DB-calls stage-12 , Skipping...",meta_raw_payload_name_stage_11[k])
                                                                                                        else:
                                                                                                            # print("--- Printing Payload information ---")
                                                                                                            # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_11[k])
                                                                                                            # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['info']['host'])
                                                                                                            # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['name'])
                                                                                                            # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['service'])
                                                                                                            # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['project'])
                                                                                                            # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                                                            # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['trace_id'])
                                                                                                            # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['parent_id'])
                                                                                                            # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['base_id'])

                                                                                                            dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['base_id']}, ignore_index=True)






                                                                                                else:
                                                                                                    #print("Children present in stage-12 index", x,y,z,a,b,c,d,e,f,g,h,i)

                                                                                                    for j in range(len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'])):
                                                                                                # print("Stage-12")
                                                                                                #print("Length",len(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children']))
                                                                                                        if not dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['children']:
                                                                                                            #print("No children to further process in Stage-6")
                                                                                                            meta_raw_payload_name_stage_12 = fnmatch.filter(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'],pattern)

                                                                                                            #print("List of payload types:",meta_raw_payload_name_stage_6)
                                                                                                            for k in range(len(meta_raw_payload_name_stage_12)):
                                                                                                                if substring in meta_raw_payload_name_stage_12[k]:
                                                                                                                    #compute something
                                                                                                                    pass
                                                                                                                    #print("Payload are DB-calls stage-12 , Skipping...",meta_raw_payload_name_stage_11[k])
                                                                                                                else:
                                                                                                                    # print("--- Printing Payload information ---")
                                                                                                                    # print("Printing Pay-Load infomarion for:",meta_raw_payload_name_stage_11[k])
                                                                                                                    # print("Host:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['info']['host'])
                                                                                                                    # print("Name:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['name'])
                                                                                                                    # print("Service:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['service'])
                                                                                                                    # print("Project:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['project'])
                                                                                                                    # print("Timestamp:", datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
                                                                                                                    # print("Trace_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['trace_id'])
                                                                                                                    # print("Parent_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['parent_id'])
                                                                                                                    # print("Base_id:",dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['info'][meta_raw_payload_name_stage_11[k]]['base_id'])

                                                                                                                    dfObj = dfObj.append({'Host': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['info']['host'], 'Name': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['name'], 'Service': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['service'], 'Project': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['project'], 'Timestamp': datetime.strptime(dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'), 'Iteration_id': iteration_id, 'Trace_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['trace_id'], 'Parent_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['parent_id'], 'Base_id': dict_train['children'][x]['children'][y]['children'][z]['children'][a]['children'][b]['children'][c]['children'][d]['children'][e]['children'][f]['children'][g]['children'][h]['children'][i]['children'][j]['info'][meta_raw_payload_name_stage_12[k]]['base_id']}, ignore_index=True)

                                                                                                        else:
                                                                                                            print("Children present in stage-13 index", x,y,z,a,b,c,d,e,f,g,h,i,j)




    return dfObj




















#create_df('/var/lib/rally_container/boot_delete_config/traces_new/compute_faults','dataframe_compute_faults')

create_df(args["path"], args["out"])

