import numpy as np

def input_locations(matrix2x2):
    input_matrix = matrix2x2[:,:2]
    types_matrix = (input_matrix/10).astype(int)
    return (types_matrix == 8) | (types_matrix == 9) | (types_matrix == 10)


def unique_init_inputs(matrix2x2):
    input_loc = input_locations(matrix2x2)
    total_unique_inputs = np.any((matrix2x2/10).astype(int) == 8).astype(int) + np.any((matrix2x2/10).astype(int) == 9).astype(int) + np.any((matrix2x2/10).astype(int) == 10).astype(int)
    mask_red = (matrix2x2/10).astype(int) == 8
    mask_green = (matrix2x2/10).astype(int) == 9
    mask_blue = (matrix2x2/10).astype(int) == 10
    return total_unique_inputs, [mask_red,mask_green,mask_blue], [np.any(mask_red),np.any(mask_green),np.any(mask_blue)]



def all_possible_inp_maker(matrix2x2):
    total_inps,_,_ = unique_init_inputs(matrix2x2)  #This was to find the no. of all the inputs which WAS WRONG, Now it's correct...
    arr = np.zeros(total_inps)
    all_bin_list = []
    for i in range(np.power(2,total_inps)):
        bin_string = bin(i)[2:].rjust(total_inps,'0')
        all_bin_list.append([i for i in bin_string])
    return np.array(all_bin_list).astype(int)


def input_value_putter(matrix2x2,vector_to_put):
    unique_inputs, masks, inp_types = unique_init_inputs(matrix2x2)
    new_matrix = np.zeros_like(matrix2x2)
    for i in range(unique_inputs):
        new_matrix[masks[i]] = vector_to_put[i]
    return new_matrix,inp_types 


def output_generator_4_inputs(matrix2x2, binary_vector):
    
    #Where's binary_vector????           Tick
    
#Initial Evaluation directly from inputs    
    
    matrix_4_op,inp_types = input_value_putter(matrix2x2,binary_vector)
    out_mat = matrix_4_op
    input_loc = input_locations(matrix2x2)
    cache = np.zeros_like(input_loc).astype(bool)
#INITIALIZE THE INPUT FOR THE NOT GATES    
    for i,val in np.ndenumerate(matrix2x2[:,2]):
            if int(val/10) == 7:
                if input_loc[i,0] == True:
                    input_loc[i,1] = True        
        

    
    for i in range(matrix_4_op.shape[0]):
        if input_loc[i,0]:
            
        
            if int(matrix2x2[i,2]/10) == 1:
                out_mat[i,2] = out_mat[i,0] and out_mat[i,1]
            elif int(matrix2x2[i,2]/10) == 2:
                out_mat[i,2] = out_mat[i,0] or out_mat[i,1]
            elif int(matrix2x2[i,2]/10) == 3:
                out_mat[i,2] = not(out_mat[i,0] and out_mat[i,1])
            elif int(matrix2x2[i,2]/10) == 4:
                out_mat[i,2] = not(out_mat[i,0] or out_mat[i,1])
            elif int(matrix2x2[i,2]/10) == 5:
                out_mat[i,2] = out_mat[i,0] ^ out_mat[i,1]
            elif int(matrix2x2[i,2]/10) == 6:
                out_mat[i,2] = not(out_mat[i,0] ^ out_mat[i,1])
            elif int(matrix2x2[i,2]/10) == 7:
                out_mat[i,2] = not(out_mat[i,0])
            
        #checking 111, i.e output
        
            #elif int(matrix_4_op[i,2]) == 111:
             #   output = matrix_4_op[i,2]
                
    count = 0
    #print(input_loc,out_mat)
    while True:
        count+=1
#PUT OUTPUT TO NEXT INPUTS
        #inserting the values just calculated, in out_mat to the specefic locations in the two input columns::-- 
        for i,outs in np.ndenumerate(matrix2x2[:,2]):
            if input_loc[i,0] & input_loc[i,1]:
                out_mat[:,:2][matrix2x2[:,:2] == outs] = out_mat[:,2][matrix2x2[:,2] == outs]
 #Check the fucking pairs and initialize the input_loc again
