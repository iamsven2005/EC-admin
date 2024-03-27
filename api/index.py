#Tan Sven
#221619Q
#IT2653
#6.25.2023 AVLtree, hashmap, insert sort,bubble sort,merge sort ,selection sort,linear search, binary search, quick sort,exponential search, heap sort*2, radix sort, bogo sort, shell sort, Fibonacci Search, introspective sort, tree sort, smooth sort, comb sort
from flask import Flask, redirect, session, redirect
import random
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import timedelta, datetime
import re
import math
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
q = []
like = []
dislike = []
profile = []
requests = []
admin = ["adminpin"]
add = "<br><br><a class="+'"'+"btn"+'"'+" href='/'>Back to homepage</a><script src="+'"'+"https://cdn.tailwindcss.com"+'"'+"></script><link href="+'"'+"https://cdn.jsdelivr.net/npm/daisyui@3.1.7/dist/full.css"+'"'+" rel="+'"'+"stylesheet"+'"'+" type="+'"'+"text/css"+'"'+" /><style>.d{width:1vw;height:1vh;}</style><script>document.addEventListener('contextmenu', event => event.preventDefault());</script><button class="+'"'+"btn btn-outline btn-warning"+'"'+"id="+'"'+"go-back"+'"'+">Go back!</button><script>document.getElementById("+'"'+"go-back"+'"'+").addEventListener("+'"'+"click"+'"'+", () => {history.back();});</script>"
records = [    {'|Year_Published': '1495', '|ISBN (PK)': '1', '|Title': 'Python Cookbook', '|Category': 'Category 1', '|Publisher': 'David Beazley & Brian K. Jones', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=874c56cbc659ea2e7ba8b90cfcd1e316&key=9J9SLSJG3KJ4OEUH"> Download</a>'},
               {'|Year_Published': '1325', '|ISBN (PK)': '2', '|Title': 'Clean Code', '|Category': 'Category 2', '|Publisher': 'Robert C. Martin',  '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=838cc6ac8cb0d8ddb98fdb1ae0c8a443&key=ETKE0Y3YT1EJANIZ"> Download</a>'},
               {'|Year_Published': '1275', '|ISBN (PK)': '3', '|Title': 'The Mythical Man-month', '|Category': 'Category 3', '|Publisher': 'Frederick Brooks', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=9da0a07baa4d3f0107bb6b758b379fcb&key=WE8H4TN67QKCIWMU"> Download</a>'},
               {'|Year_Published': '1379', '|ISBN (PK)': '4', '|Title': 'The Pragmatic Programmer', '|Category': 'Category 2', '|Publisher': 'David Thomas', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=e1654c11f6e10e4daaa84ce8964aae97&key=LL29UF8VSYCKDETJ"> Download</a>'},
               {'|Year_Published': '2189', '|ISBN (PK)': '5', '|Title': 'Code Complete', '|Category': 'Category 1', '|Publisher': 'Steve McConnell', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=bcd3ee51cd1dd56847cf9cc2336294fc&key=9E4DEPPTAHS6XXQO"> Download</a>'},
               {'|Year_Published': '1275', '|ISBN (PK)': '6', '|Title': 'The Art of Computer Programming', '|Category': 'Category 4', '|Publisher': 'Donald E Knuth', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=42a8127fd65a43c18e794bfac431ef2b&key=VPT5QD1779QJJ4IK"> Download</a>'},
               {'|Year_Published': '1435', '|ISBN (PK)': '7', '|Title': 'Programming Pearls', '|Category': 'Category 5', '|Publisher': 'John Bentley', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=7d59f01ea058c2f4d131bbe6b384dc99&key=6WHJPOVEBO0QR3ZN"> Download</a>'},
               {'|Year_Published': '1379', '|ISBN (PK)': '8', '|Title': 'Code', '|Category': 'Category 3', '|Publisher': 'Charles Petzold', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=c06c78607919e1afab8e48d417744d6f&key=8UCLODQ2WSLHZRKS"> Download</a>'},
               {'|Year_Published': '1534', '|ISBN (PK)': '9', '|Title': 'Introduction to Algorithms', '|Category': 'Category 1', '|Publisher': 'T Cormen', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=fd8631d3830bfa7a3d2d305a99a011f2&key=BC1MKSZDVE4K569H"> Download</a>'},
               {'|Year_Published': '1189', '|ISBN (PK)': '10', '|Title': 'Data Structures and Algorithms in C++', '|Category': 'Category 2', '|Publisher': 'Michael T.Goodrich,Roberto Tamassia', '|Submitted_by': 'Admin', '|Download': '<a href="https://libgen.rocks/get.php?md5=9610f5551ab358d6388a606df58be3fa&key=J2APSCK7MLBH2LY6"> Download</a>'}]

ISBN_list = ["1","2","3","4","5","6","7","8","9","10"]
syslog = []
result = "<br><h2>List of books:</h2><br>"
#home
@app.route("/")
def index():
  heapSort(records)
  stl =len(q)/2
  st = str(stl)
  lkl = len(like)
  dlkl = str(len(dislike))
  lk = str(lkl)
  dk = str(dlkl)
  results = str(records)
  result = "<br><h2>List of books:</h2><br>"
  for character in results:
    if character == "[":
      result += "<table class="+'"'+"table hover"+'"'+">"
    elif character == "]":
      result += "</table>"
    elif character == "|":
      result += "<td class="+'"'+"  "+'"'+">"
    elif character == "{":
      result += "<tr class="+'"'+" "+'"'+">"
    elif character == "}":
      result += "</tr>"
    elif character == ",":
      result += " "
    elif character == "'":
      result += " "
    else:
        result += character

  now = str(datetime.now())
  log = "Home: " + now
  syslog.append(log)
  for i in records:
    hashmap = HashMap()
    hashmap.put("zz",i)
  z = hashmap.get("zz")
  zz = str(z)
  resultz = "<br><h2>Newest Added (Using HashMap):</h2><br>"
  for character in zz:
    if character == "[":
      result += "<table class="+'"'+"table hover"+'"'+">"
    elif character == "]":
      result += "</table>"
    elif character == "|":
      result += "<td class="+'"'+"  "+'"'+">"
    elif character == "{":
      result += "<tr class="+'"'+" "+'"'+">"
    elif character == "}":
      result += "</tr>"
    elif character == ",":
      result += " "
    elif character == "'":
      result += " "
    elif character == "-":
      result += "<br>"
    else:
        resultz += character   
  return "<div class="+'"'+"hero min-h-screen bg-base-200"+'"'+"><div class="+'"'+"hero-content"+'"'+"><div class="+'"'+"hero-content text-center"+'"'+"><div class="+'"'+"max-w-md"+'"'+"><h1 class="+'"'+"text-5xl font-bold"+'"'+">Book Management System</h1><p class="+'"'+"py-6"+'"'+">Hello, register with /register/(username) to get started</p><p class="+'"'+"py-6"+'"'+">"+ st  + " users registered</p><p class="+'"'+"py-6"+'"'+">"+ lk  + " <a class="+'"'+""+'"'+"href='/all/like'>liked this website</a><p class="+'"'+"py-6"+'"'+">"+ dk  + " <a class="+'"'+""+'"'+"href='/all/dislike'>disliked this website</a></p><a class="+'"'+"btn btn-primary"+'"'+"href='/register'>Sign Up here!</a></div></div></div></div><br><div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Login</h2><p>Welcome back! Do you still remember your password?</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input id="+'"'+"a"+'"'+"required type="+'"'+"text"+'"'+"  placeholder="+'"'+"Username"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+"><input id="+'"'+"b"+'"'+"required type="+'"'+"text"+'"'+"  placeholder="+'"'+"Passsword"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+"><input type="+'"'+"submit"+'"'+" class="+'"'+"btn"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div></div></div></div><script>function pass(){const inputa = document.getElementById("+'"'+"a"+'"'+");const inputb = document.getElementById("+'"'+"b"+'"'+");const inputA = inputa.value;const inputB = inputb.value;window.location.href = "+'"'+"login/"+'"'+" + inputA + "+'"'+"/"+'"'+" +inputB;alert("+'"'+"Welcome "+'"'+" + inputA)}</script><a class="+'"'+"btn btn-primary"+'"'+"href="+'"'+"admin"+'"'+">Admin Login</a><a class="+'"'+"btn btn-primary"+'"'+"href="+'"'+"search/Python Cookbook"+'"'+">Search</a>" + resultz  + result + add
@app.route("/admin")
def adminlog():
    return "<div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Login</h2><p>Welcome back! Do you still remember your password?</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input id="+'"'+"a"+'"'+"required type="+'"'+"text"+'"'+"  placeholder="+'"'+"Username"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+"><input id="+'"'+"b"+'"'+"required type="+'"'+"text"+'"'+"  placeholder="+'"'+"Passsword"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+"><input type="+'"'+"submit"+'"'+" class="+'"'+"btn"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div></div></div></div><script>function pass(){const inputa = document.getElementById("+'"'+"a"+'"'+");const inputb = document.getElementById("+'"'+"b"+'"'+");const inputA = inputa.value;const inputB = inputb.value;window.location.href = inputA + "+'"'+"/"+'"'+"+ inputB;alert("+'"'+"Welcome "+'"'+" + inputA)}</script>" +  add
#search
@app.route("/search/<query>")
def search_for_book(query):
  now = str(datetime.now())
  log = "Search For: " + query + now
  syslog.append(log)
  results = []
  for book in records:
    if book['|Title'] == query:
      results.append(book)
    elif book['|Year_Published'] == query:
      results.append(book)
    elif book['|ISBN (PK)'] == query:
      results.append(book)
    elif book['|Category'] == query:
      results.append(book)
    elif book['|Publisher'] == query:
      results.append(book)
    elif book['|Submitted_by'] == query:
      results.append(book)
    #else:
    #  return "Book not found: " + query + add
    
  result = "<br><h2>Found Books</h2><br>"
  show = str(results)
  for character in show:
    if character == "[":
      result += "<table class="+'"'+"table hover"+'"'+">"
    elif character == "]":
      result += "</table>"
    elif character == "|":
      result += "<td class="+'"'+"  "+'"'+">"
    elif character == "{":
      result += "<tr class="+'"'+" "+'"'+">"
    elif character == "}":
      result += "</tr>"
    elif character == ",":
      result += " "
    elif character == "'":
      result += " "
    elif character == ":":
      result += ":<br>"
    else:
        result += character
  return result + add + "<div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Search</h2><p>You can use/search2/{query) to find index of book by category using Fibonacci Search</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input id="+'"'+"a"+'"'+"required type="+'"'+"text"+'"'+"  placeholder="+'"'+"Username"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+"><input type="+'"'+"submit"+'"'+" class="+'"'+"btn"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div></div></div></div><script>function pass(){const inputa = document.getElementById("+'"'+"a"+'"'+");const inputA = inputa.value;window.location.href = inputA;alert("+'"'+"Search For: "+'"'+" + inputA)}</script>"
@app.route("/search2/<query>")
def search_for_cat(query):
    now = str(datetime.now())
    log = "Search For: " + query + now
    syslog.append(log)
    target = query
    index = fibonacci_search_cat(records, target)
    if index == -1:
        return "Target not found " + add
    else:
        indexs = str(index)
        return "Target found at index:"+ indexs + add
#register New account
@app.route("/register/<email>/<phone>/<name>")
def register(name, email, phone):
  if name not in q:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(15):
        password += random.choice(letters)
    a = name + password
    id = str(len(q)+ 1)
    now = datetime.now()
    dict = {'|Phone Number': phone, '|Email':email, '|Name': name, '|ID': id, '|Time_Created': now}
    profile.append(dict)
    q.append(a)
    q.append(name)
    now = str(datetime.now())
    log = "Account Created: " + name + email + phone + now
    syslog.append(log)
    link = "/login/"+name+"/"+password
    return "<p class="+'"'+"stat-value"+'"'+">Your password is:" + password + "</p><br><a class="+'"'+"btn btn-accent"+'"'+"href='" + link + "'>View a list of actions</a><br><a class="+'"'+"btn btn-accent"+'"'+"href='" + link + "/profile'>View your profile</a><br>"+add  
  else:
    b = "<center><h1>ERROR</h1><br>Someone has taken this username" + add
    return b
@app.route("/register")
def registerinfo():
    now = str(datetime.now())
    log = "Register Info: " + now
    syslog.append(log)
    return "<center><div class ="+'"'+"hero"+'"'+"><form><input class="+'"'+"input input-bordered input-warning w-full max-w-xs"+'"'+"  type="+'"'+"text"+'"'+"  id="+'"'+"a"+'"'+" placeholder="+'"'+"Your Email"+'"'+"><input class="+'"'+"input input-bordered input-warning w-full max-w-xs"+'"'+"  minlength="+'"'+"8"+'"'+" type="+'"'+"number"+'"'+"  id="+'"'+"b"+'"'+" placeholder="+'"'+"Your Phone Number"+'"'+"><input class="+'"'+"input input-bordered input-warning w-full max-w-xs"+'"'+"  type="+'"'+"text"+'"'+"  id="+'"'+"c"+'"'+" placeholder="+'"'+"Your Username"+'"'+"><input class="+'"'+"btn"+'"'+" type="+'"'+"submit"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div><script>function pass(){const inputa = document.getElementById("+'"'+"a"+'"'+");const inputb = document.getElementById("+'"'+"b"+'"'+");const inputc = document.getElementById("+'"'+"c"+'"'+");const inputA = inputa.value;const inputB = inputb.value;const inputC = inputc.value;window.location.href = "+'"'+"register/"+'"'+" + inputA + "+'"'+"/"+'"'+" +inputB + "+'"'+"/"+'"'+" + inputC;alert("+'"'+"Welcome "+'"'+" + inputC)}</script>" + add
  
@app.route("/register/<gg>")
def registerbad(gg):
    now = str(datetime.now())
    log = "Account Fail: " + gg + now
    syslog.append(log)
    regex = r'^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z]+$'
    match = re.match(regex, gg)
    if bool(match) == False:
      return "Your email seems to be wrong" + add
    else:
      return "<center><h1>You are missing some info</h1><br>Try to input your information in the form of /register/name/email/phone <br> You are missing your phone and email" + add
@app.route("/register/<gg>/<ggg>")
def registerbad2(gg, ggg):
    now = str(datetime.now())
    log = "Account Fail: " + gg + ggg + now
    syslog.append(log)
    regex = r'^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z]+$'
    match = re.match(regex, gg)
    phone_regex = r'\\b\\d{8}\\b'
    matchs = re.match(phone_regex, ggg)
    if bool(match) == False:
      return "Your email seems to be wrong" + add
    elif bool(matchs) == False:
      return "Your phone number is not in the form +65 12345678"
    else:
      return "<center><h1>You are missing some info</h1><br>Try to input your information in the form of /register/name/email/phone <br> You are missing your phone number" + add
#Admin menu
@app.route("/admin/<pin>")
def all(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
    now = str(datetime.now())
    log = "View Profile: Admin" + now
    syslog.append(log)
    link = '/admin/'+pin
    return "Here is a list of pages you can go to: <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/view'>See All User Password</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/reset'>Reset your password</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/requests'>View all requests</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/requests/n'>See total number of requests</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/requests/address'>Address the newest request</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/syslog'>View syslog</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/syslog-sort'>Sort syslog</a>"+ add
#view all information
@app.route("/admin/<pin>/view")
def view(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
      result = "<br>View All Info<br>"
      z = q + like + dislike
      show = str(z)
      for character in show:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += "<li>"
        else:
          result += character  
      return "Add a value at the end to isolate username /view/ or /view2/ username:" + result + add
@app.route("/admin/<pin>/view/<query>")
def viewq(pin, query):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
    list = q + like + dislike
    target = query
    index = binary_search(list, target)
    if index == -1:
        return "The target string is not found." + add
    else:
        index = str(index)
        return "This is done using Binary Search, try our exponential search feature using view2/(query)<br> The target string is found at index:" + index + add
@app.route("/admin/<pin>/view2/<query>")
def viewq2(pin, query):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
    list = q + like + dislike
    target = query
    index = exponentialSearch(list,len(list),target)
    if index == -1:
        return "The target string is not found." + add
    else:
        index = str(index)
        return "This is done using Exponential Search, try our Binary search feature using view/(query)<br> The target string is found at index:" + index + add
    #syslog
@app.route("/admin/<pin>/syslog")
def syslogging(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
      result = "<br>Customer<br>"
      show = str(syslog)
      for character in show:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += "<li>"
        else:
          result += character  
      return "Add a value at the end to isolate syslog value /sysolog/n:" + result + add
@app.route("/admin/<pin>/syslog-sort")
def syslogsort(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
        quick_sort(syslog, 0, len(syslog) - 1)
        results = str(syslog)
        result = "<br><h2>List of books:</h2><br>"
        for character in results:
            if character == "[":
                result += "<table class="+'"'+"table hover"+'"'+">"
            elif character == "]":
                result += "</table>"
            elif character == "|":
                result += "<td class="+'"'+"  "+'"'+">"
            elif character == "{":
                result += "<tr class="+'"'+" "+'"'+">"
            elif character == "}":
                result += "</tr>"
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":<br>"
            else:
                result += character
        now = str(datetime.now())
        log = "Syslog_Sort: Admin" + now
        syslog.append(log)
        return result + add
#syslog number 
@app.route("/admin/<pin>/syslog/<value>")
def findsyslog(pin, value):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
      vv = int(value)
      mytree = AVLTree()
      root = None
      z = 0
      for i in syslog:
          z += 1
          mytree.insert(z, i)
      node = mytree.search(vv)
      return "Avl Tree Search<br>" + node.value + add

  #show all requests
@app.route("/admin/<pin>/requests")
def adminre(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
      result = "<br>Customer<br>"
      show = str(requests)
      for character in show:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += "<li>"
        else:
          result += character   
      now = str(datetime.now())
      log = "View All Requests: Admin" + now
      syslog.append(log) 
      return result + add
    #show number of requests
@app.route("/admin/<pin>/requests/n")
def adminren(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
      now = str(datetime.now())
      log = "Saw Number Of Requests: Admin" + now
      syslog.append(log)
      n = str(len(requests))
      return "The number of requests to be addressed: " + n + add
@app.route("/admin/<pin>/requests/address")
def address(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
        result = "<br><h2>Customer</h2><br>"
        show = str(requests)
        for character in show:
            if character == "[":
                result += "<table class="+'"'+"table hover"+'"'+">"
            elif character == "]":
                result += "</table>"
            elif character == "|":
                result += "<td class="+'"'+"  "+'"'+">"
            elif character == "{":
                result += "<tr class="+'"'+" "+'"'+">"
            elif character == "}":
                result += "</tr>"
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += "<li>"
            else:
                result += character     
        requests.pop()
        now = str(datetime.now())
        log = "Addressed_Request: Admin" + now
        syslog.append(log)
        n = str(len(requests))
        return result + "You have addressed an issue. <br> The number of requests to be addressed: " + n + add
#reset admin passwword
@app.route("/admin/<pin>/reset")
def reset(pin):
  if pin not in admin:
    return "Wrong Admin Password" + add
  else:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(15):
        password += random.choice(letters)
    admin.pop()
    now = str(datetime.now())
    log = "Reset_password: Admin" + now
    syslog.append(log)
    admin.append(password)
    return "Your New Password is;" + password + add
@app.route("/all/like")
def shlke():
    all = str(like) + add
    return all
@app.route("/all/dislike")
def dshlke():
    all = str(dislike) + add
    return all
@app.route("/all/<query>")
def comments(query):
  now = str(datetime.now())
  log = "Search For: " + query + now
  syslog.append(log)
  results = []
  z = like + dislike 
  for book in z:
    if query in book:
      results.append(book)
      results.append("<br>")

    
  result = "<br><h2>Found Comments</h2><br>"
  show = str(results)
  for character in show:
    if character == "[":
      result += "<table class="+'"'+"table hover"+'"'+">"
    elif character == "]":
      result += "</table>"
    elif character == "|":
      result += "<td class="+'"'+"  "+'"'+">"
    elif character == "{":
      result += "<tr class="+'"'+" "+'"'+">"
    elif character == "}":
      result += "</tr>"
    elif character == ",":
      result += " "
    elif character == "'":
      result += " "
    elif character == ":":
      result += ":<br>"
    else:
        result += character
  return result + add
@app.route("/login/<name>/<password>/profile")
def login(name, password):
  b = name + password
  if name in q:
    if b in q:
      category_1_books = []
      for book in profile:
          if book['|Name'] == name:
              category_1_books.append(book)
      now = str(datetime.now())
      log = "Profile_View: "+ name + now
      syslog.append(log)
      show = str(category_1_books)
      result = "<br><h2 class="+'"'+"stat-value text-primary"+'"'+">Customer Info</h2><br>"
      for character in show:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      link = "<a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='/login/" + name + "/" +password+"'>View Actions</a>"
      return result + link + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#test
@app.route("/viewbooks")
def viewbooks():
  return records
@app.route("/test/<value>")
def test(value):
    return "back"

#timer
@app.route("/login/<name>/<password>/timer")
def timer(name, password):
  b = name + password
  if name in q:
    if b in q:
        array = [101, 12, 20, 24, 35, 38, 39, 42, 48, 204]
        bogo_sort(array)
        return "<h2 class="+'"'+"stat-value text-primary hero"+'"'+">Timer Ended</h2>" + add
    else:
        return "wrong password" + add
  else:
    return "wrong username" + add 
#like comments
@app.route("/login/<name>/<password>/like/<comment>")
def liking(name, password, comment):
  b = name + password
  if name in q:
    if b in q:
      if b in like:
        now = str(datetime.now())
        log = "Posted Like: "+ name + now
        syslog.append(log)
        return "You have like this website before" + add
      else:
        words = name + "liked the website because: " + comment
        like.append(words)
        return "Thanks for likeing<br> Your Comment: " + comment + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add

@app.route("/login/<name>/<password>/like")
def likinginfo(name, password):
  b = name + password
  if name in q:
    if b in q:
        now = str(datetime.now())
        log = "Menu Like Info: "+ name + now
        syslog.append(log)
        link = "/login/"+name+"/"+password
        return "Write a comment after /like in the form of /like/<your comment><br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a><div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Like</h2><p>We appreciate your feedback!</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input required type="+'"'+"text"+'"'+"  id="+'"'+"c"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Your Request"+'"'+"><input class="+'"'+"btn btn-outline btn-warning"+'"'+" type="+'"'+"submit"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div><script>function pass(){const inputc = document.getElementById("+'"'+"c"+'"'+");const inputC = inputc.value;window.location.href = "+'"'+"like/"+'"'+" + inputC;alert("+'"'+"Like comment "+'"'+" + inputC)}</script>" + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#dislike comments
@app.route("/login/<name>/<password>/dislike/<comment>")
def disliking(name, password, comment):
  b = name + password
  if name in q:
    if b in q:
      if b in like:
        now = str(datetime.now())
        log = "Posted Dislike: "+ name + now
        syslog.append(log)
        return "You have like this website before" + add
      else:
        words = name + " disliked the website becasue: " + comment
        dislike.append(words)
        return "Sorry For That<br> Your Comment: " + comment + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
@app.route("/login/<name>/<password>/dislike")
def dislikinginfo(name, password):
  b = name + password
  if name in q:
    if b in q:
        now = str(datetime.now())
        log = "Menu Dislike Info: "+ name + now
        syslog.append(log)
        link = "/login/"+name+"/"+password
        return "Write a comment after /dislike in the form of /dislike/<your comment><br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a><div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Dislike</h2><p>Write what you dislike about this website, we won't judge</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input required type="+'"'+"text"+'"'+"  id="+'"'+"c"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Your Request"+'"'+"><input class="+'"'+"btn btn-outline btn-warning"+'"'+" type="+'"'+"submit"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div><script>function pass(){const inputc = document.getElementById("+'"'+"c"+'"'+");const inputC = inputc.value;window.location.href = "+'"'+"dislike/"+'"'+" + inputC;alert("+'"'+"Dislike comment "+'"'+" + inputC)}</script>" + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#generator
@app.route("/login/<name>/<password>/generator")
def generator(name, password):
  b = name + password
  if name in q:
    if b in q:
        now = str(datetime.now())
        log = "Menu Dislike Info: "+ name + now
        syslog.append(log)
        link = "/login/"+name+"/"+password
        return "Write a comment after /dislike in the form of /dislike/<your comment><br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a><div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Generator</h2><p>Generate a random number and we will use radix to sort it</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input required type="+'"'+"number"+'"'+"  id="+'"'+"a"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Total Number of Numbers"+'"'+"><input required type="+'"'+"number"+'"'+"  id="+'"'+"b"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Starting Value"+'"'+"><input required type="+'"'+"number"+'"'+"  id="+'"'+"c"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Ending Value"+'"'+"><input class="+'"'+"btn btn-outline btn-warning"+'"'+" type="+'"'+"submit"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div><script>function pass(){const inputa = document.getElementById("+'"'+"a"+'"'+");const inputb = document.getElementById("+'"'+"b"+'"'+");const inputc = document.getElementById("+'"'+"c"+'"'+");const inputA = inputa.value;const inputB = inputb.value;const inputC = inputc.value;window.location.href = "+'"'+"generator/"+'"'+" + inputA + "+'"'+"/"+'"'+" + inputB + "+'"'+"/"+'"'+" + inputC;alert("+'"'+"Generating Number... "+'"'+")}</script>" + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
@app.route("/login/<name>/<password>/generator/<A>/<B>/<C>")
def Generator(name, password, A, B, C):
  b = name + password
  if name in q:
    if b in q:
        A = int(A)
        B = int(B)
        C = int(C)
        array = []
        for i in range(A):
            number = random.randint(B, C)
            array.append(number)
        sorted_array = radix_sort(array)
        sorted_array = str(sorted_array)
        return sorted_array + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#main menu
@app.route("/login/<name>/<password>")
def show(name, password):
  b = name + password
  if name in q:
    if b in q:
          results = str(records)
          result = "<br><h2>List of books:</h2><br>"
          for character in results:
            if character == "[":
                result += "<table class="+'"'+"table hover"+'"'+">"
            elif character == "]":
                result += "</table>"
            elif character == "|":
                result += "<td class="+'"'+"  "+'"'+">"
            elif character == "{":
                result += "<tr class="+'"'+" "+'"'+">"
            elif character == "}":
                result += "</tr>"
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":<br>"
            else:
                result += character
          now = str(datetime.now())
          log = "Menu: "+ name + now
          syslog.append(log)
          link = "/login/"+name+"/"+password
          menu = "<br><h1>Welcome to your personal library</h1><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/colors'>Visually View Hex Values (Smooth Sort)</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/timer' onclick="+'"'+"pass()"+'"'+">Random Timer (BogoSort)</a><script>function pass(){alert("+'"'+"Timer Started"+'"'+")}</script>" + add + result
          return menu
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#publisher
#selection_sort
@app.route("/login/<name>/<password>/publisher")
def publisher(name, password):
  b = name + password
  if name in q:
    if b in q:
      length = len(records)

      for i in range(length - 1):
          smallNdx = i
          for j in range(i+1, length):
              if records[j]['|Publisher'] < records[smallNdx]['|Publisher']:
                  smallNdx = j
          if smallNdx != i:
              tmp = records[i]
              records[i] = records[smallNdx]
              records[smallNdx] = tmp
      reversed_array = records[::-1]
      results = str(reversed_array)
      result = "<br><h2>List of books:</h2><br>"
      for character in results:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      now = str(datetime.now())
      log = "Sort_Publisher: "+ name + now
      syslog.append(log)
      link = "/login/"+name+"/"+password           
      return "Records have been sorted by Publisher in decending order<br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#comb sort
@app.route("/login/<name>/<password>/publisherR")
def publisherR(name, password):
  b = name + password
  if name in q:
    if b in q:
      sorted_records = comb_sort(records)
      results = str(sorted_records)
      result = "<br><h2>List of books:</h2><br>"
      for character in results:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      now = str(datetime.now())
      log = "Sort_Publisher: "+ name + now
      syslog.append(log)
      link = "/login/"+name+"/"+password           
      return "Records have been sorted by Publisher in decending order<br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add    
#category
@app.route("/login/<name>/<password>/category")
def category(name, password):
  b = name + password
  if name in q:
    if b in q:
      length = len(records)

      for i in range(length - 1, 0, -1):
          for j in range(i):
              if records[j]['|Category'] > records[j + 1]['|Category']:
                  tmp = records[j]
                  records[j] = records[j + 1]
                  records[j + 1]= tmp
      results = str(records)
      result = "<br><h2>List of books:</h2><br>"
      for character in results:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      now = str(datetime.now())
      log = "Sort_Category: "+ name + now
      syslog.append(log)
      link = "/login/"+name+"/"+password
      return "Records have been sorted by Category<br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result + add 
    else:
        return "wrong password" + add
  else:
    return "wrong username" + add
#categoryR intro sort
@app.route("/login/<name>/<password>/categoryR")
def categoryR(name, password):
  b = name + password
  if name in q:
    if b in q:
      sorted_list = introspective_sort(records)
      reversed_array = records[::-1]
      results = str(reversed_array)
      result = "<br><h2>List of books:</h2><br>"
      for character in results:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      now = str(datetime.now())
      log = "Sort_Category: "+ name + now
      syslog.append(log)
      link = "/login/"+name+"/"+password
      return "Records have been sorted by Category<br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result + add 
    else:
        return "wrong password" + add
  else:
    return "wrong username" + add  
  
#Title Reversed Shell Sort
@app.route("/login/<name>/<password>/titleR")
def titleR(name, password):
    b = name + password
    if name in q:
        if b in q:
            link = "/login/"+name+"/"+password
            shell_sort(records)
            reversed_array = records[::-1]
            results = str(reversed_array)
            result = "<br><h2>List of books:</h2><br>"
            for character in results:
                if character == "[":
                    result += "<table class="+'"'+"table hover"+'"'+">"
                elif character == "]":
                    result += "</table>"
                elif character == "|":
                    result += "<td class="+'"'+"  "+'"'+">"
                elif character == "{":
                    result += "<tr class="+'"'+" "+'"'+">"
                elif character == "}":
                    result += "</tr>"
                elif character == ",":
                    result += " "
                elif character == "'":
                    result += " "
                elif character == ":":
                    result += ":<br>"
                else:
                    result += character
            now = str(datetime.now())
            log = "Sort_Title: "+ name + now
            syslog.append(log) 
            return "Records have been sorted by Title <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result+ add     
        else:
            return "wrong password" + add
    else:
        return "wrong username" + add
#Title
@app.route("/login/<name>/<password>/title")
def title(name, password):
  b = name + password
  if name in q:
    if b in q:
      link = "/login/"+name+"/"+password
      length = len(records)
      for i in range(1, length):
          key = records[i]
          j = i - 1
          while j >= 0 and records[j]['|Title'] > key['|Title']:
              records[j + 1] = records[j]
              j -= 1
          records[j + 1] = key
      results = str(records)
      result = "<br><h2>List of books:</h2><br>"
      for character in results:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      now = str(datetime.now())
      log = "Sort_Title: "+ name + now
      syslog.append(log) 
      return "Records have been sorted by Title <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result+ add     
    else:
        return "wrong password" + add
  else:
    return "wrong username" + add
#Year ISBN acending merge sort
@app.route("/login/<name>/<password>/Year-ISBN")
def YearISBN(name, password):
  b = name + password
  if name in q:
    if b in q:
        link = "/login/"+name+"/"+password
        sorted_book = merge_sorty(records)
        results = str(sorted_book)
        result = "<br><h2>List of books:</h2><br>"
        for character in results:
            if character == "[":
                result += "<table class="+'"'+"table hover"+'"'+">"
            elif character == "]":
                result += "</table>"
            elif character == "|":
                result += "<td class="+'"'+"  "+'"'+">"
            elif character == "{":
                result += "<tr class="+'"'+" "+'"'+">"
            elif character == "}":
                result += "</tr>"
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":<br>"
            else:
                result += character
        now = str(datetime.now())
        log = "Sort_YearISBN: "+ name + now
        syslog.append(log)           
        return "Records have been sorted by Category <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result+ add
    else:
        return "wrong password" + add
  else:
    return "wrong username" + add
#Year ISBN decending  heap sort
@app.route("/login/<name>/<password>/Year-ISBNR")
def YearISBNR(name, password):
  b = name + password
  if name in q:
    if b in q:
        link = "/login/"+name+"/"+password
        random.shuffle(records)
        heap_sort_year(records)
        heap_sort_ISBN(records)
        reversed_array = records[::-1]
        results = str(reversed_array)
        result = "<br><h2>List of books:</h2><br>"
        for character in results:
            if character == "[":
                result += "<table class="+'"'+"table hover"+'"'+">"
            elif character == "]":
                result += "</table>"
            elif character == "|":
                result += "<td class="+'"'+"  "+'"'+">"
            elif character == "{":
                result += "<tr class="+'"'+" "+'"'+">"
            elif character == "}":
                result += "</tr>"
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":<br>"
            else:
                result += character
        now = str(datetime.now())
        log = "Sort_YearISBN: "+ name + now
        syslog.append(log)           
        return "Records have been sorted by Category <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + result+ add
    else:
        return "wrong password" + add
  else:
    return "wrong username" + add
def merge_sorty(books):
    if len(books) <= 1:
        return books
    mid = len(books) // 2
    left = merge_sorty(books[:mid])
    right = merge_sorty(books[mid:])
    return merge_year(left, right)

def merge_year(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]['|Year_Published'] <= right[j]['|Year_Published']:
          if left[i]['|ISBN (PK)'] <= right[j]['|ISBN (PK)']:
              merged.append(left[i])
              i += 1
          else:
            merged.append(right[j])
            j += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

#addbook tutorial
@app.route("/login/<name>/<password>/addbook")
def addnew(name, password):
  b = name + password
  if name in q:
    if b in q:
      now = str(datetime.now())
      log = "Addbook_Info: "+ name + now
      syslog.append(log) 
      link = "/login/"+name+"/"+password
      return "<h1>Adding A Book</h1><br>Your Download Link must be from Libgen, search the book here <a href='http://libgen.is/'> Search</a><br>You can book by typing /title/Category/Publisher/YearPublished/Download_link <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a><div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Addbook</h2><p>Libgen Code: It looks something like 736d9cc8adfd335ded6c9ebc003e15d2&key=MTBS8IRE34V5J2MI</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input type="+'"'+"text"+'"'+" id="+'"'+"a"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Book Title"+'"'+"><input type="+'"'+"text"+'"'+" id="+'"'+"b"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Book Category"+'"'+"><input type="+'"'+"text"+'"'+" id="+'"'+"c"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Book Publisher"+'"'+"><input type="+'"'+"number"+'"'+" id="+'"'+"d"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Book Year"+'"'+"><input type="+'"'+"text"+'"'+" id="+'"'+"e"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Libgen code"+'"'+"><input type="+'"'+"submit"+'"'+" class="+'"'+"btn btn-outline btn-warning"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div><script>function pass(){const inputa = document.getElementById("+'"'+"a"+'"'+");const inputb = document.getElementById("+'"'+"b"+'"'+");const inputc = document.getElementById("+'"'+"c"+'"'+");const inputd = document.getElementById("+'"'+"d"+'"'+");const inpute = document.getElementById("+'"'+"e"+'"'+");const inputA = inputa.value;const inputB = inputb.value;const inputC = inputc.value;const inputD = inputd.value;const inputE = inpute.value;window.location.href = "+'"'+"addbook/"+'"'+" + inputA + "+'"'+"/"+'"'+" + inputB + "+'"'+"/"+'"'+" + inputC + "+'"'+"/"+'"'+" + inputD+ "+'"'+"/"+'"'+" + inputE;alert("+'"'+"Added your book"+'"'+" + inputA)}</script>" + add + result
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#request info page 
@app.route("/login/<name>/<password>/request")
def requestinfo(name, password):
  b = name + password
  if name in q:
    if b in q:
      now = str(datetime.now())
      log = "Request_Info: "+ name + now
      syslog.append(log) 
      link = "/login/"+name+"/"+password
      return "<h1>You can request by typing /request/(your request)</h1><br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/profile'>View Profile</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a><div class="+'"'+"hero"+'"'+"><div class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><div class="+'"'+"card-body"+'"'+"><h2 class="+'"'+"card-title"+'"'+">Make A Request</h2><p>We will address your needs as soon as possible!</p><div class="+'"'+"card-actions justify-end"+'"'+"><form class="+'"'+"card w-96 bg-base-100 shadow-xl"+'"'+"><input required type="+'"'+"text"+'"'+"  id="+'"'+"c"+'"'+" class="+'"'+"input input-ghost w-full max-w-xs"+'"'+" placeholder="+'"'+"Your Request"+'"'+"><input class="+'"'+"btn btn-outline btn-warning"+'"'+" type="+'"'+"submit"+'"'+" onclick="+'"'+"pass()"+'"'+"></form></div><script>function pass(){const inputc = document.getElementById("+'"'+"c"+'"'+");const inputC = inputc.value;window.location.href = "+'"'+"request/"+'"'+" + inputC;alert("+'"'+"Request "+'"'+" + inputC)}</script>" + add
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
@app.route("/login/<name>/<password>/request/<request>")
def request(name, password, request):
  b = name + password
  if name in q:
    if b in q:
      category_1_books = []
      for book in profile:
          if book['|Name'] == name:
              category_1_books.append(book)

      show = str(category_1_books)
      result = "<br><h2>Customer Info</h2><br>"
      for character in show:
        if character == "[":
            result += "<table class="+'"'+"table hover"+'"'+">"
        elif character == "]":
            result += "</table>"
        elif character == "|":
            result += "<td class="+'"'+"  "+'"'+">"
        elif character == "{":
            result += "<tr class="+'"'+" "+'"'+">"
        elif character == "}":
            result += "</tr>"
        elif character == ",":
            result += " "
        elif character == "'":
            result += " "
        elif character == ":":
            result += ":<br>"
        else:
            result += character
      re = str(request)      
      add_request = result + "<br>"+re +"<br>--------------"
      requests.append(add_request)
      now = str(datetime.now())
      log = "Request Added: "+ name + add_request + now
      syslog.append(log) 
      link = "/login/"+name+"/"+password
 
      return "The quest that was sent to admin: <br><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"'> 1. Display all the books records</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/addbook'>2. Add a new book record</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/category'>3. Sort books by their Category in ascending order using Bubble sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/categoryR'>3.2 Sort books by their Category in decending order using Introspective sort and display the outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisher'>4. Sort the Publisher in decending order using only Selection sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/publisherR'>4.2 Sort the Publisher in accending order using only Comb sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/title'>5. Sort the books by Title in ascending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/titleR'>5.2 Sort the books by Title in decending order using only Insertion sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBN'>6. Sort the books by Year then ISBN in ascending order using only Merge sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/Year-ISBNR'>6.2 Sort the books by Year then ISBN in decending order using only Heap Sort and display outcome</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/request'>7. Create a request to admin</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/like'> Write what you like about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/dislike'>Write what you dislike about the website</a><a class="+'"'+"btn btn-outline btn-warning"+'"'+"href='"+link+"/generator'>Random Number Generator (Radix Sort)</a>" + add_request + add

    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
@app.route("/login/<name>/<password>/colors")
def colors(name, password):
  b = name + password
  if name in q:
    if b in q:
        array = []
        array2 = []
        i = 1000
        while i < 9999:
            i+=1
            array.append(i)
        shuffle_array(array)
        for z in array:
            g = str(z)
            f = "<div class="+'"'+"d"+'"'+"style="+'"'+"background-color:#"+g+'"'+"></div>"
            array2.append(f)
        u = str(array2)
        result = " "
        for character in u:
            if character == "[":
                result += " "
            elif character == "]":
                result += " "
            elif character == "{":
                result += " "
            elif character == "}":
                result += " "
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":"
            else:
                result += character
        now = str(datetime.now())
        log = "Color Sort: "+ name + now
        syslog.append(log) 
        link = "/login/"+name+"/"+password
 
        return  result + "<a href="+'"'+"colors/sort"+'"'+">Sort With SmoothSort </a><style>*{display:flex;flex-flow:wrap;background-color:black}.d{width:1vw;height:1vh;}</style>"

    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
@app.route("/login/<name>/<password>/colors/sort")
def colorsort(name, password):
  b = name + password
  if name in q:
    if b in q:
        array = []
        array2 = []
        i = 1000
        smoothsort(array)
        while i < 9999:
            i+=1
            array.append(i)
        for z in array:
            g = str(z)
            f = "<div class="+'"'+"d"+'"'+"style="+'"'+"background-color:#"+g+'"'+"></div>"
            array2.append(f)
        u = str(array2)
        result = " "
        for character in u:
            if character == "[":
                result += " "
            elif character == "]":
                result += " "
            elif character == "{":
                result += " "
            elif character == "}":
                result += " "
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":"
            else:
                result += character
        return  result + "<style>*{display:flex;flex-flow:wrap;background-color:black}.d{width:1vw;height:1vh;}</style>"
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add
#Book Added
@app.route("/login/<name>/<password>/addbook/<title>/<Category>/<Publisher>/<Year>/<link>")
def addbook(name, password, title, Category, Publisher, Year, link):
  b = name + password
  if name in q:
    if b in q:
      if Year.isdigit():
        Year = int(Year)
        if Year > 0:
            Year = Year
        else:
            return "invalid, lesser than 0" + add            
      else:
          return "not integer" + add
      StrYear = str(Year)
      PK = len(ISBN_list) + 1
      strPK = str(PK)
      ISBN_list.append(PK)
      if PK not in ISBN_list:
        return "An unknown error happened" + add
      else:
          ISBN_list.append(PK)
          links = "<a href="+'"'+"https://libgen.rocks/get.php?md5="+link+'"'+"> Download</a>"
          dict = {'|Year_Published': StrYear, '|ISBN (PK)': strPK, '|Title':title, '|Category': Category, '|Publisher': Publisher, '|Submitted_by': name, '|Download': links}
          records.append(dict)
          now = str(datetime.now())
          log = "Book_Added: "+ name + dict + now
          syslog.append(log + "\n")  
          results = str(records)
          result = "<br><h2>List of books:</h2><br>"
          for character in results:
            if character == "[":
                result += "<table class="+'"'+"table hover"+'"'+">"
            elif character == "]":
                result += "</table>"
            elif character == "|":
                result += "<td class="+'"'+"  "+'"'+">"
            elif character == "{":
                result += "<tr class="+'"'+" "+'"'+">"
            elif character == "}":
                result += "</tr>"
            elif character == ",":
                result += " "
            elif character == "'":
                result += " "
            elif character == ":":
                result += ":<br>"
            else:
                result += character
          return "book has been added" + add + result
    else:
      return "wrong password" + add
  else:
    return "wrong username" + add

#AVL
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = Node(key, value)
        self._insert(new_node)

    def _insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert_recursive(node, self.root)

    def _insert_recursive(self, node, current_node):
        if node.key < current_node.key:
            if current_node.left is None:
                current_node.left = node
            else:
                self._insert_recursive(node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = node
            else:
                self._insert_recursive(node, current_node.right)

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self._search_recursive(key, self.root)

    def _search_recursive(self, key, current_node):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._search_recursive(key, current_node.left)
        else:
            return self._search_recursive(key, current_node.right)
    def delete(self, root, key):
 
        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
#hash map        
class HashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def put(self, key, value):
        index = hash(key) % len(self.buckets)
        self.buckets[index].append((key, value))

    def get(self, key):
        index = hash(key) % len(self.buckets)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None
#binary search
def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#quick sort
def quick_sort(array, low, high):
    if low < high:
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        quick_sort(array, low, i)
        quick_sort(array, i + 2, high)
#exponential search
def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2,
                        min(i, n - 1), x)
#heap sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i]['|ISBN (PK)'] < arr[l]['|ISBN (PK)']:
        largest = l
    if r < n and arr[largest]['|ISBN (PK)'] < arr[r]['|ISBN (PK)']:
        largest = r
    if largest != i:
        arr[i]['|ISBN (PK)'], arr[largest]['|ISBN (PK)'] = arr[largest]['|ISBN (PK)'], arr[i]['|ISBN (PK)']
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i]['|ISBN (PK)'], arr[0]['|ISBN (PK)'] = arr[0]['|ISBN (PK)'], arr[i]['|ISBN (PK)']
        heapify(arr, i, 0)
#libgen check
def check_hello(input_str):
  first_5_chars = input_str[:33]
  return first_5_chars == "https://libgen.rocks/get.php?md5="
#radix sort
def radix_sort(array, radix=10):
  max_digit = 0
  for i in array:
    max_digit = max(max_digit, int(i / radix))
  for i in range(max_digit + 1):
    bucket = [[] for _ in range(radix)]
    for j in array:
      bucket[int((j / radix**i) % radix)].append(j)
    array = []
    for j in bucket:
      array += j
  return array
#bogo sort
def bogo_sort(array):
    random.shuffle(array)
    is_sorted = False
    while not is_sorted:
        random.shuffle(array)
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                is_sorted = False
#shell sort
def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]['|Title']
            j = i
            while j >= gap and array[j - gap]['|Title'] > temp:
                array[j]['|Title'] = array[j - gap]['|Title']
                j -= gap
            array[j]['|Title'] = temp
        gap //= 2
#introspective sort
def introspective_sort(records):
  max_depth = int(math.ceil(math.log2(len(records))))

  def _introsort_helper(records, start, end, max_depth):
    if end - start <= 1:
      return
    elif max_depth == 0:
      insertion_sort(records, start, end)
    else:
      p = partition(records, start, end)
      _introsort_helper(records, start, p + 1, max_depth - 1)
      _introsort_helper(records, p + 1, end, max_depth - 1)

  def partition(records, start, end):
    pivot = records[start]
    i = start - 1
    j = end
    while True:
      i += 1
      while records[i]['|Category'] < pivot['|Category']:
        i += 1
      j -= 1
      while records[j]['|Category'] > pivot['|Category']:
        j -= 1
      if i >= j:
        return j
      swap(records, i, j)

  def swap(records, i, j):
    records[i]['|Category'], records[j]['|Category'] = records[j]['|Category'], records[i]['|Category']

  def insertion_sort(records, start, end):
    for i in range(start + 1, end):
      current_element = records[i]['|Category']
      j = i - 1
      while j >= start and records[j]['|Category']> current_element:
        records[j + 1]['|Category'] = records[j]['|Category']
        j -= 1
      records[j + 1]['|Category'] = current_element

  _introsort_helper(records, 0, len(records), max_depth)
  return records
def fibonacci_search_cat(records, target):
    a, b = 0, 1
    while b < len(records):
        if target < records[b]['|Category']:
            return a
        elif target > records[b]['|Category']:
            a, b = b, b + a
        else:
            return b
    return -1
#heapsort year
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left]['|Year_Published'] > arr[largest]['|Year_Published']:
        largest = left
    if right < n and arr[right]['|Year_Published'] > arr[largest]['|Year_Published']:
        largest = right
    if largest != i:
        arr[i]['|Year_Published'], arr[largest]['|Year_Published'] = arr[largest]['|Year_Published'], arr[i]['|Year_Published']
        heapify(arr, n, largest)
def heap_sort_year(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0]['|Year_Published'], arr[i]['|Year_Published'] = arr[i]['|Year_Published'], arr[0]['|Year_Published']
        heapify(arr, i, 0)
#heap sort isbn
def heapifyI(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left]['|ISBN (PK)'] > arr[largest]['|ISBN (PK)']:
        largest = left
    if right < n and arr[right]['|ISBN (PK)'] > arr[largest]['|ISBN (PK)']:
        largest = right
    if largest != i:
        arr[i]['|ISBN (PK)'], arr[largest]['|ISBN (PK)'] = arr[largest]['|ISBN (PK)'], arr[i]['|ISBN (PK)']
        heapifyI(arr, n, largest)
def heap_sort_ISBN(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapifyI(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0]['|ISBN (PK)'], arr[i]['|ISBN (PK)'] = arr[i]['|ISBN (PK)'], arr[0]['|ISBN (PK)']
        heapifyI(arr, i, 0)
        
#smooth sort
_leonardo_nums = [1, 1]

def L(k):
    try:
        return _leonardo_nums[k]
    except IndexError:
        while len(_leonardo_nums) <= k:
            _leonardo_nums.append(_leonardo_nums[-2] + _leonardo_nums[-1] + 1)
        return _leonardo_nums[k]


# sorts into ascending order
def smoothsort(arr):
    size_list = _create_heap(arr)
    _sort_heap(arr, size_list)
    return arr


# sorts the max heap in-place. requires the list of sizes of leonardo trees in
# the forest
def _sort_heap(heap, size_list):
    for heap_size in reversed(range(len(heap))):
        _dequeue_max(heap, size_list, heap_size)


# removes the max value from the graph
def _dequeue_max(heap, size_list, heap_size):
    removed_size = size_list.pop()
    # case 1: rightmost tree has a single node
    if removed_size == 0 or removed_size == 1:
        pass  # already removed
    # case 2: rightmost tree has two children
    else:
        # add sizes back
        size_list.append(removed_size - 1)
        size_list.append(removed_size - 2)
        # calculate indices of left and right children
        left_idx = heap_size - L(size_list[-1]) - 1
        right_idx = heap_size - 1
        left_size_idx = len(size_list) - 2
        right_size_idx = len(size_list) - 1
        # fix left child
        idx, size_idx = _fix_roots(heap, size_list, left_idx, left_size_idx)
        _sift_down(heap, idx, size_list[size_idx])
        # fix right child
        idx, size_idx = _fix_roots(heap, size_list, right_idx, right_size_idx)
        _sift_down(heap, idx, size_list[size_idx])


# modifies array in-place to make a heap. returns list of sizes of leonardo
# trees in the forest
def _create_heap(arr):
    size_list = []
    for heap_end in range(len(arr)):
        # Update the sizes of the trees in the forest
        _add_new_root(size_list)

        # Swap the root nodes of the trees. Return [heap index, size index]
        idx, size_idx = _fix_roots(arr, size_list, heap_end, len(size_list) - 1)

        # Fix the tree that now has the new node
        _sift_down(arr, idx, size_list[size_idx])

    return size_list


# updates the list of sizes of leonardo trees in a forest after a new node is
# added
def _add_new_root(size_list):
    # case 1: Empty forest. Add L_1 tree.
    if len(size_list) == 0:
        size_list.append(1)
    # case 2: Forest with two rightmost trees differing in size by 1.
    #         Replace the last two trees of size L_k-1 and L_k-2 by a single
    #         tree of size L_k.
    elif len(size_list) > 1 and size_list[-2] == size_list[-1] + 1:
        size_list[-2] = size_list[-2] + 1
        del size_list[-1]
    # case 3: Add a new tree, either L_1 or L_0
    else:
        # case 1: Rightmost tree is an L_1 tree. Add L_0 tree.
        if size_list[-1] == 1:
            size_list.append(0)
        # case 2: Rightmost tree is not an L_1 tree. Add L_1 tree.
        else:
            size_list.append(1)


# modifies 'heap' in place, assuming an implicit Leonardo heap structure exists
# with trees having sizes in the order given by 'sizes'
def _fix_roots(heap, sizes, start_heap_idx, start_size_idx):
    # variables in this function are referring to indexes
    cur = start_heap_idx
    size_cur = start_size_idx
    # keep fixing roots until we're at the leftmost root
    while size_cur > 0:
        next = cur - L(sizes[size_cur])
        # stop if the next root is not strictly greater than the current root
        if heap[next] <= heap[cur]:
            break
        # stop if the next root is not greater than both children of the
        # current root, if those children exist, i.e. the size of the current
        # tree is not 0 or 1.
        if sizes[size_cur] > 1:
            right = cur - 1
            left = right - L(sizes[size_cur]-2)
            if heap[next] <= heap[right] or heap[next] <= heap[left]:
                break

        # swap the current root with the next root
        temp = heap[cur]
        heap[cur] = heap[next]
        heap[next] = temp
        # continue, starting with the next root as the current root
        size_cur = size_cur - 1
        cur = next
    return (cur, size_cur)


# Fixes the tree of size tree_size rooted at root_idx in heap, where heap is otherwise a valid heap
def _sift_down(heap, root_idx, tree_size):
    cur = root_idx
    # continue iterating until there are no child nodes
    while tree_size > 1:
        right = cur - 1
        left = cur - 1 - L(tree_size - 2)
        # the root is at least as large as both children
        if heap[cur] >= heap[left] and heap[cur] >= heap[right]:
            break
        # the right child is at least as large as the left child
        elif heap[right] >= heap[left]:
            heap[cur], heap[right] = heap[right], heap[cur]
            cur = right
            tree_size = tree_size - 2
        # the left child is the greatest of the three
        else:
            heap[cur], heap[left] = heap[left], heap[cur]
            cur = left
            tree_size = tree_size - 1
#shuffle
def shuffle_array(array):
    for i in range(len(array)):
        # Generate a random index between i and the length of the array
        random_index = random.randint(i, len(array) - 1)

        # Swap the elements at index i and random_index
        temp = array[i]
        array[i] = array[random_index]
        array[random_index] = temp

    return array
#comb sort
def comb_sort(array):
  gap = len(array)
  shrink = 1.3
  swapped = True
  while gap > 1 or swapped:
    gap = int(gap / shrink)
    swapped = False
    for i in range(0, len(array) - gap):
      if array[i]['|Publisher'] > array[i + gap]['|Publisher']:
        array[i]['|Publisher'], array[i + gap]['|Publisher'] = array[i + gap]['|Publisher'], array[i]['|Publisher']
        swapped = True
  return array
#Defence
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)
limiter = Limiter(get_remote_address, app=app, default_limits=["2000 per day", "500 per hour"])  
@app.route('/.env')
@app.route('/admin')
@app.route('/webfig')
@app.route('/owa')
@app.route('/solr')
@app.route('/solr')
@app.route('/cgi-bin')
@app.route('/cgi-bin/config.exp')
@app.route('/remote/login')
def attack():
    now = str(datetime.now())
    log = "bot_attack: "+now
    syslog.append(log)
    return redirect('/attack')
##Injection check ##
@app.route('/<gg>.json')
@app.route('/<gg>.xml')
@app.route('/<gg>}}')
@app.route('/<gg>)')
@app.route('/<gg>--')
@app.route('/<gg>>')
@app.route('/<gg>.html')
@app.route('/<gg>.txt')
def json_request(gg):
    now = str(datetime.now())
    log = "Injection_attack: "+now
    syslog.append(log)
    return redirect('/attack')
##Cycler ##
@app.route('/attack')
def atk():
    return redirect('/attack2')
@app.route('/attack2')
def atkk():
    return redirect('/attack')
@app.errorhandler(401)
def Unauthorized(e):
    now = str(datetime.now())
    log = "Unauthorized Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(404)
def NotFound(e):
    now = str(datetime.now())
    log = "PageNotFound Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(405)
def MethodNotAllowed(e):
    now = str(datetime.now())
    log = "Method_Not_Allowed Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(406)
def NotAcceptable(e):
    now = str(datetime.now())
    log = "Not_Acceptable Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(408)
def RequestTimeout(e):
    now = str(datetime.now())
    log = "Request_Timeout Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(423)
def Locked(e):
    now = str(datetime.now())
    log = "Locked: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(410)
def Gone(e):
    now = str(datetime.now())
    log = "Gone: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(500)
def internalserver(e):
    now = str(datetime.now())
    log = "Internal_Server Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(501)
def NotImplemented(e):
    now = str(datetime.now())
    log = "Not Implemented Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(502)
def Bad_gateway(e):
    now = str(datetime.now())
    log = "Bad_Gateway Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(503)
def ServiceUnavailable(e):
    now = str(datetime.now())
    log = "ServiceUnavailable Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(504)
def GatewayTimeout(e):
    now = str(datetime.now())
    log = "GatewayTimeout Error: "+now
    syslog.append(log)
    return redirect("/")
@app.errorhandler(505)
def Unsupported(e):
    now = str(datetime.now())
    log = "Unsupported Error: "+now
    syslog.append(log)
    return redirect("/")
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)