// Socket variable to access connection on localhost:por
var socket = io.connect('http>//'+document.domain+':'+location.port);

// Subscribe to 'connect' event and print a log to know we connected succesfully
socket.on( 'connect', () => {
    console.log( 'Websocket Connected' );
});

// Simple log structure class object definition
class Log {
    constructor(t, l, f) {
        this.temp = t;
        this.level = l;
        this.flow = f;
    }
}
// Array of logs to simulate plant readings
var logs = [];
for (let i = 0; i < 15; i++) {
    logs.push( new Log(
        Math.random() * 50,
        Math.random() * 5,
        Math.random() * 100
    ));
}

obs = Rx.Observable.from(logs);

function sendLogs() {
    obs.subscribe( (data) => {
        console.log(data);
        socket.emit( 'log', data );
    } )
}