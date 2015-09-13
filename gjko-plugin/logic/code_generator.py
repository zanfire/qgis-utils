"""

ctess ratio             construction age               
 <0.3    1       <=1945  A          
0.3-0.4    2       1946-1960   B          
0.4-0.5   3       1961-1980   C          
0.5-0.6  4       1981-1990   D          
0.6-0.7     5       1991-2005   E          
0.7-0.8    6       >=2006  F          
0.8     7                      

For residential buildings                           
<0.3    0.3-0.4     0.4-0.5     0.5-0.6     0.6-0.7     0.7-0.8     >=0.8
<=1945     E1-A.1  E1-A.2  E1-A.3  E1-A.4  E1-A.5  E1-A.6  E1-A.7
1946-1960     E1-B.1  E1-B.2  E1-B.3  E1-B.4  E1-B.5  E1-B.6  E1-B.7
1961-1980    E1-C.1  E1-C.2  E1-C.3  E1-C.4  E1-C.5  E1-C.6  E1-C.7
1981-1990   E1-D.1  E1-D.2  E1-D.3  E1-D.4  E1-D.5  E1-D.6  E1-D.7
1991-2005  E1-E.1  E1-E.2  E1-E.3  E1-E.4  E1-E.5  E1-E.6  E1-E.7
>=2006    E1-F.1  E1-F.2  E1-F.3  E1-F.4  E1-F.5  E1-F.6  E1-F.7

For non residential buildings                           
<0.3    0.3-0.4     0.4-0.5     0.5-0.6     0.6-0.7     0.7-0.8     >=0.8
<=1945     En1-A.1     En1-A.2     En1-A.3     En1-A.4     En1-A.5     En1-A.6     En1-A.7
1946-1960     En1-B.1     En1-B.2     En1-B.3     En1-B.4     En1-B.5     En1-B.6     En1-B.7
1961-1980    En1-C.1     En1-C.2     En1-C.3     En1-C.4     En1-C.5     En1-C.6     En1-C.7
1981-1990   En1-D.1     En1-D.2     En1-D.3     En1-D.4     En1-D.5     En1-D.6     En1-D.7
1991-2005  En1-E.1     En1-E.2     En1-E.3     En1-E.4     En1-E.5     En1-E.6     En1-E.7
>=2006    En1-F.1     En1-F.2     En1-F.3     En1-F.4     En1-F.5     En1-F.6     En1-F.7""
"""

def get_code(prefix, epoch_str, sv):
    construction_age = ''
    # convert epoch str in first value
    epoch = 1900
    if epoch_str.startswith('<=') or epoch_str.startswith('>='):
        epoch = int(epoch_str[2:4])
    else:
        epoch = int(epoch_str[:4])

    if epoch <= 1945: construction_age = 'A'          
    elif epoch in range(1946, 1960): construction_age = 'B'          
    elif epoch in range(1961, 1980): construction_age = 'C'          
    elif epoch in range(1981, 1990): construction_age = 'D'          
    elif epoch in range(1991, 2005): construction_age = 'E' 
    else: construction_age = 'F' 
    
    compactness = ''
    if sv <= 0.3: compactness = '1'
    elif sv > 0.3 and sv <= 0.4: compactness = '2'
    elif sv > 0.4 and sv <= 0.5: compactness = '3'
    elif sv > 0.5 and sv <= 0.6: compactness = '4'
    elif sv > 0.6 and sv <= 0.7: compactness = '5'
    elif sv > 0.7 and sv <= 0.8: compactness = '6'
    else: compactness = '7'
    return prefix + '-' + construction_age + '.' + compactness 


def get_code_for_residential_building(epoch, sv):
    return get_code('E1', epoch, sv)


def get_code_for_non_residential_building(epoch, sv):
    return get_code('En1', epoch, sv)

