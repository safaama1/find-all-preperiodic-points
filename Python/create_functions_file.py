def degree(f):
     return max(f.denominator().degree() , f.numerator().degree());

def create_functions_file(FF,b):
    """
    Creat a file that contains functions over finite fields with height <= b
    
    Input :
    - FF: Finite field
    - b: The height
    
    Output:
    file that contains functions over finite fields with height <= b
    
    """
    K = GF(3)
    F.<t> = FunctionField(K)
    KF = F.constant_field()
    elements_set = set();
    if(b==0):
        return [F(el) for el in list(KF)]
    else:
        P = ProjectiveSpace((b*2)+1,KF)
        l = list(P.rational_points())
        n = len(l[0])
        for i in l:
            w1 =(list(i)[0:n/2])
            w2 =(list(i)[n/2:n])
            P = F(1).numerator().parent()
            if(P(w2) != 0 and degree(P(w1)/P(w2)) <= b):
                elements_set.add(F(P(w1)/P(w2)))
    elements_list = list(elements_set)                
    with open('height-' + str(b) + '.txt', 'w') as f:
        f.writelines("%s\n" % str(func) for func in elements_list)
    

# The files we will use 
# the finite field contains 3 numbers 

create_functions_file(3,6) # Time complexity = 10 min
create_functions_file(3,7) # Time complexity = 1 hr 36 min
create_functions_file(3,8) # Time complexity = ?
create_functions_file(3,9) # Time complexity = ?
create_functions_file(3,10) # Time complexity = ?
