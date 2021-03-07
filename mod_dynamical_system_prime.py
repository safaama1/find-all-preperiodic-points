# Function the returns the dynamical system mod p ( ds mod p )
def mod(self,p):
    DS = copy(self)
    DS.normalize_coordinates()  # normalize coordinates of dynamical system
    df_p_all = DS.defining_polynomials()
    coefficients = []
    for i in range(0,len(df_p_all)):
        coefficients.append(df_p_all[i].coefficients())
    monomials = []
    for i in range(0,len(df_p_all)):
        monomials.append(df_p_all[i].monomials())
    F = DS.base_ring() # obtain base_ring of dynamical system
    O = F.maximal_order()
    p = O.ideal(p).place()
    k, fr_k, to_k = p.residue_field()
    # reduce each coefficient of each polynomial using the function to_k :
    reduced_coefficients = []
    for i in range(0,len(coefficients)):
        reduced_coefficients.append([to_k(c) for c in coefficients[i]])
    # change the ring of each monomial to the residue field :
    new_monomials = []
    for i in range(0,len(monomials)):
        new_monomials.append([m.change_ring(k) for m in monomials[i]])
    new_pol = []
    polynom = 0
    for i in range(0,len(reduced_coefficients)):
        for j in range(0,len(reduced_coefficients[i])):
            polynom += reduced_coefficients[i][j] * new_monomials[i][j]
        new_pol.append(polynom)
        polynom = 0
    # construct a new dynamical system from the polynomials
    new_DS = DynamicalSystem(new_pol)
    return new_DS
