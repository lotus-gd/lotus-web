const router = require('express').Router();

router.get('/', (req, res) => {
    res.status(200).json({
        code: 200,
        message: 'hi!'
    });
});

module.exports = router;