def Sum(a,b):
    return a+b

def DotProduct(v1, v2):
    if(len(v1) != len(v2)):
        raise ValueError("Vectors de diferents mides")
    result = []
    for i in range(len(v1)):
        result.append(v1[i]+v2[i])
    return result


def MatrixSum(m1, m2):
    if (len(m1) != len(m2) or len(m1[0])!=len(m2[0])):
        raise ValueError("Matrius de dimensions diferents")
    temp_row = []
    result = []
    for i in range(len(m1)):
        for j in range(len(m1[i]):
            temp_row.append(m1[i,j]+m2[i,j])
        result.append(temp_row)
        temp_row=[]
    return result

def MatrixMult(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("Matrices of incompatible dimensions for multiplication.")
    
    result = []
    for i in range(len(m1)):  
        temp_row = []  
        
        for j in range(len(m2[0])):  
            pos_val = 0  
            for k in range(len(m2)):  
                pos_val += m1[i][k] * m2[k][j]
            
            temp_row.append(pos_val)  
        
        result.append(temp_row)  
    
    return result   
        
