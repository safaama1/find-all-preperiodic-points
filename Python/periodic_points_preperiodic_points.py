def _all_periodic_points_(self,periods):
    DS = copy(self)
    # first find there is numbers that's dividible by another numbers
    # and keep the max between them
    # Example : periods = (3,5,15) => lst = (15)
    lst = []
    periods  = sorted(periods)
    for i in range(0,len(periods)) :
        # put all the numbers that are divisible by periods[i]
        f = list(reversed(list(filter(lambda x: (x % periods[i] == 0),periods))))
        lst.append(f[0]) # keep the maximum
        lst = list(sorted((set(lst))))
    # now for every period find the periodic points and add them to the list
    periodic_points_lst = []
    for period in lst :
        periodic_points_lst += DS.periodic_points(period ,minimal = True)
        # 'minimal = True' because we removed the period = 1
    return list(set(periodic_points_lst))

def _all_preperiodic_points_(self, periodic_points):
    DS = copy(self)
    preperiodic_points_lst = []
    for p in periodic_points:
        # for every periodic point find its rational preperiodic points
        preperiodic_points_lst += DS.all_rational_preimages(p)
    return sorted(list(set(preperiodic_points_lst)))
