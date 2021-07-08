const config = require('./default.conf');

config.clearDb = true;
config.tests = './Scenarios/Sanity/v2_test.js',

exports.config = config;