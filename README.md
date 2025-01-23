# consistentHashing
This repo contains the basic code to understand and simulate the consistent hashing algorithm.

## What it simulates

### Initial State
#### There are 5 servers (A,B,C,D,E) to start with in a server pool.

#### Each gets assigned a position on the hash ring using a Hash function (hashFn)

#### Then we bring in data to store, which gets assigned a position on the hash ring using the same function (hashFn) as above.

#### The first server to the right of data's hash position gets assigned this data.

#### All the subsequent data is assigned a data server the same way.

### Remove a server
#### A server is removed from the server pool.

#### The data assigned to it is moved to the next adjacent available server.


### See a demo

#### Clone the repo and run the python script ConsistentHashing.py 
