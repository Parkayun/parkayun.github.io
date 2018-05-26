from os import system


if __name__ == '__main__':
    system('hugo')
    system('cp public/index.html ./')
    with open('./public/index.html', 'r') as o:
        with open('./index.html', 'r+') as n:
            n.seek(0)
            n.write(o.read().replace('href="https://parkayun.kr/public/"', 'href="https://parkayun.kr/"'))
            n.truncate()

