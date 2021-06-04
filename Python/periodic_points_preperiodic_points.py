def _all_periodic_points_(self, periods):
    DS = copy(self)
    # first find there is numbers that's dividible by another numbers
    # and keep the max between them
    # Example : periods = (3,5,15) => lst = (15)
    lst = []
    periods = sorted(periods)
    for i in range(0, len(periods)):
        # put all the numbers that are divisible by periods[i]
        f = list(
            reversed(list(filter(lambda x: (x % periods[i] == 0), periods))))
        lst.append(f[0])  # keep the maximum
        lst = list(sorted((set(lst))))
    # now for every period find the periodic points and add them to the list
    periodic_points_lst = []
    for period in lst:
        periodic_points_lst += DS.periodic_points(period, minimal=True)
        # 'minimal = True' because we removed the period = 1
    return list(set(periodic_points_lst))

# edit to all_rational_preimages


def all_rational_preimages(self, points):
    from sage.rings.function_field.function_field import RationalFunctionField_global
    if not isinstance(self.base_ring(), RationalFunctionField_global) and self.domain().base_ring() not in NumberFields():
        raise TypeError("field won't return finite list of elements")
    if not isinstance(points, (list, tuple)):
        points = [points]
    preperiodic = set()
    while points != []:
        P = points.pop()
        preimages = self.rational_preimages(P)
        for i in range(len(preimages)):
            if not preimages[i] in preperiodic:
                points.append(preimages[i])
                preperiodic.add(preimages[i])
    return list(preperiodic)


def _all_preperiodic_points_(self, periodic_points):
    DS = copy(self)
    preperiodic_points_lst = []
    for p in periodic_points:
        # for every periodic point find its rational preperiodic points
        preperiodic_points_lst += DS.all_rational_preimages(p)
    return sorted(list(set(preperiodic_points_lst)))
