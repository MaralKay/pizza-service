# postgres-client
A simple lightweight async postgres client library wrapper.

##Installation
```
npm install --save postgres-client
```

##Configuration
The expected configuration connection string should be in the following format.

```
{"user":"postgres-admin", "database":"xxxx", "host": "xxxx", "port": 5432, "password": "xxx"}
```

##Usage
```
let pgClient = require("postgres-client");
pgClient(process.env.CONNECTION_CONFIG, "select * from users", (error, results) =>{})
```