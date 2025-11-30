# Oportunidades de mejora:

Main |:
    <w> "Secuencia de Fibonacci en música"
    
    ### Generar secuencia de Fibonacci ###
    melodia <- {}
    a <- 0
    b <- 1
    i <- 0
    
    while i < 8 |:
        ### Añadir nota correspondiente al número de Fibonacci ###
        nota <- C + a
        melodia << nota
        
        ### Siguiente número de Fibonacci ###
        temp <- a + b
        a <- b
        b <- temp
        i <- i + 1
    :|
    
    <w> "Generando partitura con" #melodia "notas"
    (:) melodia
    <w> "Secuencia completada"
:|

Secuencia de Fibonacci en música
Generando partitura con 8 notas
Secuencia completada
Partitura generada: static/outputs/temp_20251130_053901_560197.pdf
Audio generado: static/outputs/temp_20251130_053901_560197.wav


<img width="1305" height="432" alt="image" src="https://github.com/user-attachments/assets/5b85604d-107f-4d3c-a70d-a06d554893cf" />


:Hanoi n origen destino auxiliar melodia |:
    if n > 0 |:
        temp <- n - 1
        Hanoi temp origen auxiliar destino melodia

        ### Agregar nota del movimiento ###
        nota <- C + n * 2
        melodia << nota
        <w> "Mover disco" n "de" origen "a" destino

        Hanoi temp auxiliar destino origen melodia
    :|
:|
Main |:
    <w> "Torres de Hanoi con 3 discos"
    notas <- {}
    Hanoi 3 1 3 2 notas
    <w> "Generando partitura con" #notas "movimientos"
    (:) notas
:|

Mover disco 1 de 1 a 3 0 0 2 3 1 [30]
Mover disco 2 de 1 a 2 0 1 3 2 1 [30 32]
Mover disco 3 de 1 a 3 0 2 2 3 1 [30 32 34]


<img width="821" height="370" alt="image" src="https://github.com/user-attachments/assets/2b4066e8-aecc-4800-ba47-fb503ab852b7" />


Main |:
    <w> "Hello Algoritmia"
    (:) {C D E F G A B C}
:|



Hello Algoritmia
Partitura generada: static/outputs/temp_20251130_060348_557902.pdf
Audio generado: static/outputs/temp_20251130_060348_557902.wav


<img width="1016" height="274" alt="image" src="https://github.com/user-attachments/assets/6816531a-8298-4a67-92a7-4c6aed3676f0" />

Main |:
    notas <- {C D E F G}
    <w> "Notas iniciales:" notas
    <w> "Longitud:" #notas
    
    ### Añadir notas ###
    notas << A
    notas << B
    <w> "Notas finales:" notas
    
    ### Reproducir todas ###
    (:) notas
:|

Notas iniciales: [28 29 30 31 32]
Longitud: 5
Notas finales: [28 29 30 31 32 33 34]
Partitura generada: static/outputs/temp_20251130_060850_918283.pdf
Audio generado: static/outputs/temp_20251130_060850_918283.wav

<img width="1017" height="277" alt="image" src="https://github.com/user-attachments/assets/fac88331-5e73-4fcb-900e-bc8065fc5f20" />

observación: resultado esperado:
28 = E1 (Mi grave)
29 = F1 (Fa)
30 = F#1 (Fa#)
31 = G1 (Sol)
32 = G#1 (Sol#)

Después de añadir A y B (7 notas totales):

28 = E1 (Mi)
29 = F1 (Fa)
30 = F#1 (Fa#)
31 = G1 (Sol)
32 = G#1 (Sol#)
33 = A1 (La) ← añadida
34 = A#1 (La#/Sib) ← añadida


resultado obtenido: 
Do (C) - la nota redonda al inicio, debajo del pentagrama
Clave de Do en primera línea - el símbolo de clave
Re (D) - la primera nota negra
Sol (G) - la segunda nota (ovalada)
Re (D) - nota en la cuarta línea
Mi (E) - nota en el primer espacio
Fa# (F#) - nota en el espacio superior (entre 4ª y 5ª línea)
Sol (G) - nota en la segunda línea adicional superior
Re (D) - la última nota negra



