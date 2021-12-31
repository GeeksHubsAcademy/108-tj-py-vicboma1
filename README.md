<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


    Considere el siguiente problema:

    Escriba un programa corto que permita pasar de un formato de tiempo establecido en 3 parámetros (horas, minutos, segundos) a un número entero en milisegundos.
    
    Los inputs de entrada se restringen de la siguiente manera :

	0 <= h <= 23
	0 <= m <= 59
	0 <= s <= 59
	
	En caso de romperse estas cláusualas, el retorno debe de ser -1.

	
    Ejemplo:

	milliseconds.apply(0,1,1) = 61000
    
	milliseconds.apply(1,1,1) = 3661000

	milliseconds.apply(24,10,10) = -1


    En la carpeta 'src/kata.py' se encuentra el fichero con 
    la definición de nuestro método vacío.
    En la carpeta 'tests/test_kata.py' se encuentra el fichero
    con la suite de test.
    
    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.

    [Test Suite]

    tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [  5%]
    tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [ 10%]
    tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 15%]
    tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 20%]
    tests/test_kata.py::Test_kata::test_apply_13 PASSED                      [ 25%]
    tests/test_kata.py::Test_kata::test_apply_14 PASSED                      [ 30%]
    tests/test_kata.py::Test_kata::test_apply_15 PASSED                      [ 35%]
    tests/test_kata.py::Test_kata::test_apply_16 PASSED                      [ 40%]
    tests/test_kata.py::Test_kata::test_apply_17 PASSED                      [ 45%]
    tests/test_kata.py::Test_kata::test_apply_18 PASSED                      [ 50%]
    tests/test_kata.py::Test_kata::test_apply_19 PASSED                      [ 55%]
    tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 60%]
    tests/test_kata.py::Test_kata::test_apply_20 PASSED                      [ 65%]
    tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 70%]
    tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 75%]
    tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 80%]
    tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 85%]
    tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 90%]
    tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 95%]
    tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]

## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
