def read_lines(path):
    with open(path) as f:
        content = list()
        while 1:
            try:
                lines = f.readlines(100)
            except UnicodeDecodeError:
                f.close()
                continue
            if not lines:
                break
            for line in lines:
                content.append(line)
    return content