from django.shortcuts import render

# Create your views here.
def index(request):
    names="john,doe,mark,swain"
    return  render(request,"index.html",{"names":names})

def greeting_view(request):
    books={"The night rider": "Ben Author",\
          "The Justice": "Don Abeman"}

    return render(request,"simple_tag_template.html",{"username":'Vasanth AKA  BMW_Kunju ','books':books})
