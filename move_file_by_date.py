import os  
from PIL import Image  
import maya
import datetime

def get_file_data(file_path):
    # try to use image exif info
    try:
        with Image.open(file_path) as img:  
            exif_data = img._getexif()  
            if exif_data is not None:
                if 36867 in exif_data:
                    date_time = exif_data[36867]
                    date_time = maya.parse(str(date_time)).datetime() 
                    print(file_path + " Use exif create time " + str(date_time))
                    return date_time
                elif 306 in exif_data:                
                    date_time = maya.parse(exif_data[306]).datetime()
                    print(file_path + " Use exif modify time " + str(date_time))
                    return date_time
    except Exception as e:
        print("Some erro in get exif data ",e)
    
    #use file modify time
    date_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    print(file_path + " Use file modify time " + str(date_time))
    return date_time

def sort_files(file_dir, target_dir):  
    for filename in os.listdir(file_dir): 
        file_full_name = os.path.join(file_dir, filename) 
        if(os.path.isdir(file_full_name)): continue
        date_time = get_file_data(file_full_name)         
        date_time_str = date_time.strftime('%Y:%m:%d %H:%M:%S')  
        year = date_time_str.split(':')[0]  
        month = date_time_str.split(':')[1]  
        # Create Month and Day Dir
        year_dir = os.path.join(target_dir, year)  
        month_dir = os.path.join(year_dir, month)  
        if not os.path.exists(year_dir):  
            os.makedirs(year_dir)  
        if not os.path.exists(month_dir):  
            os.makedirs(month_dir)  
        # Move source file to target dir
        src_path = os.path.join(file_dir, filename)  
        dst_path = os.path.join(month_dir, filename)  
        os.rename(src_path, dst_path)
        print("Move " + filename)
  
if __name__ == '__main__':  
    file_dir = input("Please input file source path: ")
    target_dir = input("Please input file output root path: ")
    sort_files(file_dir, target_dir)  
    print("Done")