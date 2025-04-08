
    Algoritmo MenuRiego
        Definir opcion Como Entero;
        Definir humedad Como Real;
        Definir humedad_umbral Como Entero;
        Definir historial Como Lista;
        
        humedad_umbral <- 40;
        
        Repetir
            Escribir "---- MENÚ ----";
            Escribir "1. Medir humedad";
            Escribir "2. Ajustar umbral de humedad";
            Escribir "3. Ver historial de humedad";
            Escribir "4. Salir";
            Escribir "Elija una opción:";
            Leer opcion;
            
            Si opcion = 1 Entonces
                humedad <- Aleatorio(40, 100);
                historial.Agregar(humedad)
                Escribir "Humedad actual: ", humedad, "%";
                Si humedad < humedad_umbral Entonces
                    Escribir "Humedad baja. Activando riego...";
                Sino
                    Escribir "Humedad suficiente. No se activa riego.";
                FinSi
            FinSi
            
            Si opcion = 2 Entonces
                Escribir "Ingrese el nuevo umbral de humedad:";
                Leer humedad_umbral;
                Escribir "Nuevo umbral establecido en ", humedad_umbral, "%";
            FinSi
            
            Si opcion = 3 Entonces
                Escribir "Historial de humedad: ", historial;
            FinSi
            
            Si opcion <> 1 Y opcion <> 2 Y opcion <> 3 Y opcion <> 4 Entonces
                Escribir "Opción no válida.";
            FinSi
            
        Hasta Que opcion = 4
        
        Escribir "Fin del programa.";
        
FinAlgoritmo
