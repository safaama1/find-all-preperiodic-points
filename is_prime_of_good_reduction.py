# Function to check if "prime" is a prime of good reduction
def is_prime_of_good_reduction(self,prime):
    DS = copy(self)
    degree = DS.degree_sequence(1)[0]
    try:
        new_DS = DS.mod(prime)
    except:
        # the mod fucntion modDS throws exception only if
        # the polynomials of the DynamicalSystem doesn't have the same degree which
        # means that this is a prime of bad reduction
        return False
    # check if the degree of the DynamicalSystem changed.
    # yes -> prime of bad reduction
    # no -> prime of good reduction
    if new_DS.degree_sequence(1)[0] != degree :
        return False
    return True
