import colour
import numpy as np
import matplotlib.pyplot as plt
import colour.plotting as cpl
 


def calc_error_sRGB(sRGB):
#    l_RGB = np.matrix( ((sRGB/255+0.055)/1.055)**2.4)
    l_RGB = np.matrix( ((sRGB/255))**2.2)
#    l_RGB = np.matrix ((sRGB/255) )

    s_rgb_2_xyz = np.matrix([[0.4124 , 0.3576 , 0.1805],
    [0.2126 , 0.7152 , 0.0722],
    [0.0193 , 0.1192 , 0.9505]])

    XYZ = np.dot(s_rgb_2_xyz , l_RGB) 

    sum_xyz = []
    xy_x = []
    xy_y = []
    for i_x in range(3):
        for i_y in range(3):
            for i_z in range(3):
                X = (XYZ[0,i_x])
                Y = (XYZ[1,i_y])
                Z = (XYZ[2,i_z])
                sum_xyz.append(X+Y+Z)
                xy_x.append(X/(X+Y+Z))
                xy_y.append(Y/(X+Y+Z))
    
    print("X+Y+Z :ave:" , np.average(sum_xyz) , " error:" , (np.max(sum_xyz)-np.min(sum_xyz))/np.min(sum_xyz)*100.0)
    #print("X+Y+Z :ave:" , np.average(sum_xyz) , " error:" , np.std(sum_xyz)*100.0)

    #print("x: ave:" , np.average(xy_x) , " error:" , np.std(xy_x))
    #print("y: ave:" , np.average(xy_y) , " error:" , np.std(xy_y))
    print("x: ave:" , np.average(xy_x) , " error:" , (np.max(xy_x)-np.min(xy_x))/np.min(xy_x)*100.0)
    print("y: ave:" , np.average(xy_y) , " error:" , (np.max(xy_y)-np.min(xy_y))/np.min(xy_y)*100.0)
    return (xy_x,xy_y)



def calc_error_sRGB_set(sRGB):
#    l_RGB = np.matrix( ((sRGB/255+0.055)/1.055)**2.4)
#    l_RGB = np.matrix( ((sRGB/255))**2.2)
    l_RGB = np.matrix ((sRGB/255) )
    
    s_rgb_2_xyz = np.matrix([[0.4124 , 0.3576 , 0.1805],
    [0.2126 , 0.7152 , 0.0722],
    [0.0193 , 0.1192 , 0.9505]])

    XYZ = np.dot(s_rgb_2_xyz , l_RGB) 

    sum_xyz = []
    xy_x = []
    xy_y = []
    ans = []
    for i_x in range(3):
                X = (XYZ[0,i_x])
                Y = (XYZ[1,i_x])
                Z = (XYZ[2,i_x])
                sum_xyz.append(X+Y+Z)
                xy_x.append(X/(X+Y+Z))
                xy_y.append(Y/(X+Y+Z))


    
    print("X+Y+Z :ave:" , np.average(sum_xyz) , " error:" , (np.max(sum_xyz)-np.min(sum_xyz))/np.min(sum_xyz)*100.0)
    #print("x: ave:" , np.average(xy_x) , " error:" , np.std(xy_x))
    #print("y: ave:" , np.average(xy_y) , " error:" , np.std(xy_y))
    print("x: ave:" , np.average(xy_x) , " error:" , (np.max(xy_x)-np.min(xy_x))/np.min(xy_x)*100.0)
    print("y: ave:" , np.average(xy_y) , " error:" , (np.max(xy_y)-np.min(xy_y))/np.min(xy_y)*100.0)

    return (xy_x,xy_y)


dataset = {}

dataset["helmet"] = np.array([[229,239,249] , [230,240,250], [224,234,244] ])
dataset["steering"] = np.array([[231,241,251] , [229,239,249], [231,241,254] ])
dataset["Hair"] = np.array([[35,45,55] , [36,46,57], [37,47,57] ])
dataset["Skin"] = np.array([[72,108,182] , [33,95,165], [0,72,142] ])
dataset["Trousers"] = np.array([[0,0,20] , [90,110,130], [133,153,173] ])
dataset["Rubber Tire"] = np.array([[35,45,55] , [36,46,56], [37,47,57] ])
dataset["Frame"] = np.array([[35,45,55] , [36,46,56], [37,47,57] ])

cpl.plot_chromaticity_diagram_CIE1931(bounding_box=(-0.1, 0.9, -0.1, 0.9), standalone=False)
for key in dataset.keys():
    print(key)
    xy_x , xy_y = calc_error_sRGB(dataset[key])
    #xy_x , xy_y = calc_error_sRGB_set(dataset[key])
    plt.plot(xy_x, xy_y, 'o', markersize=2, label=key)


plt.legend() 

plt.show()
