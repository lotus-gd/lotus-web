const fs = require('fs');
const path = require('path');
const Logger = require('../util/Logger');

module.exports = (app) => {
    let routerPath = __dirname + '/../../routers';

    Logger.info('Loading routers...');

    (function read (dirPath, router = '') {
        let files = fs.readdirSync(dirPath);
        for (let file of files) {
            let stat = fs.lstatSync(path.join(dirPath, file));

            if (stat.isDirectory()) {
                read(path.join(dirPath, file), router + '/' + file);
            } else {
                // file
                let p = path.parse(dirPath);
                let route = `${router}/${file.replace(/\..*$/, '')}`;

                if (p.base === file.replace(/\..*$/, ''))
                    route = `${router}`;

                app.use(route, require(path.join(dirPath, file)));
            }
        }
    })(routerPath);

    Logger.info('Successfully setup router engine.');
};