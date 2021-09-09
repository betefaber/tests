const env = {
    
    // // Docker-compose v1 and v2
    dojot_host: process.env.DOJOT_HOST || 'http://localhost:8000',
    mqtt_host: process.env.MQTT_HOST || 'tcp://localhost:1883',

    dojot_host_v2: process.env.DOJOT_HOST || 'http://localhost:8000/v2#/login',

    //K8s v1 and v2
    // dojot_host: process.env.DOJOT_HOST || 'http://10.50.4.46',
    // mqtt_host: process.env.MQTT_HOST || 'tcp://10.50.4.46',

    // dojot_host_v2: process.env.DOJOT_HOST || 'http://10.50.4.46/v2#/login',
    // // mqtt_host: process.env.MQTT_HOST || 'tcp://10.50.4.46',
};

module.exports = env;
