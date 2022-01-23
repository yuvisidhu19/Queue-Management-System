# QMS (Queue Management System)
This project is aimed to optimize the current queue system being used in retail
stores, fast food restaurants and other institutions where long queues are present.
Instead of standing in long queues, the software attempts to provide a way by which
the customer can book their place in the queue and can estimate the expected
duration of his turn while being in a comfortable place. The project is built as a
website. The user can use their mobile phone to scan a QR code or write the website
manually and be redirected to a webpage which will be used to register the user into
the queue and provide them with a token number. A confirmation of their registration will also
be sent to their mobile number as SMS and their email address. Following
registration, the user will be sent to a webpage where they can check their position and counter number from token number. 
The user will also be notified through SMS and email when its their turn.

# Customer side
The software is able to perform the following operations:
1. Register user: The software is able to register user by asking their name, phone number
and email address. The user will receive an OTP on their phone via SMS and email.
OTP can minimize the risk of fraudulent login attempts.

2. Provide token number: It provides the customer with a unique token number that distinguishes
one record from all others. The token number starts with one and increments by one.

3. Assign counter: It can assign user a counter with the smallest queue,
given there are more than one counter present at the location.

4. Check queue status: The software provides a way for user to check their assigned counter number and position in queue.

5. Notify turn: The software is able to notify the user when it’s their turn to reach
the assigned counter.

# Working
Index page: User can access main page by scanning the QR code assigned to the hosted website.
![index](https://user-images.githubusercontent.com/67970877/150690882-bc540f4e-52d0-409a-9577-6f45d40e7f88.PNG)

Registration page: This page will only submit if there are no blank columns, the email is of valid format and the phone number is 10 digit (after +91).

![register](https://user-images.githubusercontent.com/67970877/150690983-549f507d-5345-4b7e-8ec1-e2b249d184bb.PNG)

OTP page: The otp is notified through SMS and email. The registration will be complete if the otp is correct and a counter number with smallest queue will be assigned to the customer. 

![otp](https://user-images.githubusercontent.com/67970877/150690278-7eba1a13-1cbe-4837-aa11-3a07c30b3542.PNG)

Queue details page: Customer can check their assigned counter number and position in queue by inputting their token number.

![view queue](https://user-images.githubusercontent.com/67970877/150691132-efbd614e-c5bb-434d-84e8-0d8a3088e7f4.PNG)

SMS
![phone](https://user-images.githubusercontent.com/67970877/150690633-843b34e0-3b34-4ddc-85f9-00b943c64704.jpeg)

Email
![email](https://user-images.githubusercontent.com/67970877/150690637-2958e310-cf39-4c65-aaf5-0cfe07c8f316.PNG)


# Employee side
1. Login: The employees can login using their username and password.

2. Select counter: The software allows the employees to select a counter that is free. An employee can only have one unique counter at a time.

3. Customer control: The employees can call-in the customer in the first position of queue to their counter. 

4. Logout: Employees can logout and leave anytime they want.

# Manager/Admin side
1. Login: The admin can login using username and password.

2. Select total counters: The admin has the power to change the total number of counters available for employees to choose.

3. Add/remove employees: The admin can add new employees and they can create a new username and password using the admin portal. The admin can also remove any employee.

4. Logout: The admin an logout anytime.

P.S.: Admin has a lot of other permissions too but it is advised not to use them to avoid any errors in QMS. For eg, deleting a customer's data, changing employee's counter number, etc.
