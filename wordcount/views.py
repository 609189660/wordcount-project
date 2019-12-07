from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    if len(fulltext)==0:
        return render(request,'home.html')
    else:
        wordlist=fulltext.split()

        dic={}
        for word in wordlist:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
            sorted_dic = sorted(dic.items(), key=lambda kv: kv[1],reverse=True)

        return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'dic':dic,'sorteddic':sorted_dic})

def about(request):
    return render(request,'about.html')