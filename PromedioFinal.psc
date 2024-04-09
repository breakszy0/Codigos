Algoritmo PromedioFinal
	Definir Nota1, Nota2, Nota3, promedio Como real;
	Escribir "Escriba las 3 notas";
	Leer  Nota1, Nota2, Nota3;
	
	promedio <- (Nota1+Nota2+Nota3)/3;
	Escribir "El promedio de las tres notas es: ",promedio;
	si promedio >= 4.0 Entonces
		Escribir "Felicidades Aprovaste";
	SiNo
		si promedio<=4.0 Entonces
			
			Escribir "Lo siento aprovaste el ramo";
		FinSi
	FinSi
	

	
FinAlgoritmo
