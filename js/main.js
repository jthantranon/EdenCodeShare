$(document).ready(function(){
	function OpenSesh(){
		var channel;
		var handler;
		var socket;
		$.getJSON('/cic/asession', function(sesh) {
	        chantoken = sesh.Chan
			onOpen = function() {
			    console.debug('onOpen: ' + chantoken);
			};

			onClose = function() {
			    console.debug('onClose');
			};
			
			onMessage = function(msg) {
			    console.debug('onMessage: ' + msg.name);
//			    pack = JSON.parse(msg.data);
			};
			
			onError = function() {
			    console.debug('onError');
			};
			
			openChannel = function() {
			    channel = new goog.appengine.Channel(chantoken);
			    handler = {
				    'onopen': onOpen,
				    'onclose': onClose,
				    'onmessage': onMessage,
				    'onerror': onError
			    };
				socket = channel.open(handler);
				socket.onopen = onOpen;
				socket.onmessage = onMessage;
		};
			setTimeout(openChannel, 50);
		});
	};
	
	OpenSesh();
	
	function cb(msg){
		console.debug(msg);
	};
	
//	alert('hello');
	
//	$.getJSON('/cic/immigration',function(data){
//		cb(data);
//	});
	
	
});