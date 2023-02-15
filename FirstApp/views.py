from django.shortcuts import render

# Create your views here.
import datetime;
def wishes3(request):
    date1=datetime.datetime.now();
    msg1="Hello User/Client......GOOD";
    hr=int(date1.strftime('%H'));
    if hr<12:
        msg1+='Morning';
        imgs='image1.jpg';
    elif hr<4:
        msg1+='Afternoon';
        imgs='image2.jpg';
    elif hr<8:
        msg1+='Evening';
        imgs='image3.jpg';
    else:
        msg1="Hello User/Client.....GOOD night";
        imgs='image5.jpg';
        dict1={'server_date1': date1,'msg1': msg1,'imgs': imgs}
    return render(request,'FirstApp/wishes2.html',context=dict1);


import datetime;
def imgsgallery(request):
    date1=datetime.datetime.now()
    msg1="***DJANGO TEMPLATE GALEERY";
    dict1={'date1': date1, 'msg1':msg1};
    return render(request,'FirstApp/imgsgallery.html',context=dict1);

import datetime;
def imgsgallery2(request):
    date1=datetime.datetime.now()
    msg1="***DJANGO TEMPLATE GALEERY";
    dict1={'date1': date1, 'msg1':msg1};
    return render(request,'FirstApp/imgsgallery2.html',context=dict1);


def sample_view(request):
    return render(request,'FirstApp/sample.html')
