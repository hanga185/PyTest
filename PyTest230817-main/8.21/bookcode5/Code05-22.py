inFp, outFp = None, None
inStr = ""

# ini를 문자열로 읽어서 복사
inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")
