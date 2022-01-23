from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import userData, num_counters, Employee
import random
from django.contrib.auth.models import User, auth, Group

#----------------------------------------------------------FILL THE DETAILS BELOW--------------------------------------------------------------------

#email: input your email id and password as a string below
import smtplib
sender_email = ""
password = ""

#phone: input your twilio account's SID, token and phone number as a string below
from twilio.rest import Client
account_sid = ''
auth_token = ''
twilio_phone = ''   #start with '+'

#--------------------------------------------------------------END OF DETAILS------------------------------------------------------------------------

#uid is the token number, starts with 0, increments with 1 and so on...
uid = 0

#getting the admin info
u = User.objects.get(username='admin')

#the employee model under application App1 has the data of admin, the counterNumber for admin means the total number of
#counters the admin want the employees to access. For others, it is zero by default and can be selected from selectCounter
#website by employee numbered between 1 and total_counters (admin's counter number)
#The admin can change the the total number of counters anytime but the system would have to restart for the changes to be applied
total_counters = u.employee.counterNumber

#counters is a dictionary which represents the counters and the number of people (queue size) of each available counter
#For eg, counters = {1:5, 2:4, 4:6} means 1st counter has 5 people, 2nd counter has 4 people and 4th counter has 6 people
#Empty by default, an employee would have to select a counter first for it to work
counters = {}

#naming convention w.r.t. employee (the counters available for the employees to choose)
#For eg, if the total_counters is 4, then the employees can choose counter from 1, 2, 3, 4
#No employee can select more than 1 counter
availableCounters = list(range(1, total_counters + 1))

#index (main) page
def index(request):
    return render(request, 'index.html')

#customer registration page
def register(request):
    #if counters dictionary is empty i.e. none of the counters is assigned to any employee. Hence, customers can't register.
    if not counters:
        return HttpResponse('There is no counter available. Kindly, try again when an employee arrives at the counter')
    elif request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']

        #taking the proper information and displaying error for wrong ones

        #checking if input email is valid
        from django.core.validators import validate_email
        try:
            validate_email(email)
        except:
            messages.info(request, 'Enter a valid email address')
            return redirect('register')

        #checking if name column is empty
        if name == '':
            messages.info(request, 'Enter a name')
            return redirect('register')
        
        #checking if phone number if numeric and has a length of 10 digits
        elif not phoneNumber.isnumeric() or len(phoneNumber) != 10:
            messages.info(request, 'Enter a valid 10 digit phone number')
            return redirect('register')
        
        #else generating otp and sending it to customer via email and text message on phone number
        else:
            phoneNumber = '+91'+phoneNumber             #using +91 by default, so it will only work for indian number
            #random 6 digit number generation for otp
            otpNum = ''
            for i in range(6):
                otpNum += str(random.randint(0, 9))
            try:
                data = userData(name = name, email = email, phoneNumber = phoneNumber, otp = otpNum)
                data.save()

                # #E-MAIL
                # rec_email = email
                # message = "Dear {}, OTP to book your position in queue is {}. Do not share it with anyone.".format(name, otpNum)
                # server = smtplib.SMTP('smtp.gmail.com', 587)
                # server.starttls()
                # server.login(sender_email, password)
                # server.sendmail(sender_email, rec_email, message)

                # #PHONE
                # client = Client(account_sid, auth_token)
                # msg = client.messages.create(
                #     body = f"Dear {name}, OTP to book your position in queue is {otpNum}. Do not share it with anyone.",
                #     from_ = twilio_phone,
                #     to = phoneNumber
                # )

                return redirect('otp', phoneNumber)
            except:
                #same phone number can't be registered again, its unique
                messages.info(request, 'This Phone Number is already registered')
                return redirect('register')

    else:
        return render(request, 'register.html')

