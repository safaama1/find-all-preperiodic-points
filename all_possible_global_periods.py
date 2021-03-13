def all_possible_global_periods(self,primes,e  ):
    DS = copy(self)
    base = DS.base_ring()
    CF = base.constant_field()
    D = DS.domain()
    # Check if the dimension is equal to 1
    if DS.domain().dimension() != 1 :
        raise NotImplementedError("The dimension must be 1")
    # Check if the field is function field over Finite Field
    if not isinstance(DS.base_ring(), sage.rings.function_field.function_field.RationalFunctionField_global) or CF.order() == Infinity :
        raise TypeError("The field must be function field over finite Field ")
    all_possible_global_periods_list = []
    temp_g = 0
    for prime in primes :
        # check if the prime is a prime of good reduction
        if is_prime_of_good_reduction(DS,prime) :
            new_DS = mod(DS,prime)
            all_periodic_points = new_DS.all_periodic_points()
            for periodic_point in all_periodic_points:
                # check if this isn't the Infinity point
                if periodic_point != D(1 , 0) :
                    temp_g += 1 # just to know what is the first list
                    period = new_DS.orbit_structure(periodic_point)[1] # period of the periodic point
                    multiplier_ = new_DS.multiplier(periodic_point,period)
                    sub_list = []
                    # first add the period of the point
                    sub_list.append(period)
                    # first add the period of ( 1:0 )
                    sub_list.append(1)
                    if multiplier_[0][0] != 0 :
                        # calculate the multiplicative order of the multiplier
                        a = CF(multiplier_[0][0])
                        m_o = a.multiplicative_order()
                        #  Compute mrVp^e for the cycle (period)
                        for temp_e in range(0,e+1) :
                            sub_list.append(period * m_o * (prime**temp_e) )
                    if temp_g == 1 :
                        # just to avoid making intersection
                        # between the first possible periods list and the empty list (the start of the list )
                        all_possible_global_periods_list = list(sub_list)
                    else :
                        # find the intersection between the list of the mrp^e (Proposition 2 in the article of Hutz algorithm )
                        # and the main list possible global periods list
                        all_possible_global_periods_list = list ( set(all_possible_global_periods_list) & set(sub_list))

    return all_possible_global_periods_list
