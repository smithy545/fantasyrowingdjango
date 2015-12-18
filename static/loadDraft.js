function convertHeader(key){
	if(key == 'ranking'){
		return 'Ranking';
	} else if(key == 'first_name') {
		return '<td>First Name</td>';
	} else if(key == 'last_name') {
		return '<td>Last Name</td>';
	} else if(key == 'weight') {
		return '<td>Weight</td>';
	} else if(key == 'hometown') {
		return '<td>Hometown</td>';
	} else if(key == 'age') {
		return '';
	} else if(key == 'school') {
		return '<td>School</td>';
	} else if(key == 'height') {
		return '<td>Height</td>';
	} else if(key == 'year') {
		return '<td>Year</td>';
	} else if(key == 'major') {
		return '';
	} else if(key == 'high_school') {
		return '<td>High School</td>';
	} else if(key == 'side') {
		return '';
	}
}

function isValidKey(key) {
	var validKeys = ['ranking', 'first_name', 'last_name', 'weight', 'hometown', 'school', 'height', 'year', 'high_school'];
	if(validKeys.indexOf(key) > -1) {
		return true;
	}
	return false;
}
function validField(key) {
	if(key == 'age' || key == 'major' || key == 'side')
		return false;
	return true;
}
function toFeetInches(inches) {
	if(typeof inches == "number")
		return parseInt(inches / 12) + "'" + inches % 12 + '"';
	return inches;
}
function displayAthletes(athletes) {
	document.getElementById("draft-content").innerHTML = "<table id='athlete_table'></table>";
	table = document.getElementById('athlete_table');
	var row = table.insertRow();
	for(var key in athletes[0]["fields"]){
		if(isValidKey(key)) {
			cell = row.insertCell();
			cell.innerHTML = convertHeader(key);
		}
	}
	for(var a in athletes) {
		row = table.insertRow();	
		for(var key in athletes[a]["fields"]) {
			if(validField(key)) {
				if(key == 'height')
					athletes[a]["fields"][key] = toFeetInches(athletes[a]["fields"][key]);
				else if(key == 'weight' && athletes[a]["fields"][key])
					athletes[a]["fields"][key] = athletes[a]["fields"][key]+' lbs';
				cell = row.insertCell();
				cell.innerHTML = athletes[a]["fields"][key];
			}
		}
	}
}

function displayPlayers(players) {
	document.getElementById("player-turn").innerHTML = "<div id='player_table'></div>";
	var div = document.getElementById('player_table');
	for(a in players) {
		var x = document.createElement("div");
		x.setAttribute("id","player_div");
		x.appendChild(document.createTextNode(players[a]["fields"]["name"]));
		div.appendChild(x);
	}
}

globalStore = {}

$(document).ready(function() {
$.when(
	$.getJSON('\/draft\/getathletes', function(data){globalStore.athletes=data;}),
	$.getJSON('\/draft\/getplayers', function(data){globalStore.players=data;})
).then(function() {
	displayAthletes(globalStore.athletes);
	displayPlayers(globalStore.players);
});
});
