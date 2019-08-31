
def find_us_layer(key, us_data):
    us_layer = dict({})
    for us_data_key in us_data.keys():
        if len(us_data_key) > 4:
            if us_data_key[0] == key[0]:
                if us_data_key[1] == key[1]:
                    if us_data_key[2] == key[2]:
                        if us_data_key[3] == key[3]:
                            if len(us_data_key) == 10:

                                us_layer[us_data_key] = us_data[us_data_key]

    return us_layer
