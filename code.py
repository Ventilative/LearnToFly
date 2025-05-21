Web VPython 3.2

scene = canvas(width = 900, height = 600, resizable = False, autoscale = True)
scene.camera.pos = vec(0, 0, 500)
#scene.userzoom = False
scene.userpan = False
#scene.userspin = False

earth = sphere(pos = vec(0,0,0), radius = 500, color = color.white, texture = textures.earth)
print(scene.camera.pos)
def chonky(evt):
        console.log(evt)
        print(scene.camera.pos)
        if evt.id is 'rad':
                earth.radius = evt.value

xslider = slider(bind=chonky, max=6000, min=500, step=0.1, value=earth.radius, id='rad')
