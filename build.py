from os import system
from subprocess import check_output


if __name__ == '__main__':
    system('hugo')
    system('cp public/index.html ./')
    with open('./public/index.html', 'r') as o:
        with open('./index.html', 'r+') as n:
            n.seek(0)
            n.write(o.read().replace('href="https://parkayun.kr/public/"', 'href="https://parkayun.kr/"'))
            n.truncate()
    system('git add .')
    message = input('commit message: ')
    system('git commit -m "%s"' % message)
    git_hash = check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    files = check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', git_hash]).decode().split()
    system('git checkout master')
    for f in files:
        if f.startswith('public/'):
            print(f)
            system('git checkout %s %s' % (git_hash, f))
    system('git commit -m "%s"' % message) 
    system('git push --all origin')
    system('git checkout real-master')
