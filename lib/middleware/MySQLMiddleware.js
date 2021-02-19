const fs = require('fs');
const toml = require('toml');
const mysql = require('mysql2/promise');
const Logger = require('../util/Logger');

module.exports = async (app) => {
    let config = toml.parse(fs.readFileSync(__dirname + '/../../config/mysql.toml'));
    let keys = Object.keys(config.database);
    let pools = {};
    let count = 0;

    Logger.info('Loading MySQL Pools...');

    for (let pool in keys) {
        Logger.log('Loading MySQL Pool: ' + pool);

        try {
            let connection = await mysql.createPool(config.database[pool]);
            await connection.execute(`SHOW TABLES;`).then(_ => {
                Logger.log('Successfully connected to the pool!');
                pools[pool] = connection;
            });

            count++;
        } catch (e) {
            Logger.error('Could not load MySQL pool: ' + e.message);
        }
    }

    app.use((req, res, next) => {
        req.pools = pools;
        next();
    });

    Logger.info(`Successfully connected to ${count} out of ${keys.length} pools.`);

    if (keys.length !== count)
        Logger.warn(`Look above to see whether or not any errors occurred during pool connection.`);
};