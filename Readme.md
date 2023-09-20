https://codingchallenges.fyi/challenges/intro

1. wc Tool
   
   ```
   alias wc="python3 ccwc.py"
   wc test.txt
   cat test.txt | wc 
   wc -l/-c/-w/-m test.txt
   ```

2. Json Parser

    ```
    python3 test/valid.json
    ```


5. Load Balancer
  
   ```  
   1. starting 4 servers 

   python3 -m http.server --bind 127.0.0.1 8001 --directory www
   python3 -m http.server --bind 127.0.0.1 8002 --directory www2
   python3 -m http.server --bind 127.0.0.1 8003 --directory www3
   python3 -m http.server --bind 127.0.0.1 8004 --directory www4

   2. start lb server

   python3 lb.py

   3. curl http://localhost:1111/
   
   4. start a health check 
   python3 healthcheck.py --tries <int; default=10>
   ```
   
6. 
