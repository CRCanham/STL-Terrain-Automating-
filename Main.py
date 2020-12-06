import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import zipfile36 as zipfile
import glob


def download(lat, lng):
    # latitude box
    lat_box = driver.find_element_by_id('c-lat')
    lat_box.send_keys(Keys.CONTROL, "a")
    lat_box.send_keys(lat)

    # longtitude box
    lng_box = driver.find_element_by_id('c-lng')
    lng_box.send_keys(Keys.CONTROL, "a")
    lng_box.send_keys(lng)

    ## don't click the "center to view" button since it changes the lat and lng slightly
    # cnt_button = driver.find_element_by_class_name('btn-small')
    # cnt_button.click()

    gen_button = driver.find_element_by_id('genButton')
    gen_button.click()

    time.sleep(4)

    dwn_button = driver.find_element_by_id('downloadbtn')
    dwn_button.click()

    time.sleep(15)

    list_of_zips = glob.glob("C:/Users/chris/Downloads/*")
    latest_zip = max(list_of_zips, key=os.path.getctime)
    with zipfile.ZipFile(latest_zip, 'r') as zip_ref:
        zip_ref.extractall("C:/Users/chris/OneDrive/Documents/Terrain")

    list_of_files = glob.glob("C:/Users/chris/OneDrive/Documents/Terrain/stls/*")
    latest_file = max(list_of_files, key=os.path.getctime)

    if int(lat) > 0:
        lat_coord = "N"
        lat_text = lat
    else:
        lat_coord = "S"
        lat_text = str(int(lat) * -1)

    if int(lng) > 0:
        lng_coord = "E"
        lng_text = lng
    else:
        lng_coord = "W"
        lng_text = str(int(lng) * -1)

    os.rename(latest_file, "C:/Users/chris/OneDrive/Documents/Terrain/stls/%s%s_%s%s.stl" % (
    lat_coord, lat_text, lng_coord, lng_text))


driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver.exe') # Using Chrome to access web
driver.get('http://jthatch.com/Terrain2STL/')  # Open the website

model_link = driver.find_element_by_link_text('Model Details')
model_link.click()
complete = input("Press any key when setup complete.")
location_link = driver.find_element_by_link_text('Location')
location_link.click()
time.sleep(2)

lat = 49
#lng = '-112'

for lat in range(49, 32, -1):
    for lng in range(-125, -103, 1):
        download(lat, lng)
        time.sleep(1)

# Blender Portion Below ----------------------------------------------------------------------------------------------

# import bpy
# from bpy.app.handlers import persistent
#
# lat = 0
# lng = 0
#
#
# @persistent
# def load_handler(dummy):
#     bpy.ops.wm.save_as_mainfile(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Blender\\Python_test4.blend")
#
#
# bpy.ops.import_mesh.stl(
#     filepath="C:\\Users\\chris\\OneDrive\\Documents\\Terrain\\stls\\N" + str(lat) + "_W" + str(lng) + ".stl")
# bpy.context.object.dimensions = [50, 65, 1]
# bpy.context.object.scale[2] = 0.14
#
# # Join the two objects
# # ---------------------------------------------------
# scene = bpy.context.scene
# obs = []
# for ob in scene.objects:
#     # whatever objects you want to join...
#     if ob.type == 'MESH':
#         obs.append(ob)
# ctx = bpy.context.copy()
# # one of the objects to join
# ctx['active_object'] = obs[1]
# ctx['selected_editable_objects'] = obs
#
# bpy.ops.object.join(ctx)
# # ---------------------------------------------------
#
# bpy.ops.export_mesh.stl(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Terrain\\Complete\\" + ob.name + ".stl")
#
# bpy.app.handlers.load_post.append(load_handler)
#
# for latitude in range(49, 32, -1):
#     for longitude in range(-125, -103, 1):
#         lat = abs(latitude)
#         lng = abs(longitude)
#         bpy.ops.wm.open_mainfile(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Blender\\Puzzle_Master.blend")
#         print("Finished: " + str(lat) + " " + str(lng))