#SIMILARILY, UPDATE THE input_loc BOOL TABLE                                                            
        pairs_loc = input_loc[:,0] & input_loc[:,1]
#Long Term Memory    
        input_loc = np.zeros_like(input_loc).astype(bool) 
        for i in range(cache.shape[0]):
            if (((cache[i,0] ==True) & (cache[i,1]==False))) :#| ((cache[i,0] ==True) & (cache[i,1]==False))):
                input_loc[i,0] = True
            elif (((cache[i,0] ==False) & (cache[i,1]==True))):
                input_loc[i,1] = True
         
        for i,val in np.ndenumerate(pairs_loc):
            if val:
                input_loc[matrix2x2[:,:2] == matrix2x2[i,2]] = True
                
                
#Checks whether the next input is for NOT gate, AND IF IT IS, PUT A TRUE ON IT'S NEXT ROW TOO (I know it's an inefficient implementation!!)    
        for i,val in np.ndenumerate(matrix2x2[:,2]):
            if int(val/10) == 7:
                if input_loc[i,0] == True:
                    input_loc[i,1] = True        

            
#LOOP BREAKING CONDITION            
        #Below Condition is for the breaking from the loop when the corresponding row in which the flow is have output as '111'    
            
        if np.any(matrix2x2[input_loc[:,0] == True][:,2] == 111):
            output = out_mat[:,0][matrix2x2[:,2] == 111]
            break
        
#CALCULATE NEXT OUTPUTS        
        #Now, the new pairs are made (if there's any) and now we need to calculate the new outputs to put in out_mat
        
        for i in range(matrix_4_op.shape[0]):
            if input_loc[i,0] & input_loc[i,1]:

                if int(matrix2x2[i,2]/10) == 1:
                    out_mat[i,2] = out_mat[i,0] and out_mat[i,1]
                elif int(matrix2x2[i,2]/10) == 2:
                    out_mat[i,2] = out_mat[i,0] or out_mat[i,1]
                elif int(matrix2x2[i,2]/10) == 3:
                    out_mat[i,2] = not(out_mat[i,0] and out_mat[i,1])
                elif int(matrix2x2[i,2]/10) == 4:
                    out_mat[i,2] = not(out_mat[i,0] or out_mat[i,1])
                elif int(matrix2x2[i,2]/10) == 5:
                    out_mat[i,2] = out_mat[i,0] ^ out_mat[i,1]
                elif int(matrix2x2[i,2]/10) == 6:
                    out_mat[i,2] = not(out_mat[i,0] ^ out_mat[i,1])
                elif int(matrix2x2[i,2]/10) == 7:
                    out_mat[i,2] = not(out_mat[i,0])
        
        #verb_count+=1
        #print('While Loop number {}'.format(verb_count))
    
        #print(input_loc,out_mat)
        if count==1:
            cache = input_loc
    return output,out_mat,input_loc,inp_types
    
    #After this the input_pair_matrix[:,:2] will be filled by 1's where the pairs are there.    
        
    
    #After this the input_pair_matrix[:,:2] will be filled by 1's where the pairs are there.    
        

def truth_table_generator(matrix2x2):
    binary_vectorS = all_possible_inp_maker(matrix2x2)
    TT = []
    for i in range(binary_vectorS.shape[0]):
        output, _ , _ , inp_types= output_generator_4_inputs(matrix2x2,binary_vectorS[i])
        TT.append([binary_vectorS[i],output])
    print("Outputs:")
    l = []
    for i in range(3):
        if ((inp_types[i] == True) and (i==0)):
            l.append("Red")
        elif ((inp_types[i] == True) and (i==1)):
            l.append("Green")
        elif ((inp_types[i] == True) and (i==2)):
            l.append("Blue")
    print(l)        
    return np.array(TT)