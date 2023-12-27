const ROOM_TYPE_LEARNING = 0;
const ROOM_TYPE_TEACHERS = 1;
const ROOM_TYPE_SERVICE = 2;
const ROOM_TYPE_LIFT = 3;
const ROOM_TYPE_COWORKING = 4;
const ROOM_TYPE_TOILET = 5;

async function schedule_get(room_type, number){
    let schedule;
    let links = new Map();
    links.set(ROOM_TYPE_LEARNING, 'http://127.0.0.1:5000/schedule?type=learning&number=');

    if (room_type == ROOM_TYPE_LEARNING){
        const temp = await fetch(links.get(ROOM_TYPE_LEARNING) + number)
        schedule = await temp.json();
	    return await schedule;
    }

}


async function work_with_window(number, room_type){
	if (room_type == ROOM_TYPE_LEARNING){
	 var tip = "Учебная аудитория № ";
	 var schedule = await schedule_get(room_type, number);
	 console.log(schedule[0]);

	}
	if (room_type == ROOM_TYPE_TEACHERS){
		var tip = "Вход только для преподавателей № ";
	}
	if (room_type == ROOM_TYPE_SERVICE){
	 var tip = "Служебное помещение № ";
	 }
	
	if (room_type == ROOM_TYPE_LIFT){
	 var tip = "Лифт № ";
    }
	if (room_type == ROOM_TYPE_COWORKING){
	 var tip = "Коворкинг № ";
    }
	if (room_type == ROOM_TYPE_TOILET){
	 var tip = "Туалет № ";
	}
	document.querySelector(".win1").innerHTML = tip + number;
}