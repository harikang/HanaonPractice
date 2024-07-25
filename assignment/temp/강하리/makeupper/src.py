def convert(line):
    return line.upper()

def reader(src):
    with open(src) as f:
        for line in f:
            yield line

def writer(dest, reader):
    with open(dest, 'w') as f:
        for line in reader:
            f.write(convert(line))