Proceso Censo_Personas
    Definir N, Q, i, x, vivos, minEdad, maxEdad, edad como Entero
    
    Escribir "Ingresa la cantidad de personas (N) y la cantidad de preguntas (Q):"
    Leer N
    Leer Q
    
    Dimension nacimiento[N]
    Dimension fallecimiento[N]
    
    Escribir "Ingresa los a�os de nacimiento y fallecimiento para cada persona:"
    Para i <- 1 Hasta N Con Paso 1 Hacer
        Escribir "Persona ", i, ":"
        Leer nacimiento[i]
        Leer fallecimiento[i]
    FinPara
    
    Escribir "Ingresa los a�os de las preguntas, uno por l�nea:"
    Para j <- 1 Hasta Q Con Paso 1 Hacer
        Leer x
        
        vivos <- 0
        minEdad <- 1000000000
        maxEdad <- -1
        
        Para i <- 1 Hasta N Con Paso 1 Hacer
            Si nacimiento[i] <= x Y fallecimiento[i] >= x Entonces
                vivos <- vivos + 1
                edad <- x - nacimiento[i]
                Si edad < minEdad Entonces
                    minEdad <- edad
                FinSi
                Si edad > maxEdad Entonces
                    maxEdad <- edad
                FinSi
            FinSi
        FinPara
        
        Si vivos = 0 Entonces
            Escribir "En el a�o", x, ": ", 0, " personas vivas, edad m�nima: -", ", edad m�xima: -"
        Sino
            Escribir "En el a�o", x, ": ", vivos, " personas vivas, edad m�nima: ", minEdad, ", edad m�xima: ", maxEdad
        FinSi
    FinPara
FinProceso
