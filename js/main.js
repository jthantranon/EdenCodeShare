$(document).ready(function(){
	
	function cb(msg){
		console.debug(msg);
	};
	
	alert('hello');
	
	$.getJSON('/cic/immigration',function(data){
		cb(data);
	});
	
	
});