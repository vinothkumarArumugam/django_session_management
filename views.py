from django.shortcuts import render
   # def cookiescount_view(request):

      #  count=request.COOKIES.get('count',0)
      # total_count=int(count)+1                                                         ##### these commented function is for cookies creation to count number of cookies
    
      #response=render(request,'cookiesapp/cookies.html',{'count':total_count})
      #response.set_cookie("count",total_count)
      #return response
def session_view(request):
    count=request.session.get("count",0)  ----# these are for getting session information(here count of session id) here 'count' is key value ,it store in as key value pair (dict) as string   
                                             -----  # ('count',o) here 0 is for returning 0 if key has no value in it (default value)
    total_count=int(count)+1                 ---# so to convert str to int and adding one to this
    request.session['count']=total_count        ----# setting this key value as total_count value
    return render(request,'cookiesapp/cookies.html',{'count':total_count}) -----# then rendering this to html file
