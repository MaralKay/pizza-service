"use strict"

let pg = require('pg');

function postgresClientWrapper(connectionString, operation, callback) {
    let client = new pg.Client(connectionString);

    client.connect(err => {
        if (err) return callback({}, err);

        operation(client, (err, results) => {
            client.end();
            callback(err, results);
        });
    });
}

module.exports = function(pgConnectionString, query, callback){
    postgresClientWrapper(pgConnectionString, (client, wrapperCallback) => {
                
                client.query(query, (err, results) => {
                    if (err) return wrapperCallback(err, {});

                    return wrapperCallback(null, results);
                });
            }, callback);
};