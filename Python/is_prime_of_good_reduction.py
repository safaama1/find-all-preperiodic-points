# %load is_prime_of_good_reduction.py
# Function to check if "prime" is a prime of good reduction
def is_prime_of_good_reduction(self,prime):
    try:
        new_DS = self.mod(prime)
    except ValueError:
        # the mod fucntion mod throws ValueError exception only if
        # the polynomials of the DynamicalSystem doesn't have the same degree which
        # means that this is a prime of bad reduction
        return False
    return True