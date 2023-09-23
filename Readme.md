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

3. Compression (Yet to be completely implemented)

4. Cut Tool 
   ```
   alias cut="python3 main.py"

   - cut -f1 sample.tsv -> proper value
   - cut -f1 -d, fourchords.csv | head -n5 -> proper value
   - cut -f20 sample.tsv -> blank
   - cut -f2.0 sample.tsv -> err msg

   - cut -d, -f"1 2" fourchords.csv | head -n5
   - cut -f2 -d, fourchords.csv | uniq | wc -l

   This throws an err
   - tail -n5 fourchords.csv | cut -d, -f"1 2"


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


   curl --parallel --parallel-immediate --parallel-max 3 --config test.txt
   ```
   
   Here are some other areas you could explore if you wish to take the project further and dig deeper into what makes a load balancer useful and how it works:

   - [ ] Read up about HTTP keep-alive and how it is used to reuse back end connections until the timeout expires.
   - [x] Add some Logging - think about the kinds of things that would be useful for a developer, i.e. which server did a client’s request go to, how long did the backend server take to process the request and so on.
   - [ ] Build some automated tests that stand up the backend servers, a load balancer and a few clients. Check the load balancer can handle multiple clients at the same time.
   - [ ] If you opted for threads, try converting it to use an async framework - or vice versa.

6. 
