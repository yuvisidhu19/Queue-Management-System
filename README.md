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

The software is able to perform the following operations:

Customer side:
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

Employee side:
1. Login: The employees can login using their username and password.

2. Select counter: The software allows the employees to select a counter that is free. An employee can only have one unique counter at a time.

3. Customer control: The employees can call-in the customer in the first position of queue to their counter. 

4. Logout: Employees can logout and leave anytime they want.

Manager/Admin side:
1. Login: The admin can login using username and password.

2. Select total counters: The admin has the power to change the total number of counters available for employees to choose.

3. Add/remove employees: The admin can add new employees and they can create a new username and password using the admin portal. The admin can also remove any employee.

4. Logout: The admin an logout anytime.

P.S.: Admin has a lot of other permissions too but it is advised not to use them to avoid any errors in QMS. For eg, deleting a customer's data, changing employee's counter number, etc.
