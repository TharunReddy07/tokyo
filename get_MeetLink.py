import pandas as pd
from python_sheets import get_data

def Link(msg):
    if len(msg) < 3 :
        return (msg)
    else :
        if msg[0:3] == 'bot':
            meetLink = 'Not Found'
            bot, course, course_id, section = map(str, msg.split())
            course = course.lower()
            section = section.lower()
            indices_data = pd.read_excel(r'.\indices\%s.xlsx'%(course+'_indices'))
            i_from = 'None'
            i_to = 'None'
             
            m = len(indices_data)
            for j in range(0, m):
                if indices_data.at[j, 'course_id'] == course_id:
                    i_from = indices_data.at[j, 'from']
                    i_to = indices_data.at[j, 'to']
                    break            
            
            if i_from != 'None' :
                data = get_data(course, 'None', int(i_from)-1, int(i_to)-1)              
                n = len(data)
                course = data.at[0, 'course_title']
                for i in range(0, n) :
                    if section == data.at[i, 'section'].lower():
                        meetLink = data.at[i, 'link']
                        faculty = data.at[i, 'faculty']
                        if meetLink == '':
                            meetLink = 'Not found in the Database'
                        return("{}\n{} - {}\n{}".format(course.upper(), section.upper(), faculty, meetLink))
                    else :
                        pass                    
            if j == m:
                return(course.upper() + course_id.upper() + ' not found in the Database')
            elif meetLink == 'Not Found' :
                return("There's no "+ section.upper() + ' in '+ course.upper())
            else:
                pass                              
        else:
            return(str(msg))    