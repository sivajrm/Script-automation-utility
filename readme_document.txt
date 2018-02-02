In this program execution,

1.I have assumed the test files to be exected as a python script that opens a Notepad as the operation for all the test files which are inputted in the console

2 And the user has to end the process by providing the file id that has to be ended. The program records the file execution ending time

And, For concurrent execution of the test files given in the step, I have used the python concurrent library for simulataneous operation

The start and the end time of the test file execution were recorded by using the Nested dictionary concepts


Can be done:

I had a global dict to record the start time and end time of the file execution, This can also be done by writing to a file, and reading from there for future usage


To execute:
>python main.py
>a.sql b.sql c.sql   \n
>c.sql
>#


