// Учебная аудитория - b = 0
// Вход только для преподавателей - b = 1
// Служебное помещение - b = 2
// Лифты - b = 3
// Коворкинги - b = 4
// Туалеты - b = 5


function fun(number, b){
	if (b == 0) var tip = "Учебная аудитория № ";
	
	if (b == 1)	var tip = "Вход только для преподавателей № ";
	
	if (b == 2) var tip = "Служебное помещение № ";
	
	if (b == 3) var tip = "Лифт № ";

	if (b == 4) var tip = "Коворкинг № ";

	if (b == 5) var tip = "Туалет № ";
	
	document.querySelector(".win1").innerHTML = tip + number;
}