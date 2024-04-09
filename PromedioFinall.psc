Algoritmo PromedioFinal
	//
	Definir nota_1, nota_2, notaTres, promedio Como real;
	Escribir "Escriba las 3 notas";
	Leer  nota_1, nota_2,  notaTres;
	//
	promedio <- (nota_1+nota_2+notaTres)/3;
	Escribir "El promedio de las tres notas es: ",promedio;
	si promedio >= 4.0 Entonces
		Escribir "Felicidades Aprovaste";
	SiNo
		si promedio<=4.0 Entonces
			
			Escribir "Lo siento aprovaste el ramo";
		FinSi
	FinSi
	

	
FinAlgoritmo
