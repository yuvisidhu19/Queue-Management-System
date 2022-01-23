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
