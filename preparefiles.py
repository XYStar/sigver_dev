import os

path = '/Users/Star/Code/Python/sigver/sample_Signature/test'
fileList = os.listdir(path)

for item in fileList:
    print(item)
    if item.startswith('00'):
        n = 1
        if item.endswith('forg'):
            targetFolder = path + os.sep + item
            tempStr = item.split('_')[0]
            for file in os.listdir(targetFolder):
                oldname = targetFolder + os.sep + file
                newname = targetFolder + os.sep + tempStr + 'f' + '{:02d}'.format(n) + '.PNG'
                os.rename(oldname, newname)
                n += 1
        else:
            targetFolder = path + os.sep + item
            tempStr = item
            for file in os.listdir(targetFolder):
                oldname = targetFolder + os.sep + file
                newname = targetFolder + os.sep + file.replace('_', 'v')
                os.rename(oldname, newname)
                n += 1
