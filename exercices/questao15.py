#http://www.protetordelinks.com/link/?url=http://www.megaupload.com/?d=E34ZP1CO
#http://www.loadbr.info/link/?url=OC1PZ43E=d?/moc.daolpuagem.www//:ptth
def start(adress):
    for n, url in enumerate(adress, start=1):
        if url == "=":
            return n

def local(x):
    if x[0:4] == "http":
        return x 
    else:
        return x[::-1]


link = "http://www.loadbr.info/link/?url=OC1PZ43E=d?/moc.malulu.www//:ptth"
original = link[start(link):]
print(local(original))
