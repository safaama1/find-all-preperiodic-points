def rational_preperiodic_graph(self,primes,e):
    DS = copy(self)
    periods = DS.all_possible_global_periods(primes,e)
    periodic_points_ = DS._all_periodic_points_(periods)
    preperiodic_points_ = DS._all_preperiodic_points_(periodic_points_)
    g1 = DS._preperiodic_points_to_cyclegraph(preperiodic_points_)
    # number every vertice on the graph
    g2 = g1.canonical_label()
    g3 = g2.copy(immutable=True)
    return g3
