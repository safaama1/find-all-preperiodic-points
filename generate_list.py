def generate_list(filename):
    lst_graphs = []
    with open(filename) as file_in:
        for func_str in file_in:
            # converte the string to a mathematical expression
            func_eval = sage_eval(func_str,locals={'x':x , 't':t})
            DS = DynamicalSystem_projective([x^2 + func_eval*y^2 , y^2 ])
            # add to the list the graph of the given dynamical system
            lst_graphs.append(DS.rational_preperiodic_graph(lst,1))
    return lst_graphs
