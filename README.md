# QMS (Queue Management System)
This project is aimed to optimize the current queue system being used in retail
stores, fast food restaurants and other institutions where long queues are present.
Instead of standing in long queues, the software attempts to provide a way by which
the customer can book their place in the queue and can estimate the expected
duration of his turn while being in a comfortable place. This project is built as a
website. The user can use their mobile phone to scan a QR code and be redirected to a webpage which will be used to register the user into
the queue and provide them with a token number. A confirmation of their registration will also
be sent to their mobile number as SMS and their email address. Following
registration, the user will be sent to a webpage where they can check their position and counter number using token number. 
The user will also be notified through SMS and email when its their turn.

Medium Article: https://medium.com/p/32a1d9bc14e2

# Dynamic queue allocation
This algorithm works whenever the 'next customer' button is clicked by any employee which rearranges the queue accordingly. It finds the largest and smallest queue and transfers some people from the largest to the smallest queue if the new position of the person would be better than before. For example, if smallest queue has 3 people in it, the algorithm will find the largest queue, say queue of length 7. The person at position (3 + 2) of largest queue will be transferred to last position (3 + 1) of smallest queue and so on. It will work till the condition is satisfied i.e. ```length of largest queue > length of smallest queue + 1```.

Consider there are 2 counters, one counter attended people faster than the other. Now, 1st counter has 2 people and 2nd counter has 6 people in it.
Hence, we can transfer 2 people from 2nd counter to 1st counter to balance it out. But the question is which 2 out of those 6 people.
If we take the last 2, it would be easier to implement but unfair to the people who came before them. 

So, the algorithm will work in the following way:

The 4th and 5th person of 2nd queue will be assigned 3rd and 4th position of 1st counter and the 6th person of counter 2 will naturally get the 4th position of counter 2.
            

# Customer side
The software is able to perform the following operations:
1. **Register user**: The software is able to register user by asking their name, phone number
and email address. The user will receive an OTP on their phone via SMS and email.
OTP can minimize the risk of fraudulent login attempts. Only one phone number can be registered at a time. 
This page can be accessed at http://127.0.0.1:8000/ if you localhost it. Twilio API is used to send SMS and smtplib module is used to send emails. I have left the variables for both as a blank string at top in views.py file. You need to fill those details if you want to use them. I have also commented the codes in the same file at lines 90-104, 142-156, 290-304. If you want to use the SMS or email privileges, you need to fill details at line 10-19 and uncomment those lines. You might also need to lower the security of your email account for it to work. Compiling twilio and smtplib codes in a seperate file is suggested before moving on to views.py file.

2. **Provide token number**: It provides the customer with a unique token number that distinguishes
one record from all others. The token number starts with one and increments by one. It will start with one again if the system is restarted.

3. **Assign counter**: It can assign user a counter with the smallest queue,
given there are more than one counter present at the location. The assigned counter number might change later as the queue is dynamic. More explaination in the #employee side.

4. **Check queue status**: The software provides a way for user to check their assigned counter number and position in queue.

5. **Notify turn**: The software is able to notify the user when it’s their turn to reach
the assigned counter through SMS and email.

## Screenshots

**Index page**: User can access main page by scanning the QR code assigned to the hosted website.

