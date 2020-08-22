import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def get_data(course, indices, i_from, i_to) :
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("ExcelSheets-55bed763e1a3.json", scope)
    
    if indices == 'None':
        client = gspread.authorize(creds)
        sheet = client.open("%s"%(course)).sheet1  
        data = sheet.get_all_records()  
        df = pd.DataFrame(data[i_from:i_to], columns=data[0])
    else:
        course = course+indices
        client = gspread.authorize(creds)
        sheet = client.open("%s"%(course)).sheet1  
        data = sheet.get_all_records() 
        df = pd.DataFrame(data[0:], columns=data[0])
    
    return df