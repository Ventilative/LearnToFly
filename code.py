Web VPython 3.2

scene = canvas(width = 900, height = 600)

scene.userzoom = False
scene.userpan = False
scene.userspin = False

radii = 6378137

earth = sphere(pos = vec(0,0,0), radius = radii, color = color.white, texture = textures.earth)
earth.rotate(axis=vec(1,0,0), angle = pi, origin = vec(0,0,0))
scene.camera.pos = vec(77440.8, 6389600, 278902)
scene.camera.axis = vec(1201350, 551637, 5615770)
