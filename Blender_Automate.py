import bpy
from bpy.app.handlers import persistent

lat = 0
lng = 0

@persistent
def load_handler(dummy):
	bpy.ops.wm.save_as_mainfile(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Blender\\Python_test4.blend")
    bpy.ops.import_mesh.stl(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Terrain\\stls\\N" + str(lat) + "_W" + str(lng) + ".stl")
    bpy.context.object.dimensions = [50, 65, 1]
    bpy.context.object.scale[2] = 0.14
	
	# Join the two objects
	#---------------------------------------------------
	scene = bpy.context.scene
	obs = []
	for ob in scene.objects:
		# whatever objects you want to join...
		if ob.type == 'MESH':
			obs.append(ob)
	ctx = bpy.context.copy()
	# one of the objects to join
	ctx['active_object'] = obs[1]
	ctx['selected_editable_objects'] = obs

	bpy.ops.object.join(ctx)
	#---------------------------------------------------
	
	bpy.ops.export_mesh.stl(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Terrain\\Complete\\" + ob.name + ".stl")
	
		
    
bpy.app.handlers.load_post.append(load_handler)


for latitude in range(49, 32, -1):
    for longitude in range(-125, -103, 1):
        lat = abs(latitude)
        lng = abs(longitude)
        bpy.ops.wm.open_mainfile(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Blender\\Puzzle_Master.blend")
        print("Finished: " + str(lat) + " " + str(lng))
