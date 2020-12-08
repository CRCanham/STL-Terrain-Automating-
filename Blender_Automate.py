import bpy
from bpy.app.handlers import persistent

lat = 0
lng = 0

@persistent
def load_handler(dummy):
	bpy.ops.wm.save_as_mainfile(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Blender\\Python_test4.blend")
    	bpy.ops.import_mesh.stl(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Terrain\\stls\\N" + str(lat) + "_W" + str(lng) + ".stl")
    	bpy.context.object.dimensions = [50, 65, 1]
    	bpy.context.object.scale[2] = 0.18
	
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
	
	# Add Embossed Text
	#---------------------------------------------------
	bpy.ops.object.text_add(enter_editmode=False, location=(25, -8, -5))
	bpy.context.object.scale = 6, 6, 6
	bpy.context.object.rotation_euler[1] = math.pi


	bpy.ops.object.editmode_toggle()
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.text_insert(text="N"+str(lat)+"\nW"+str(lng))
	bpy.ops.object.editmode_toggle()

	bpy.context.object.data.extrude = 0.4
	bpy.ops.object.convert(target='MESH')

	scene = bpy.context.scene
	obs = []
	for ob in scene.objects:
		if ob.type == 'MESH':
			obs.append(ob)

	bpy.context.view_layer.objects.active = obs[0]
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
	bpy.context.view_layer.objects.active = obs[1]
	bpy.ops.object.delete(use_global=False, confirm=False)
	#---------------------------------------------------
	
	bpy.ops.export_mesh.stl(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Terrain\\Colorado\\" +"N"+str(lat)+"_W"+str(lng) + ".stl")
	
		
    
bpy.app.handlers.load_post.append(load_handler)


for latitude in range(49, 32, -1):
    for longitude in range(-125, -103, 1):
        lat = abs(latitude)
        lng = abs(longitude)
        bpy.ops.wm.open_mainfile(filepath="C:\\Users\\chris\\OneDrive\\Documents\\Blender\\Puzzle_Master.blend")
        print("Finished: " + str(lat) + " " + str(lng))
