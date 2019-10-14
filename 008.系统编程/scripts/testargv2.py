#!python3
# testargv2.py - 将传入的命令行参数保存在词典中


def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv
    myargvs = getopts(argv)
    if '-i' in myargvs:
        print(myargvs['-i'])
    print(myargvs)

