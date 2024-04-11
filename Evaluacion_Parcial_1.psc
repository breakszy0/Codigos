Algoritmo Evaluacion_Parcial_1
	//declarar variables
	Definir num1, tabla, resultado, num2 Como Entero;
	Definir op Como Entero;
	Definir Nota1, Nota2, Nota3, Promedio Como Real;
	//datos de entrada
	op <- 1;
	Mientras op <> 3 hacer
		Escribir "Elige una opcion del (1,3)";
		Escribir "1. Tabla de multiplicar";
		Escribir "2. Sacar Promedio";
		Escribir "3. Salir del programa";
		Leer op;
	//datos de entrada
	si op = 1 Entonces
	Escribir "Ingresa numero que quiera multiplicar";
	Leer tabla;
	Escribir "Ingresa numero a que desea llegar ";
	Leer num1;
	//proceso a realizar
	Para num2<-0 Hasta num1 Con Paso 1 Hacer
		resultado = tabla * num2;
		Escribir tabla, " X ", num2, " = ", resultado;
		op =3;
	FinPara
FinSi
    //datos de entrada
si op = 2 Entonces
	Escribir "Escriba las 3 notas";
	Leer Nota1,Nota2,Nota3;
	Promedio <- (Nota1+Nota2+Nota3)/3;
	Escribir "El promedio de las tres notas es: ",Promedio;
	//Proceso a realizar
	si Promedio >= 4.0 Entonces
		Escribir "Felicidades aprovaste";
	SiNo
		si Promedio <= 4.0 Entonces
			Escribir "Lo siento Reprovaste el ramo";
			op = 3;
		FinSi
		si op = 3 Entonces
			Escribir "Saliendo del programa";
			Esperar 2 Segundos;;
		FinSi
	FinSi
FinSi
FinMientras
FinAlgoritmo
