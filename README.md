# STL-Terrain-Automating-

Project goal is to automate the process of turning geographical topo data into stls which can be 3D printed. 

Main.py downloads stls from http://jthatch.com/Terrain2STL/ which are rectangles 1 degree latiitude by 1 degree longitude. User can specify exactly which regison on the erath to extract files from. In this example I'm using all the western United Staes. Files are then unzipped and saved to a single file location containing all terrain files.

Blender_Automate.py is designed to be used within Blender using the Blender API. Blender is used to set the size and height exageration for 3D printing purposes. Blender is also used to join terrain piece with a puzzle piece base which enables users to create a 3D puzzle of any geographical terrain on Earth. The automation loops through for all stls downloaded in Main.py to eliminate any manual repetitive tasks. 
