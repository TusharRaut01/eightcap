ht=int(input('height of tank'))
lt=int(input('length of tank'))
bt=int(input('breadth of tank'))
hg=int(input('height of glass'))
rg=int(input('radius of glass'))
volume_of_tank=(ht*lt*bt)
volume_of_glass=(2*3.14*rg*hg)
no_of_glass=(volume_of_tank/volume_of_glass)
print("No of glass is :_", no_of_glass)