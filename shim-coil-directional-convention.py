import numpy as np

#class current_direction:
#def _init_(self):
 #   self.coil=[]
  #  self.numcoils=len(self.coil)
def check_and_correct_winding(points):
    coils_to_set_negative=[9,10,12,14,17,27,30,32,33,34,35,
                       43,44,45,46,47,49,24,25,26,
                       41,42,36,37,0,1,5,4,6,8]

    for coil in coils_to_set_negative:
        print("There are %d coils that are positive."%(50-len(coils_to_set_negative)))
        print("There are %d coils that are negative."%(len(coils_to_set_negative)))
        # Winding direction is incorrect; reverse current direction
        origin=np.array([0,0,0]) # points is a list of numpy 3-arrays defining the loop (m)
        for i in range(len(points)):     
            vec_ell_i=points[i]     #vec{l}_i, 'i' is current in (A)    
            vec_ell_f=points[(i + 1) % len(points)]   #vec{l}_l+1
            diff=vec_ell_f-vec_ell_i           #diferrence between the two vectors
            vec_r=vec_ell_i-origin    #any coil point     
            cross_product = np.cross(vec_ell_i, vec_ell_f)
            if np.dot(vec_r, cross_product) <= 0:
                return -1
            
            return 1
            

#Check and correct winding direction (test points of interest)

points = np.array([
    [1, 4, 0],
    [0, 1, 0],
    [-1, 0, 0],
    [0, -1, 0]
])
software_flag = check_and_correct_winding(points)
print("Software flag for current correction:", software_flag)


