import numpy as np

def mask_and_classify_scores(arr):
    
    if type(arr) is not np.ndarray:
        return None
    
    if arr.ndim !=2:
        return None
    n_rows, n_cols = arr.shape
    if n_rows != n_cols:
        return None
    
    if n_rows < 4:
        return None
    
    n = n_rows 
    
    cleaned = arr.copy()  #copy of the original array
    cleaned[cleaned<0] = 0   #all values<0 =0
    cleaned[cleaned>100] = 100  #all values>100 = 100
    
    #classifying scores
    levels = np.zeros_like (cleaned, dtype=int)    
    #create a new array called levels, filled with zeros, with the same shape as cleaned, and with integer values
    
    medium_mask = (cleaned >= 40) & (cleaned < 70)
    levels[medium_mask] = 1
    
    high_mask =( cleaned >=70)
    levels [high_mask] = 2
    # low (<40) remain 0
    
    #counting passing scores per now
    row_pass_counts = np.zeros (n,dtype = int)
    
    for i in range (n):
        count = 0
        for value in cleaned[i]:
            if value >= 50: #passing score
                count += 1
        row_pass_counts[i] = count
        
    return (cleaned, levels, row_pass_counts)
            
    
#%%
#Input rules:
#- arr must be a NumPy array(np.ndarray)
#- arr must be 2-dimensional and square (shape n × n)
#-  n must be at least 4

#If any of these rules are not satisfied,the function should return None
#%%
#Part B; classifying scores
#Based on cleaned, create another array with the same shape, called levels.
#Each entry in levels is an integer that encodes the “level” of the score:
#- 0 for “low” scores       (< 40)
#- 1 for “medium” scores    (40 ≤ value < 70)
#- 2 for “high” scores      (value ≥ 70)
#levels will be the second element of the return value.

