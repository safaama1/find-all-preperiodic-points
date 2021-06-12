def all_possible_global_periods(self, primes, e):
    DS = copy(self)
    base = DS.base_ring()
    CF = base.constant_field()
    D = DS.domain()
    # check if the dimension is equal to 1
    if DS.domain().dimension() != 1:
        raise NotImplementedError("The dimension must be 1")
    # check if the field is function field over Finite Field
    from sage.rings.function_field.function_field import RationalFunctionField_global
    if not isinstance(DS.base_ring(), RationalFunctionField_global) or CF.order() == Infinity:
        raise TypeError("The field must be function field over finite Field ")
    all_possible_global_periods_list = []
    temp_g = 0
    sub_list = []
    for prime in primes:
        # check if the prime is a prime of good reduction
        if DS.is_prime_of_good_reduction(prime):
            sub_list = []
            temp_g += 1  # just to know what is the first list
            new_DS = DS.mod(prime)
            new_base = new_DS.base_ring()
            all_periodic_points = new_DS.all_periodic_points()
            for periodic_point in all_periodic_points:
                # check if this isn't the infinity point
                period = new_DS.orbit_structure(periodic_point)[
                    1]  # period of the periodic point
                multiplier_ = new_DS.multiplier(periodic_point, period)
                # first add the period of the point
                sub_list.append(period)
                if multiplier_[0][0] != 0:
                    # calculate the multiplicative order of the multiplier
                    a = CF(multiplier_[0][0])
                    m_o = a.multiplicative_order()
                    # calculate the characteristic (p) of the new dynamical system
                    characteristic = new_base.characteristic()
                    #  Compute mrVp^e for the cycle (period)
                    for temp_e in range(0, e+1):
                        sub_list.append(
                            period * m_o * (characteristic**temp_e))
            if temp_g == 1:
                # just to avoid making intersection
                # between the first possible periods list and the empty list (the start of the list )
                all_possible_global_periods_list = list(sub_list)
            elif temp_g > 1:
                # find the intersection between the list of the mrp^e (Proposition 2 in the article of Hutz algorithm )
                # and the main list possible global periods list
                all_possible_global_periods_list = list(
                    set(all_possible_global_periods_list) & set(sub_list))
    return sorted(all_possible_global_periods_list)