#otp verification page
def otp(request, phoneNumber):
    d = userData.objects.get(phoneNumber = phoneNumber)
    if request.method == 'POST':
        input_otp = request.POST['input_otp']
        if input_otp == d.otp:
            #Assigning counter with smallest queue
            global counters
            global uid

            #incrementing token number
            uid += 1
            #smallest queue
            temp = min(counters.values())      
            #counter(s) of that queue (more than one queue have same number of people)                         
            res = [key for key in counters if counters[key] == temp]  
            #assigning one of the counters with smallest queue  
            d.counter = res[0]   
            #position of customer                                       
            d.pos = temp + 1
            #token number of customer
            d.token = uid
            #saving data
            d.save()
            #adding one customer to the counters dictionary
            counters[res[0]] += 1                                       

            # #PHONE
            # client = Client(account_sid, auth_token)
            # msg = client.messages.create(
            #     body = f"Dear {d.name}, your Token number is {uid}.",
            #     from_ = twilio_phone,
            #     to = phoneNumber
            # )

            # #E-MAIL
            # rec_email = d.email
            # message = "Dear {}, your Token number is {}.".format(d.name, uid)
            # server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.starttls()
            # server.login(sender_email, password)
            # server.sendmail(sender_email, rec_email, message)

            return redirect('queue details')
        else:
            messages.info(request, 'Invalid OTP')
            return redirect('otp', phoneNumber)
    else:
        return render(request, 'otp.html', {'phoneNumber' : phoneNumber})

#customer can check their counter number and position in queue using token number here
#Since the queue is dynamic, the counter number might change.
def view_queue(request):
    if not counters:
        return HttpResponse('There is no counter available. Kindly, try again when an employee arrives at the counter')
    elif request.GET.get('token'):
        token = request.GET['token']
        try:
            d = userData.objects.get(token = token)
            return render(request, 'view_queue.html', {'counter_num': d.counter, 'pos': d.pos})
        except:
            messages.info(request, 'Token number not found')
            return redirect('queue details')
        
    else:
        return render(request, 'view_queue.html', {'counter_num': "", 'pos': ""})

#employee login
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password) 
        if user is not None:
            auth.login(request, user)
            return redirect('selectCounter')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

#employee logout
def logout(request):
    global counters
    user = request.user
    old_counter = user.employee.counterNumber
    if old_counter in counters:
        counters.pop(old_counter)
        availableCounters.append(old_counter)

    #if the queue is empty before logging out, it would cause an error because of the following query. That's why I used try-except here.
    try:
        current = userData.objects.get(counter = old_counter, pos = 0)
        current.delete()
    except:
        pass

    user.employee.counterNumber = 0
    user.employee.save()

    #In case the employee had customers at the counter before log out.
   
    #If every employee logs out, all the user(customer) data will be deleted.
    if counters == {}:
        userData.objects.all().delete()
    
    #Reassigning new counter (smallest queue) to customers who were assigned the old_counter (the counter which employee had before logging out).
    else:
        new = userData.objects.filter(counter = old_counter)
        for customer in new:
            temp = min(counters.values())                               #smallest queue
            res = [key for key in counters if counters[key] == temp]    #counter(s) of that queue
            customer.counter = res[0]
            customer.pos = temp + 1
            customer.save()
            counters[res[0]] += 1

    auth.logout(request)
    return redirect('login')

