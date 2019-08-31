def find_cn_layer(key, chapter, heading, detail):
    cn_layer = []

    del cn_layer[:]

    for chapter_key in chapter.keys():
        if (chapter_key[0] == key[0]) & (chapter_key[1] == key[1]):
            cn_layer.append(chapter[chapter_key])

    for heading_key, value in heading.items():

        if len(heading_key) == 4:
            if heading_key[0] == key[0]:
                if heading_key[1] == key[1]:
                    if heading_key[2] == key[2]:
                        if heading_key[3] == key[3]:
                            cn_layer.append(value)

    for detail_key in detail.keys():
        if detail_key == key:
            cn_layer.append(detail[detail_key])
    while len(cn_layer) < 3:
        cn_layer.append('')

    return cn_layer
