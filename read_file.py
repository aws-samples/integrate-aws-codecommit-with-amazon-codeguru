def read_lines(file):
    lines = []
    f = open(file, ‘r’)
    for line in f:
        lines.append(line.strip(‘\n’).strip(‘\r\n’))
    return lines