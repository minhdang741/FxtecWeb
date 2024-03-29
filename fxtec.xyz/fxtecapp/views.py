from django.shortcuts import render
from fxtecapp.models import Robot
from django.http import HttpResponse
import time
import random
from rest_framework import generics
from .serializers import RobotModelSerializer
from pprint import pprint
# Create your views here.

class RobotListAPIView(generics.ListAPIView):
# def robotview(generics.ListAPIView):
    serializer_class = RobotModelSerializer
    #def get_queryset(self):
    '''
    def get_queryset(self):
        a = compare()
        #del a
        return Robot.objects.all()
    # return Robot.objects.all()
    '''

    #class View():
    def get_queryset(self):
        ##### Get equity and balance
        countrobot = Robot.objects.all().count() # Count robot
        count = countrobot + 1
        EQT = []
        BAL = []
        #x = random.randrange(8000000, 9999999, 1000000)
        for i in range(1, count):
            # Get equity
            equity = list(Robot.objects.filter(id=i).values('EQUITY')) # equity = [{'equity': 8901231.12}]
            equity = equity[0] # equity = {'equity': 8901231.12}
            EQT.append(equity['EQUITY']) # EQT1 = [8901231.12]

            # Get balance
            balance = list(Robot.objects.filter(id=i).values('BALANCE'))
            balance = balance[0]
            BAL.append(balance['BALANCE'])
        ##### Get equity and balance
        """
        ##### Get time for first time
        TIME1 = []
        TIME2 = []
        for i in range(1, count):
            times = list(Robot.objects.filter(id=i).values('TIME')) # [{'time': 12367541982}]
            times = times[0] # {'time': 12367541982}
            TIME1.append(times['TIME']) # 12367541982
        ##### Get time for first time #####

        time.sleep(0.5) # Wait 0.5s

        ##### Get equity for second time
        for i in range(1, count):
            equity = list(Robot.objects.filter(id=i).values('EQUITY')) # equity = [{'equity': 8901231.12}]
            equity = equity[0] # equity = {'equity': 8901231.12}
            EQT2.append(equity['EQUITY']) # EQT2 = [8901231.12]
            #EQT2.append(x)
        ##### Get equity for second time #####

        ##### Get time for second time
        for i in range(1, count):
            times = list(Robot.objects.filter(id=i).values('TIME')) # [{'time': 12367541982}]
            times = times[0] # {'time': 12367541982}
            TIME2.append(times['TIME']) # 12367541982
        ##### Get time for second time #####
        """

        ##### Compare equity
        for i in range(countrobot):
            if BAL[i] > EQT[i]:
                i = i + 1 # EQT_list begin with 0 but robot id begins with 1
                # EQT3.append('True')
                Robot.objects.filter(id=i).update(EQTCHECK='False')
            else:
                i = i + 1
                # EQT3.append('False')
                Robot.objects.filter(id=i).update(EQTCHECK='True')
        ##### Compare equity #####

        """
        ##### Compare time
        for i in range(countrobot):
            if TIME1[i] < TIME2[i]:
                i = i + 1 # TIME_list begins with 0 but robot id begins with 1
                Robot.objects.filter(id=i).update(TIMECHECK='1')
            else:
                Robot.objects.filter(id=i).update(TIMECHECK='1')
        ##### Compare time #####
        """

        del EQT, BAL, equity, balance # Destructor

        return Robot.objects.all()



'''
def view(request):
    """
    count = Robot.objects.all().count()
    count = count + 1
    for i in range(1, 3):
        data = {'robotdata': Robot.objects.filter(id=i).values()}
    """
    ##### Check equity
    countrobot = Robot.objects.all().count() # Count robot
    count = countrobot + 1
    EQT1 = []
    EQT2 = []
    # x = random.randrange(8000000, 9999999, 1000000)
    # Get equity for first time
    for i in range(1, count):
        equity = list(Robot.objects.filter(id=i).values('EQUITY')) # equity = [{'equity': 8901231.12}]
        equity = equity[0] # equity = {'equity': 8901231.12}
        EQT1.append(float(equity['EQUITY'])) # EQT1 = [8901231.12]
    time.sleep(3) # Wait 3s
    # Get equity for second time
    for i in range(1, count):
        equity = list(Robot.objects.filter(id=i).values('EQUITY')) # equity = [{'equity': 8901231.12}]
        equity = equity[0] # equity = {'equity': 8901231.12}
        EQT2.append(float(equity['EQUITY'])) # EQT2 = [8901231.12]
        # EQT2.append(x)
    # Compare equity
    for i in range(countrobot):
        if EQT1[i] >= EQT2[i]:
            i = i + 1 # EQT_list begin with 0 but robot id begins with 1
            # EQT3.append('True')
            Robot.objects.filter(id=i).update(EQTCHECK='True')
        else:
            i = i + 1
            # EQT3.append('False')
            Robot.objects.filter(id=i).update(EQTCHECK='False')
    ##### Check equity #####

    ##### Check time
    TIME1 = []
    TIME2 = []
    # Get time for first time
    for i in range(1, count):
        times = list(Robot.objects.filter(id=i).values('TIME')) # [{'time': 12367541982}]
        times = times[0] # {'time': 12367541982}
        TIME1.append(float(times['TIME'])) # 12367541982
    time.sleep(15) # Wait 3s
    # Get time for second time
    for i in range(1, count):
        times = list(Robot.objects.filter(id=i).values('TIME')) # [{'time': 12367541982}]
        times = times[0] # {'time': 12367541982}
        TIME2.append(float(times['TIME'])) # 12367541982
    # Compare time
    for i in range(countrobot):
        if TIME1[i] < TIME2[i]:
            i = i + 1 # TIME_list begins with 0 but robot id begins with 1
            Robot.objects.filter(id=i).update(TIMECHECK='1')
        else:
            Robot.objects.filter(id=i).update(TIMECHECK='1')
    ##### Check time #####

    DATA = {'robotdata': Robot.objects.all()} # Query all robot data
    return render(request, 'View.html', DATA)
    # return HttpResponse(x)
'''

'''
def checkequity(self):
        countrobot = Robot.objects.all().count()
        count = countrobot + 1
        EQT2 = []
        EQT1 = []
        EQT3 = []
        for i in range(1, count):
            equity = list(Robot.objects.filter(id=i).values('equity')) # equity = [{'equity': 8901231.12}]
            equity = equity[0] # equity = {'equity': 8901231.12}
            EQT1.append(equity['equity']) # EQT1 = [8901231.12]
        time.sleep(3)
        for i in range(1, count):
            equity = list(Robot.objects.filter(id=i).values('equity')) # equity = [{'equity': 8901231.12}]
            equity = equity[0] # equity = {'equity': 8901231.12}
            EQT2.append(equity['equity']) # EQT2 = [8901231.12]
        for i in range(countrobot):
            if EQT1[i] >= EQT2[i]:
                # EQT3.append('True')
                Robot.objects.filter(id=i).update(eqtcheck='True')
            else:
                # EQT3.append('False')
                Robot.objects.filter(id=i).update(eqtcheck='False')
        return HttpResponse('Hello')
        """
        KEYLIST = []
        for i in range(countrobot):
            KEYLIST.append(str(i))
        eqt = zip(KEYLIST, EQT3)
        eqt = {'key': dict(eqt)}
        """
'''
