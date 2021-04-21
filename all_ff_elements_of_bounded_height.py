def degree(f):
     return max(f.denominator().degree() , f.numerator().degree());

def all_ff_elements_of_bounded_height(F,b):
    KF = F.constant_field()
    elements_set = set();
    if(b==0):
        return [F(el) for el in list(KF)]
    else:
        P = ProjectiveSpace((b*2)+1,KF)
        l = list(P.rational_points())
        n = len(l[0])
        for i in l:
            w1 =(list(i)[0:n/2])
            w2 =(list(i)[n/2:n])
            P = F(1).numerator().parent()
            if(P(w2) != 0 and degree(P(w1)/P(w2)) <= b):
                elements_set.add(F(P(w1)/P(w2)))
    return(list(elements_set))


K = GF(3)
FF.<t> = FunctionField(K)

lst6 = all_ff_elements_of_bounded_height(FF,6) # 10 min
lst7 = all_ff_elements_of_bounded_height(FF,7) # 1 hr 36 min
lst8 = all_ff_elements_of_bounded_height(FF,8) # ?
lst9 = all_ff_elements_of_bounded_height(FF,9) # ?
lst10 = all_ff_elements_of_bounded_height(FF,10) # ?

with open('height-6.txt', 'w') as f:
    f.writelines("%s\n" % str(func) for func in lst6)

with open('height-7.txt', 'w') as f:
    f.writelines("%s\n" % str(func) for func in lst7)

with open('height-8.txt', 'w') as f:
    f.writelines("%s\n" % str(func) for func in lst8)

with open('height-9.txt', 'w') as f:
    f.writelines("%s\n" % str(func) for func in lst9)

with open('height-9.txt', 'w') as f:
    f.writelines("%s\n" % str(func) for func in lst10)

%%time
count = 0
with open("height-6.txt") as file_in:
    for func_str in file_in:
        func_eval = sage_eval(func_str,locals={'x':x , 't':t})
        DS = DynamicalSystem_projective([x^2 + func_eval* y^2,y^2 ])
        show(plot(rational_preperiodic_graph(DS,lst,1),figsize=8,vertex_color = "white",title = func_str,title_pos=(0.5,-0.05),fontsize = 14,graph_border=True))
        count += 1
        if count == 10000 :
            break
file_in.close()
