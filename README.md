# :rice_ball: Steps to Run Everything Correctly


1. Check your Ubuntu version: All steps have been tested on Ubuntu 24.04.1 LTS.
2. Set your user and password: These are your own decisions. For example purposes, we use user: ruben and password: password33.
3. Validate your IPs: The IPs provided in the examples are placeholders and won’t work. Check your IP using ifconfig (Linux) or ipconfig (Windows).
4. Update Python API scripts: The Python script for fetching data from the Binance API might stop working if API endpoints change. Always refer to the latest API documentation.
5. Use the latest DBeaver version: At the time of writing, we are using version 24.3.1.
6. PostgreSQL and Power BI SSL settings: In some environments, PostgreSQL may not connect to Power BI due to SSL restrictions. If you are in a secure environment, you can disable SSL by changing ssl = off in the postgresql.conf file.

If you have any questions about the process, feel free to contact me at rubengarciaolivas@gmail.com
