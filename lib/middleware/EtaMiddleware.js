const fs = require('fs');
const path = require('path');
const eta = require('eta');
const Logger = require('../util/Logger');

module.exports = async (app) => {
    Logger.info('Reading Eta Views...');

    app.engine('eta', eta.renderFile);
    app.set('view engine', 'eta');
    app.set('views', './views');

    // Load all files as views.
    let FILE_SPACE = (function read (dir, split = '') {
        let arr = [];
        let files = fs.readdirSync(dir);

        for (let file of files) {
            file = path.join(dir, file);
            let stats = fs.lstatSync(file);

            if (stats.isDirectory()) {
                arr = [...arr, ...read(file)];
            } else arr.push(file);
        }

        return arr.map(a => a.slice(split.length, a.length));
    })(path.join(__dirname, '/../../views'), path.join(__dirname, '/../../views'));

    app.get('/', (req, res) => res.render('home', {
        title: 'home'
    }));

    app.get('*', (req, res, next) => {
        let file = FILE_SPACE.find(f => {
            f = f.replace(/\\/g, '/')
                .replace(/\.eta/g, '');

            if (req.path === f) return true;
        });

        if (file) {
            file = file.replace(/\\/g, '/')
                .replace(/\.eta/g, '');

            if (file.startsWith('/.'))
                return next(); // ignore files with .

            return res.status(200).render(file.slice(1), {
                title: file.slice(1)
            });
        } else {
            // do nothing, let our 404 handler handle the rest.
            next();
        }
    });

    Logger.info(`Successfully setup render engine.`);
};