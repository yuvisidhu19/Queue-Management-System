# QMS (Queue Management System)
This project is aimed to optimize the current queue system being used in retail
stores, fast food restaurants and other institutions where long queues are present.
Instead of standing in long queues, the software attempts to provide a way by which
the customer can book their place in the queue and can estimate the expected
duration of his turn while being in a comfortable place. The project will be built as a
website. The user can use their mobile phone to scan a QR code or write the website
manually and be redirected to a webpage which will be used to register the user into
the queue and provide them with a UID. A confirmation of their registration will also
be sent to their mobile number as SMS and their email address. Following
registration, the user will be sent to a webpage that will display the number of people
in line ahead of them, and a rough waiting time can be calculated using this
information. In case of any technical difficulties, the operator will be able to notify the
users through the website.
The software must be able to perform the following operations:
Register user: It must be able to register user by asking their name, phone number
and email address. The user will receive an OTP on their phone via SMS and email.
OTP’s will minimize the risk of fraudulent login attempts.
Provide UID: It must be able to provide the customer with a UID that distinguishes
one record from all others. It enables the record to be referred in the Summon Index
without causing confusion or accidental overwriting of other records.
Assign counter: It must be able to assign user a counter with the smallest queue,
given there are more than one counter present at the location.
Check queue status: The software must be able to check the queue status and
determine the number of people standing before user in the queue and display it on
the website.
Notify turn: The software must be able to notify the user when it’s their turn to reach
the assigned counter.
