import os

ls = []
for rt, dr, fl in os.walk('.'):
    for d in dr:
        tf = os.path.join(rt, d)
        tfs = tf.strip('.\\')
        if (rt == '.'
                and '.git' not in tf
                and '__pycache__' not in tf
                and 'venv' not in tf
                and '.idea' not in tf
                and '.other' not in tf):
            ls.append(tf)
        elif (rt == '.'
                and '~TEMP.' in tf):
            ls.append(tf)

rls = []
for i in ls:
    if i[2] == '[':
        print(f'不上传的 | {i}')
        rls.append(i)
    elif not bool(os.listdir(i)):
        print(f'空文件夹 | {i}')
        rls.append(i)
    elif '~TEMP' in i:
        print(f'临时存放 | {i}')
        rls.append(i)
else:
    del ls
    print()

if not bool(input('已缓存，导出？回车为是，n为否：')):
    if not bool(input('追加至.gitignore？回车为是，n为否：')):
        with open('.gitignore', 'w+') as f:
            _tmp = set(f.readlines())
            _rls = set(rls)
            tmp = list(_tmp | _rls)
            f.write('\\[*\\]*\n')
            f.write('*.cmd\n.idea\n*.ini\n~*({*})\n.gitignore\n\n')
            for t in tmp:
                if '[' in t:
                    f.write(f'{t[1:-1]}\\]' + '\n')
                else:
                    f.write(t.strip('.\\') + '\n')
            else:
                del _tmp, _rls, tmp, f