![index](https://user-images.githubusercontent.com/67970877/150690882-bc540f4e-52d0-409a-9577-6f45d40e7f88.PNG)

**Registration page**: This page will only submit if there are no blank columns, the email is of valid format and the phone number is not already registered and is of 10 digit (after +91).

![register](https://user-images.githubusercontent.com/67970877/150690983-549f507d-5345-4b7e-8ec1-e2b249d184bb.PNG)

**OTP page**: The otp is notified through SMS and email. The registration will be complete if the otp is correct and a counter number with smallest queue will be assigned to the customer. 

![otp](https://user-images.githubusercontent.com/67970877/150690278-7eba1a13-1cbe-4837-aa11-3a07c30b3542.PNG)

**Queue details page**: Customer can check their assigned counter number and position in queue by inputting their token number.

![view queue](https://user-images.githubusercontent.com/67970877/150691132-efbd614e-c5bb-434d-84e8-0d8a3088e7f4.PNG)

**SMS** (using Twilio)

![phone](https://user-images.githubusercontent.com/67970877/150690633-843b34e0-3b34-4ddc-85f9-00b943c64704.jpeg)

**Email** (using smtplib)

![email](https://user-images.githubusercontent.com/67970877/150690637-2958e310-cf39-4c65-aaf5-0cfe07c8f316.PNG)

P.S.: Frontend for customer side isn't done by me.

# Employee side
1. **Login**: The employees can login using their username and password. The customer can only register if there is atleast one employee logged in.

2. **Select counter**: The software allows the employees to select a counter that is free. An employee can only have one unique counter at a time. The employee can also change counters and the counters will be reassigned to the customers who were assigned to previous counter.

3. **Customer control**: The employees can call-in the customer in the first position of queue to their counter. 

4. **Logout**: Employees can logout and leave anytime they want. If an employee logs out and the queue assigned to his counter isn't empty, the counters will be reassigned to the people of that queue in ascending order. If all the employees logged out, all the user (customer) data will be deleted (if any).

## Screenshots
**Login page**: This website can be accessed by using '/login' after the link i.e. http://127.0.0.1:8000/login for localhost. The username and password can be set by admin.

![login](https://user-images.githubusercontent.com/67970877/150784909-f531f2a4-76d6-41c5-8422-f605cfa44aaa.PNG)

**Select counter page**: The employee can select any available counter and also change it.
![select counter](https://user-images.githubusercontent.com/67970877/150784960-42ef6272-aeda-43ed-9036-d1791b43f0f7.PNG)

**Employee page**: The employee can call-in next customer by clicking the 'next customer' button. 
![employee 1](https://user-images.githubusercontent.com/67970877/150784983-b89fc2ae-7d80-40a6-a6bc-8aeb4070f807.PNG)

When the 'next customer' button is clicked, the positions of all the people in that counter is decremented by one. Hence, the details of the person belonging to that counter with position 0 is displayed as shown below. When this button is clicked again, the position of person present at the counter will become -1 and it will get deleted.

![employee 2](https://user-images.githubusercontent.com/67970877/150784994-da7c4b31-17b5-4c47-b35b-c166721f474c.PNG)


# Manager/Admin side
1. **Login**: The admin can login using username and password which is set while making a database.

2. **Select total counters**: The admin has the power to change the total number of counters available for employees to choose.

3. **Add/remove employees**: The admin can add new employees and they can create a new username and password using the admin portal. The admin can also remove any employee.

4. **Logout**: The admin can logout anytime.

## Screenshots
**Users**: The admin can add employees and give then username and password in this section.

**User datas**: All the temporary cutomer data is stored here.

**Employees**: The counter number of employees is saved here. It is 0 by default. The column number for admin works differently. It works as the total number of counters that can be selected by employees.

![admin](https://user-images.githubusercontent.com/67970877/150790593-529322f5-3f7e-414a-80f6-149f00c49747.PNG)


Employees can be added by admin by clicking on the 'add user' button in the users section as specified by the arrow below.

![admin2](https://user-images.githubusercontent.com/67970877/150790607-4969ebb8-9835-4356-83d5-27a64f26f149.PNG)


The admin can change the total number of counters that can be selected by employees by going to the employees section and selecting the name of the admin (can be anything) as specified below. The admin mustn't tamper with any other option.

![admin3](https://user-images.githubusercontent.com/67970877/150790632-9a12289d-ee98-4ccd-822b-0cb88c4d5b0c.PNG)


As mentioned before, the column of CounterNumber for admin works as total number of counters.

![ADMIN4](https://user-images.githubusercontent.com/67970877/150790645-7c5a886f-4feb-4082-ae6b-f18cabee8e9a.png)


Example of customer data:

![admin5](https://user-images.githubusercontent.com/67970877/150790659-c0007edd-f44e-4a77-884d-cd37dfd43314.PNG)
![image](https://user-images.githubusercontent.com/67970877/150793832-453630d2-1d23-4efe-a59f-3e9d04bb1909.png)

P.S.: Admin has a lot of other permissions too but it is advised not to use them to avoid any errors in QMS. For eg, deleting a customer's data, changing employee's counter number, etc.

Note: You are required to input secret key in the settings.py file.