#Employee controls page
def employee(request):  #admin cannot access this website
    if request.user.is_authenticated and request.user.username != 'admin':
        global counters
        n = request.user.employee.counterNumber
        if n <= 0:
            return redirect('selectCounter')
        elif 'next' in request.POST:

            #Dynamic queue: whenever the 'next customer' button is clicked by an employee, the queues are rearranged accordingly
            #Consider there are 2 counters, one counter attended people faster than the other. Hence, 1st counter has 2 people and 2nd counter has 6 people in it.
            #So, we can transfer 2 people from 2nd counter to 1st counter to balance it out. But the question is which 2 out of those 6 people.
            #If we take the last 2, it would be easier to implement but unfair to the ones who came before them. So, the algorithm will work in the following way:
            #The 4th and 5th person of 2nd queue will be assigned 3rd and 4th position of 1st counter and the 6th person of counter 2 will naturally get the 4th position of counter 2.
            while max(counters.values()) > min(counters.values()) + 1:
                smallest_queue = min(counters.values())                                 #smallest queue
                largest_queue = max(counters.values())                                  #largest queue
                small = [key for key in counters if counters[key] == smallest_queue]    #counter(s) of smallest queue
                large = [key for key in counters if counters[key] == largest_queue]     #counter(s) of largest queue
                small_counter = small[0]                                                #counter of smallest queue
                large_counter = large[0]                                                #counter of largest queue
                customer = userData.objects.get(counter = large_counter, pos = smallest_queue + 2)
                customer.counter = small_counter
                customer.pos = smallest_queue + 1
                customer.save()
                counters[large_counter] -= 1
                counters[small_counter] += 1

                #if the person removed from large_counter was at last position
                try:    
                    data = userData.objects.filter(counter = large_counter, pos__gt = smallest_queue + 2)   #__gt means greater than
                    for i in data:
                        i.pos -= 1
                        i.save()
                except:
                    pass
            
            #next customer button is clicked, so decreasing the number of people in that queue by 1
            if counters[n] > 0:
                counters[n] -= 1

            #Decrement the positions of customers by 1, and delete their data if the position is -1.
            data = userData.objects.filter(counter = n)
            for i in data:
                i.pos -= 1
                i.save()
                if i.pos < 0:
                    i.delete()

        #calling the customer to counter when its their turn
        try:
            d = userData.objects.get(pos = 0, counter = n)

            # #PHONE
            # client = Client(account_sid, auth_token)
            # msg = client.messages.create(
            #     body = f"Dear {d.name}, it's your turn now. Kindly, arrive at counter number {d.counter}.",
            #     from_ = twilio_phone,
            #     to = str(d.phoneNumber)
            # )
           
            # #E-MAIL
            # rec_email = d.email
            # message = "Dear {}, it's your turn now. Kindly, arrive at counter number {}.".format(d.name, d.counter)
            # server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.starttls()
            # server.login(sender_email, password)
            # server.sendmail(sender_email, rec_email, message)

            return render(request, 'employee.html', {'name': d.name, 'token': d.token, 'counter': n})
        except:
            messages.info(request, 'The queue is empty. Press "next customer" button when a customer arrives.')
            return render(request, 'employee.html', {'name': '', 'token': '', 'counter': n})
    else:
        return redirect('login')

#Employee select counter page
def selectCounter(request):
    if request.user.is_authenticated and request.user.username != 'admin':
        if request.method == 'POST':
            old_counter = int(request.user.employee.counterNumber)
            new_counter = int(request.POST['counter'])

            #if more than one employee opened up this page and one selected a counter, it wouldn't be removed from the page until the page is reloaded
            #So if, by chance, the other employee selects the already selected counter, page would reload and the selected counter would be removed.
            try:
                availableCounters.remove(new_counter)
            except:
                return render(request, 'selectCounter.html', {'availableCounters': availableCounters})

            global counters
            counters[new_counter] = 0

            #if the employee is changing counter (wouldn't work if the employee just logged in because there is no old_counter i.e. old_counter = 0)
            if old_counter in counters:
                counters.pop(old_counter)
                availableCounters.append(old_counter)

                #removing the one with pos=0 (the customer details which were displayed on the employee's screen before different counter was selected, if there was one)
                try:
                    current = userData.objects.get(counter = old_counter, pos = 0)
                    current.delete()
                except:
                    pass
                
                #reassigning new counter (smallest queue) to customers who were assigned the old_counter 
                new = userData.objects.filter(counter = old_counter).order_by('pos')
                for customer in new:
                    temp = min(counters.values())                               #smallest queue
                    res = [key for key in counters if counters[key] == temp]    #counter(s) of that queue
                    customer.counter = res[0]
                    customer.pos = temp + 1
                    customer.save()
                    counters[res[0]] += 1                                       #adding one customer to the counter

            #sorting so that it gets displayed in ascending order
            availableCounters.sort()

            #assigning counter
            user = request.user
            user.employee.counterNumber = new_counter
            user.employee.save()
            return redirect('employee')
        else:
            return render(request, 'selectCounter.html', {'availableCounters': availableCounters})
    else:
        return redirect('login')