import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        Firstname, filetype = os.path.splitext(filename)
        if 'Unclassified' in Firstname:
            pass
        else: 
            Firstname_parts = Firstname.split('.')
            new_filename = f'IM{Firstname_parts[-3]}.{Firstname_parts[-2]}_{Firstname_parts[-1]}{filetype}'
            #print(f'New filename: {new_filename}')
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    

#folder_path = r'C:\Users\dward\Downloads\Post'
#rename_files(folder_path)


import pyautogui
import time

i=1

def click_and_enter():
    global i
    if i ==1:        
        time.sleep(10)
        i=i+1
    else:
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)


while True:
    click_and_enter()
