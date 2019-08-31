
test_cn_layer = [0, 0, 0]
test_cn_layer[0] = 'Beverages, spirits,'
test_cn_layer[1] = 'spirits liqueurs other,spirits,beverages'
test_cn_layer[2] = 'Other other other spirits,distilling,potatoes'

test_us_layer = [0]*6
for i in range(6):
    test_us_layer[i] = [0]*2
    test_us_layer[i][0] = 'Beverages, spirits,'
    test_us_layer[i][1] = 'spirits liqueurs other,spirits,beverages'


test_us_layer[0].append('other,other,other,spirit')
test_us_layer[1].append('spirit,distill,grape,wine,pisco,singani')
test_us_layer[2].append('liqueur,cordial')
test_us_layer[3].append('gin,geneve')

test_us_layer[4].append('other,other,spirit,mezcal,container')
test_us_layer[5].append('other,imitation,brandy,other,spirit,beverage')


