import sys


def getreply():
    if sys.stdin.isatty():  # 如果 stdin 是控制台，从stdin读取数据
        return input('?:')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch('?')
            key = msvcrt.getche()   # 获取键盘输入
            msvcrt.putch('\n')
            return key
        else:
            assert False, 'platform not supported'


def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getreply() not in ['y', 'Y']:
            break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1], 'rb').read())


