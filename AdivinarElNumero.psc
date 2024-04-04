Algoritmo AdivinarElNumero
	Definir NumeroAdivinar, intentos , IntentosUsuario, acertado Como Entero;
	NumeroAdivinar<-Aleatorio(1,100);
	Escribir NumeroAdivinar;
	Escribir "Ingresa la cantidad de intentos que desea";
	Leer intentos;
	Mientras intentos>0 Hacer
		Escribir "Ingresa un numero";
		Leer IntentosUsuario;
		si	IntentosUsuario==NumeroAdivinar Entonces
			Escribir "Felicidades";
			intentos=0;
		SiNo
			Escribir "Incorrecto, intentado nuevamente";
			intentos=intentos-1;
		FinSi
	FinMientras
	si IntentosUsuario==NumeroAdivinar Entonces
		Escribir "Haz adivinado el numero";
	SiNo
		Escribir "No haz adivinado el numero";
	FinSi
	
FinAlgoritmo
