def rational_preperiodic_graph(self,primes,e):
    DS = copy(self)
    periods = DS.all_possible_global_periods(primes,e)
    periodic_points_ = DS.all_periodic_points(periods)
    preperiodic_points_ = DS.all_preperiodic_points(periodic_points_)
    g1 = DS._preperiodic_points_to_cyclegraph(preperiodic_point_)
    # number every vertice on the graph
    g2 = g1.canonical_label()
    g3 = g2.copy(immutable=True)
    return g3
