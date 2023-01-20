


def perform_map():
    line = "1,2020-01-01 00:28:15,2020-01-01 00:33:03,1,1.20,1,N,238,239,14,6,3,0.5,1.47,0,0.3,11.27,2.5"
    line = line.strip()
    words = line.split(sep=',')
    data = str(words[2])[0:7]
    key = str(data) + 'pt:' + str(words[9])
    value = words[13]
    print('%s\t%s' % (key, value))
    line2 = '%s\t%s' % (key, value)
    key2, count2 = line2.split('\t', 1)
    print(key2)
    print(key2[0:7])
    print(key2[10:])
    print(count2)


perform_map()
