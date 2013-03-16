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
			    console.debug('onMessage: ' + msg.data);
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
	}