___

Main |:
    <w> "Tocando una melodía"
    
    ### Frase 1 ###
    (:) {C C G G A A G}
    
    ### Frase 2 ###
    (:) {F F E E D D C}
    
    <w> "Melodía completada"
:|



output esperado: 
C  C  G  G  A  A  G

F  F  E  E  D  D  C
Tocando una melodía
Melodía completada
Partitura generada: static/outputs/temp_20251130_061802_872194.pdf
Audio generado: static/outputs/temp_20251130_061802_872194.wav
resultado obtenido: 
Analizando esta partitura en **clave de Sol**, las notas son:

1. **Do** (C) - nota redonda inicial, debajo del pentagrama
2. **Clave de Do en primera línea** - el símbolo de clave
3. **Re** (D) - primera nota negra
4. **Re** (D) - segunda nota negra
5. **La** (A) - nota en el segundo espacio
6. **La** (A) - nota en el segundo espacio
7. **Si** (B) - nota en la tercera línea
8. **Si** (B) - nota en la tercera línea
9. **La** (A) - nota en el segundo espacio
10. **Sol** (G) - nota en la segunda línea
11. **Sol** (G) - nota en la segunda línea
12. **Fa** (F) - nota ovalada en el primer espacio
13. **Fa** (F) - nota ovalada en el primer espacio
14. **Re** (D) - nota negra final

**Secuencia completa**: 
**Do - Re - Re - La - La - Si - Si - La - Sol - Sol - Fa - Fa - Re**

Esto parece ser una variación o continuación de "Twinkle, Twinkle, Little Star", pero con una secuencia diferente. La estructura sigue el patrón de notas repetidas (cada nota aparece dos veces), característico de melodías infantiles.


<img width="1297" height="283" alt="image" src="https://github.com/user-attachments/assets/eaf02107-7643-435f-96cb-a66842454ffa" />



____

Main |:
    x <- 10
    y <- 20
    suma <- x + y
    <w> "La suma de" x "y" y "es:" suma
    (:) {C E G}
:|

La suma de 10 y 20 es: 30
Partitura generada: static/outputs/temp_20251130_062248_529452.pdf
Audio generado: static/outputs/temp_20251130_062248_529452.wav


___


resultaado esperado:
✅ Coincide:

Las notas Do - Mi - Sol están presentes
Forma el acorde de Do Mayor

❌ No coincide completamente:
La imagen mostraba 4 notas: Do - Mi - Sol - Do (con la octava repetida)
El código solo genera 3 notas: Do - Mi - Sol (sin la octava)
Conclusión:
El código genera el acorde de Do Mayor básico (tríada), mientras que la partitura de la imagen mostraba el arpegio completo con la octava.
Para que coincida exactamente con la imagen, el código debería ser:
(:) {C E G C}


resultado obtenido : 
Identificación de las notas (en clave de Sol):

Clave de Do en primera línea - símbolo de clave
Do (C) - la nota redonda en el tercer espacio
Mi (E) - la nota negra en la primera línea
Sol (G) - la nota negra en la segunda línea
Do (C) - la nota negra final en el tercer espacio

Secuencia: Do - Mi - Sol - Do
Análisis armónico:
Acorde de Do Mayor (C Major) en forma de arpegio
Este es un ejemplo perfecto de un arpegio de tríada mayor que contiene:

Fundamental (tónica): Do (C) - 1ª
Tercera mayor: Mi (E) - 3ª
Quinta justa: Sol (G) - 5ª
Octava: Do (C) - 8ª (repetición de la tónica una octava arriba)


<img width="426" height="236" alt="image" src="https://github.com/user-attachments/assets/80b7b905-1e33-4d96-b815-b533ece9ce16" />


