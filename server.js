// MODULES
const express = require('express');
const less = require('less-middleware');
const path = require('path');
const Logger = require('./lib/util/Logger');
const morgan = require('morgan');

// CONSTANTS
const PORT = 8080;

// APPLICATION //
const app = require('express')();

(async () => {
    // REQUEST LOGGER //
    app.use(morgan('dev'));

    // MIDDLEWARE //
    app.use(express.urlencoded({ extended: true }));
    app.use(express.json());

    app.use(less(path.join(__dirname, 'static', 'less'), {
        force: true,
        dest: path.join(__dirname, 'static', 'css')
    }));

    // STATIC //
    app.use(express.static(path.join(__dirname, 'static', 'css')));

    // MIDDLEWARE //
    await require('./lib/middleware/MySQLMiddleware')(app);
    Logger.empty();
    await require('./lib/middleware/RouterMiddleware')(app);
    Logger.empty();
    await require('./lib/middleware/EtaMiddleware')(app);
    Logger.empty();

    // SETTINGS //
    app.set('json-spaces', 4);
    app.disable('x-powered-by');

    // 404 ROUTE //
    app.get('*', ((req, res) => {
        res.status(404).render('.error', {
            error_name: 'Page not found...',
            error_message: 'The page you were looking for was not found.',
            title: '404'
        });
    }));

    app.listen(PORT, () => {
        Logger.info('Running server on port ' + require('chalk').bold(PORT));
        Logger.empty();

        console.log(require('chalk').italic('- All debug logging requests will be logged here. -'));
        Logger.empty();
    });
})();