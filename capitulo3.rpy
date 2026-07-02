# CAPÍTULO 3: 
label capitulo3:
    #CAMPO del abuelo cortando la leña
    scene cor
    
   
    "Capitulo3"
    "(Han pasado un par de días viviendo con tu abuelo.)"
    
    "De a poco te va enseñando la vida de campo. Es dura. Tu cuerpo está adolorido, las manos llenas de ampollas y la espalda te duele cada mañana… pero las risas con él no faltan. Poco a poco sientes que tu ánimo va mejorando."
    
    "Es mediodía. El sol pega fuerte."
    
    "Estás cortando leña junto a tu abuelo. Él toma chicha de un vaso de plástico mientras tú tomas una Coca-Cola."
    
    abu "Pégale sin miedo, hombre… Imagínate que es el weón que te quitó la mina."
    
    tu "Jajaja…"
    
    "(Te ríes, aunque la broma te llega un poco al corazón. Aun así, te sientes feliz estando con él.)"
    
    "(Le pegas al tronco con más fuerza. El hacha suena limpia y hace un corte perfecto.)"
    
    abu "(sonriendo orgulloso) ¡Ese es! ¡Así se hace, mi nieto!"
    play sound terr volume 0.85

    "(De pronto, la tierra tiembla bajo tus pies. Es breve, pero lo suficientemente fuerte como para que se te erice la piel.)"
    
    tu "¿Qué fue eso, abuelo?"
    
    abu "(secándose el sudor con un pañuelo viejo, mirando hacia el volcán) Mmm… a veces tiembla lo típico de este país…"
    
    tu "¿Estás seguro?"
    
    abu "Sehh… tú calmado nomás. ¿Qué hora es esta cuestión?"
    
    tu "Como un poco pasado las 2."
    
    abu "Naaa… bueno… Vamo’ pa’ la casa mejor. Además estoy con la tripa seca, no he comido nada en todo el día."
    
    tu "Ya, vamos entonces."



    # escena CASA DEL ABUELO
    scene com
    "(Llegan a la casa. El abuelo se deja caer pesadamente en su silla de madera.)"


    abu "(agotado) Ahhh… jue uta que tengo hambre y frío."


    abu "Porque no te hacís el fuego o pelai las verduras pa’ ayudarme un poco."

    
    # QUINTA DECISION no afecta la historia 
    menu:
        "¿Qué haces para ayudar?"


        "Pelar las verduras":
            $ tarea = "verduras"
            
            scene ali
            "(Buscas unas papas, cebollas y zanahorias y empiezas a pelarlas en la mesa.)"


        "Hacer el fuego":
            $ tarea = "fuego"
            
            scene estufa
            "(Vas a la cocina y revisas el cajón de leña para prender el fuego.)"
    
    "(Mientras haces tu trabajo, sucede otro temblor… esta vez más fuerte. Los muebles se sacuden"
    
    tu "¡Abuelo! Volvió de nuevo… y fue más fuerte esta vez."
    
    abu "(serio) Sí… lo sentí. Esto ya no me gusta ná."
    "(Silencio )"
    
    scene alerta
    
    "De repente, suena fuerte la alarma del SERNAPRED  en los celulares:"
    
    ser "¡Atención! Alerta Amarilla en su zona. Posible erupción del Volcán Osorno. Prepáre plan de emergencia."
    
    scene com
    
    tu "¡Abuelo! ¡Abuelo! ¡Están diciendo que el volcán puede explotar!"
    
    "(El abuelo se levanta rápidamente y mira por la ventana hacia el volcán. Su expresión cambia por completo.)"
    
    abu "Por la cresta…"
    
    "Pasan unos segundos"
    
    abu "eh analiazado esto"
    
    abu "Sera mejor que te mande a tu casa"

    #Sexta decision quedarse con tu abuelo o irse
    
    menu:
        "¿Qué respondes?"


        "No abuelo me quiero quedar contigo pase lo que pase":
            jump decision_no_te_vas


        "Esta bien abuelo,mejor me voy para mi casa...":
            jump decision_si_te_vas
    label decision_si_te_vas:
        tu "Abuelo... creo que tienes razón"
       
        "(Bajas la mirada. Sientes un nudo en la garganta.)"
        abu "(te mira unos segundos)"
       
        abu "No te sintai mal por eso, cauro. Igual da miedo una cuestión así."
       
        tu "Pero tampoco quiero dejarte solo..."
       
        abu " prométeme una cosa."
       
        tu "¿Cuál?"
       
        abu "(te pone una mano en el hombro)"
       
        abu "Que cuando termine todo esto vay a volver a visitarme."
       
        abu "No quiero que esta sea la última vez que te vea."
       
        "(Te quedas en silencio.)"
       
        "(Sientes un peso en el pecho.)"
       
        "(Te acercas y abrazas a tu abuelo.)"
       
        "(Lo abrazas fuerte.)"
       
        abu "(te aprieta la espalda)"
       
        abu "Estoy orgulloso de ti, nieto."
       
        abu "Más de lo que creí que iba a estar."
       
        "(Te separas lentamente.)"
       
        abu "Ya po... vamos."
       
        abu "Antes de que sea demasiado tarde."
       
        "(Tomas tu mochila.)"
        scene casabun
        "(Miras por última vez la casa, el campo y a tu abuelo.)"
       
        "(Luego caminas hacia la camioneta con el corazón apretado.)"  
       
        abu "regresemos a la villa"
        scene campov
        "El ambiente se siente raro. Ninguno de los dos quiere hablar, pero al mismo tiempo parece que ambos tienen muchas cosas que decir."
       
        "Solo puedes observar amargamente el paisaje."
       
        "Llegan a la villa."
        scene esta3
        "Se despiden amargamente en el terminal."
       
        tu "Cuídate, abuelo."
       
        abu "Tú también, nieto."

        scene interb1
       
        "Te subes al bus."
       
        "Tomas tu asiento."
       
        "Te llegan los recuerdos de todo lo que pasaste con tu abuelo."
       
        "Escondes tus emociones a través del sueño."
       
        "Pasan un par de horas." 
       
        "Te despiertas."
       
        "Observas las noticias en tu teléfono."
       
        "El volcán explotó..."
       
        "Es un desastre. Se informa que la ceniza está recorriendo gran parte del mundo y que, en la zona, un alud ha destruido varias localidades."
       
        "Tu corazón se congela"
       
        "Es un desastre. Se informa que la ceniza está recorriendo gran parte del mundo y que, en la zona, un alud ha destruido varias localidades."
       
        "Intentas llamar a tu abuelo durante todo el día..."
       
        "No contesta."
        "Vuelves a intentarlo una y otra vez."
       
        "Nada."
       
        "El silencio duele más que cualquier noticia."
       
        "Te das cuenta de que quizás nunca vuelvas a verlo."

        #final de la historia dejaste solo a tu abuelo
        
        scene solofin
       
        "FIN DE LA HISTORIA"
       
        "Final: Has sobrevivido, pero dejaste solo a tu abuelo"
    return
#continua la historia
label decision_no_te_vas:
    tu "No abuelo me quiero quedar conitgo pase lo que pase"

    abu "(te mira fijamente por un segundo, )"
    
    abu "Está bien, nieto… pero tenemos que prepararnos pa’ lo que viene. Me faltan unas manos acá en la casa y quizás pa’ los vecinos también."
    
    abu "Tú que andai todo el día metido en la tecnología… ¿qué se te ocurre que podríamos hacer?"
    
    tu "Ya abuelo, déjame ver…"
    
    "(Enciendes tu teléfono. Tus manos sudan y tiemblan ligeramente. Sientes el peso de la responsabilidad.)"
    
    "(Tu abuelo te observa en silencio)"
    
    abu "(poniéndote una mano firme en el hombro) ¿Qué te pasa, nieto? Todavía no erupciona. Relaja ese cuerpo, chico."
    
    "(Te abraza brevemente. Sientes su calor y fuerza. Por un momento, una tranquilidad extraña te recorre el cuerpo.)"
    
    "(Te separas y vuelves a mirar la pantalla.)"
    
    tu "(pensando) ¿Dónde puede estar…?"
    
    "(Buscas las guías oficiales del SENAPRED.)"
    
    "(miras  la página con atención.)"
    
    tu "¡A perfecto!"
    
    tu "Abuelo, ya encontré lo que tenemos que hacer."
    
    abu "¿Y qué dice?"
    
    tu "Podemos hacer varias cosas importantes."
    
    abu "¿Cuáles eliges, mi nieto?"

    #Septima decision de las guia de SENAPRED se puede elegir la que quieras en diferente orden
    $ preparacion = 0
    $ prep_personal = False
    $ prep_casa = False
    $ prep_animales = False

    label eleccion_preparacion:

        if preparacion >= 3:
            jump fin_preparacion

        "Según las guías oficiales, hay tres cosas importantes que deben preparar. ¿Qué quieres hacer primero?"

        menu:
            "1 Preparación personal (Comida, ropa, implementos de emergencia)" if not prep_personal:
                $ preparacion += 1
                $ prep_personal = True
                call prep_personal
                jump eleccion_preparacion

            "1 Preparación personal (Comida, ropa, implementos de emergencia)" if prep_personal:
                "Ya lo hicimos, está terminado."
                jump eleccion_preparacion

            "2 Preparación de casa (Tapar la casa con madera, cerrar ventanas)" if not prep_casa:
                $ preparacion += 1
                $ prep_casa = True
                call prep_casa
                jump eleccion_preparacion

            "2 Preparación de casa (Tapar la casa con madera, cerrar ventanas)" if prep_casa:
                "Ya lo hicimos, está terminado."
                jump eleccion_preparacion

            "3 Preparación de animales (Crear plan de emergencia para salvar a los animales)" if not prep_animales:
                $ preparacion += 1
                $ prep_animales = True
                call prep_animales
                jump eleccion_preparacion

            "3 Preparación de animales (Crear plan de emergencia para salvar a los animales)" if prep_animales:
                "Ya lo hicimos, está terminado."
                jump eleccion_preparacion

    label prep_personal:
        tu "regresemos a la cocina a buscar la comida"
        scene cocina 
        "(Se dirigen a la cocina)"

        tu "abuelo busquemos algo para prepararnos , tienes unas latas arroz o"
        
        abu "creo que me tengo unas latas de jurel aca"
        
        tu "vale guardalas entonces"
        
        tu "Y las botellas vacías necesitamos guardar agua"
        
        abu"En el cajón del lavaplatos pero no te la llenes toda…tengo que guardar para dársela al vecino para que me de chicha el próximo año"
        
        tu "abueloooo…"
        
        abu "es broma nomas agarra las que quieras"
        
        "(buscas las botellas)"
        
        "(te diriges al lavaplatos y empiezas a llenar las botellas una por una)"
        
        tu "con esto bastara no?"
        
        abu "yo creo"
        return

    label prep_casa:
        tu "abuelo tenemos que proteger esta casa si no la quieres perder"
        
        tu "tenemos algo para tapar las ventanas? algunas tablas"
        
        abu "si tengo unas tablas que anduvieron sobrando de la otra ves que me hice un cerco "
        
        tu "a perfecto y el martillo con los clavos"
        
        abu "igual deben de andar tirados en la bodega"
        
        "(se dirigen a la bodega)"
        
        "(observas el volcán majestuoso pero peligroso)"

        scene bodega
        
        abu "aca tenemos las tablas recojas las que puedas"
        
        tu "si igual me llevo el martillo con los clavos"
        
        "(caminan rapido de regreso a la casa)"
        scene casabun

        "Tienen que reforzar 3 ventanas principales antes de que sea demasiado tarde."
        
        $ ventanas_tapadas = 0


    label tapar_ventanas:

        if ventanas_tapadas >= 3:
            jump casa_protegida

        "Ventanas protegidas: [ventanas_tapadas]/3"

        menu:
            "¿Qué ventana quieres reforzar ahora?"

            "Ventana del frente":
                if ventanas_tapadas < 1:
                    $ ventanas_tapadas += 1
                    scene ventab3 with dissolve
                   
                    "(Clavas varias tablas de abajo hacia arriba. La ventana queda bien asegurada.)"
                else:
                    "Ya está protegida."
                jump tapar_ventanas

            "Ventana lateral derecha":
                if ventanas_tapadas < 2:
                    $ ventanas_tapadas += 1
                    scene ventab2 with dissolve
                    "(Refuerzas la ventana del costado derecho con tablas y clavos.)"
                else:
                    "Ya está protegida."
                jump tapar_ventanas

            "Ventana trasera":
                if ventanas_tapadas < 3:
                    $ ventanas_tapadas += 1
                    scene ventab1 with dissolve
                    "(Aseguras la ventana de atrás.)"
                else:
                    "Ya está protegida."
                jump tapar_ventanas

            "Dejarlo para después (arriesgado)":
                tu "Mejor lo hago después..."
                jump decision_riesgosa

    label casa_protegida:
        scene casabut
        tu "(Sudando) Uff... ya estamos."
        abu "Buen trabajo, nieto. Ahora la casa está más protegida."
        return

    label decision_riesgosa:
        scene casabun
        "(Decides no reforzar todas las ventanas...)"
        "Esto podría traer consecuencias más adelante..."
        return
        
        



    scene cor
    label prep_animales:
        abu "vamos pa los animales"
        
        "(corren juntos al establo)"
        scene estab
        
        "(los animales estan inquietos)"
        
        "(las gallinas cacarean las vacas mugen)"
        
        abu "(desesperado) mi animales mi animales diosito"
        
        "tu abuelo las trata de calmar"
        scene vacpov
        abu "(lagrimeando) que vamos a hacer ahora con mis animalitos"
        
        abu "los e visto nacer le e dado alimento…"
        
        abu "no los quiero dejar asi"
        
        "como nunca lo ves angustiado"
        
        "(Los animales están cada vez más nerviosos.)"
        
        "(El suelo vuelve a temblar.)"
        
        "(Tu abuelo te mira esperando una respuesta.)"
        
        abu "Nieto... no tenemos tiempo."
        
        abu "¿Qué hacemos con ellos?"

        # Decisión interna de los animales
        menu:
            "¿Qué hacemos con los animales?"

            "Liberar a los animales y confiar en que encontrarán una ruta de escape por sí solos.":
                jump liberar_animales

            "Protegerlos, preparándoles comida y un lugar seguro para resistir la erupción.":
                jump proteger_animales

    label liberar_animales:
        tu "Abramos las puertas."
        
        abu "¿Seguro, nieto?"
        
        tu "Los animales sienten estas cosas mejor que nosotros."
        
        "(Corres hacia el portón del establo.)"
        
        "(Lo abres de par en par.)"
        
        "(Durante unos segundos no pasa nada.)"
        
        "(de pronto una vaca sale corriendo.)"
        
        "(Detrás de ella salen los demás animales.)"
        
        "(En pocos minutos el establo queda vacío.)"

        abu "Ojalá sepan encontrar un lugar seguro..."
        return

    label proteger_animales:
        tu "No podemos abandonarlos."
        
        abu "(asintiendo con determinación) Así se habla, cabro."
        
        "(Corren por el establo reuniendo sacos de alimento y llenando recipientes con agua. El trabajo es pesado y el tiempo apremia.)"
        
        "(Refuerzan las puertas.)"
        
        abu "(secándose el sudor de la frente, agotado) hicimos todo lo que pudimos…"
        
        "(Los animales parecen un poco más tranquilos, pero nada es seguro .)"
        
        return

    label fin_preparacion:
        tu "hicimos todo lo necesario por si llega ocurrir algo no?"

        abu "eso parece"

        tu "le podemos brindar ayuda a los vecinos"

        abu "Si tu quieres igual ya esta de noche"

        #octava decision la historia toma 2 caminos
    menu octava_decision:
        "Ya nieto que vamos hacer ahora"

        "Mejor quedémonos en la casa a descansar":
            jump ruta_quedarse_casa

        "Vamos ayudar a los vecinos quizás necesiten de nuestra ayuda":
            jump ruta_ayudar_vecinos
label ruta_quedarse_casa:
    "Mejor quedémonos en la casa a descansar"

    scene dormid

    tu "Mejor quedémonos en la casa a descansar, abuelo. Ya hicimos hartoo."

    abu "(dudando un poco) Mmm... puede ser. Aunque no sé si esta noche se preste pa' dormir tranquilo."

    "(Revisas tu mochila, la que preparaste con tanto cuidado horas atrás.)"

    "(Sientes un pequeño remordimiento. Una parte de ti sabe que los vecinos podrían necesitar ayuda.)"

    tu "(pensando) Ya hicimos lo nuestro... mañana vemos qué más se puede hacer."

    abu "Ya po, acuéstate nomás. Si pasa alguna cuestión te despierto al tiro."

    "(El cansancio pesa en todo tu cuerpo.)"

    "(Cierras los ojos.)"

    "(Pasan unos minutos.)"

    "(De pronto sientes una pequeña vibración bajo la cama.)"

    "(La loza de la cocina tintinea suavemente.)"

    "(Abres los ojos de golpe.)"

    tu "(medio dormido) Abuelo... ¿sentiste esa cuestión?"

    abu "(desde la otra pieza) Sehh... fue un temblorcito nomás."

    abu "No te preocupís tanto y duerme."

    "(Te quedas mirando el techo unos segundos.)"

    "(Todo vuelve a quedarse en silencio.)"

    "(Afuera solo se escucha el viento.)"

    "(Intentas relajarte.)"

    "(Poco a poco el sueño vuelve a vencerte.)"

    "Ya es de medianoche."

    scene dormite

    "LA TIERRA COMIENZA A TEMBLAR."

    "Los platos se rompen, los muebles caen."

    "Apenas te puedes levantar."

    "Tú y tu abuelo se levantan tambaleando."

    "Logran salir de la casa, no sin antes agarrar la mochila."

    "Los dos se agarran de la mano."
    
    scene volcanoso

    "Sus ojos observan la furia del volcán."

    "No pueden creer lo que ven."

    "La lava se acerca y quema todo a su paso. Árboles centenarios arden como cerillos."

    abu "(con la voz quebrada) En mis casi 80 años nunca había visto algo así..."

    "Levantan la cabeza."

    "La nube de ceniza se extiende por kilómetros, tapando las estrellas que quedaban."

    "Tu abuelo te toca el hombro."

    scene volcasa

    abu "Nieto... mira allá."

    "Giras la cabeza hacia el noreste."

    "Observas que la erupción derrite la nieve, que se junta con el río. Una masa turbulenta de agua, árboles y ceniza se acerca rápidamente."
    
    scene lahar

    abu "(con los ojos muy abiertos) Eso es un lahar... nieto, partamos de acá cagando."

    tu "Sí, sí... ¡dale!"

    abu "¡Vamos!"

    scene povcam1

    "Corren hacia la camioneta entre el polvo y el ruido."

    abu "(subiéndose, forcejeando con la llave) Que parta esta vieja de lata..."
    #decision interna
    "(La camioneta comienza a ronronear, pero no enciende.)"
    menu decision_camioneta:
        "¿Qué haces?"

        "Intentas tú con la llave mientras el abuelo revisa el motor":
            jump opcion_llave

        "Le dices al abuelo que se calme y lo intente de nuevo":
            jump opcion_calmar_abuelo

    label opcion_llave:
        tu "Abuelo, prueba revisar el motor, yo intento con la llave."

        abu "(asintiendo) Ya, dale nomás."

        "(Giras la llave un par de veces. Te cuesta mantener el pulso firme, pero lo intentas con calma.)"
        jump despues_intento_camioneta


    label opcion_calmar_abuelo:
        tu "Abuelo, tranquilo. Inténtalo otra vez, tú la conoces mejor que nadie."

        abu "(respirando hondo) Tení razón..."

        "(El abuelo se toma un momento y vuelve a girar la llave, esta vez con más calma.)"
        jump despues_intento_camioneta


    label despues_intento_camioneta:
        "(Después de varios intentos...)"

        
        "¡Ron ron ron! La camioneta finalmente se enciende."

        abu "¡Ahora sí que sí! ¡Partamos de acá!"
        "(Suben los dos a la camioneta. Las puertas cierran con fuerza.)"

    scene povcam2

    "(La camioneta avanza dando tumbos por el camino de tierra hacia la villa.)"

    "(El camino está lleno de barro, haciendo que las ruedas patinen constantemente.)"

    abu "No te preocupes nieto, vamos a salir de esta."

    "(De pronto comienza a caer ceniza espesa. Se mezcla con el agua del suelo creando una masilla gris y pegajosa que dificulta aún más el avance.)"

    tu "Aparte de que casi no podemos andar… ahora para variar no estamos quedando ciegos."

    "(Apartas tu mirada por unos instantes, tratando de protegerte los ojos de la ceniza.)"

    abu "Mejor salgamos de acá… no tiene sentido perder más tiempo. Quizás llegamos más rápido caminando."

    "(Entre la oscuridad y la lluvia de ceniza, ves a lo lejos un campo con luces débiles.)"
     
    scene povcasdes

    tu "(angustiado) Abuelo… creo que los vecinos la están pasando mal."

    tu "Parece que les llegó el alud…"

    tu "Creo que deberíamos ir a ayudar…"

    abu "(con voz cansada y pesada) Lamentablemente ya es tarde, nieto… no podemos hacer nada. Debemos seguir nuestro camino a la villa, nos queda poco."

    "(El remordimiento te golpea fuerte en el pecho. Sabes que pudiste haber hecho más…)"

    scene albergue

    "Después de una noche infernal, logran llegar a la zona segura."

    "Sobreviviste… pero el remordimiento por no haber ayudado a los vecinos te acompañará por mucho tiempo."

    #final elegiste quedarte en tu casa y no ayudar a tus vecinos
    
    scene final1

    "Final: Sobreviviste, pero dejaste personas atrás."

    return

    

label ruta_ayudar_vecinos:
    scene  salae
    tu "Vamos a ayudar a los vecinos, quizás necesiten de nuestra ayuda."

    abu "Eres una buena persona. Tenemos acá un par de vecinos, vamos a la casa de una señ que vive con su hija y nieta, es la más cercana."

    abu "Creo que nos topamos a su nieta el primer día que llegaste cuando te enseñé la villa."

    "(Recuerdas que es la misma chica que viste subirse en el bus cuando te dirigías al terminal.)"

    "(Esa misma que no miraste por miedo.)"

    "(Tu cuerpo arde internamente, sientes como tu pecho tiembla con los latidos de tu corazón.)"

    tu "(Te sonrojas y te pones nervioso) ¿De verdad…? ¿A abuelo?"

    abu "Sí que tiene? ¿O ya le anduviste echando el ojo, pillín?"

    tu "Nada…"

    scene povcallu

    "(Suben a la camioneta rumbo a la casa de la vecina.)"

    "(El sol ya se está escondiendo.)"

    scene vecasa

    "(Paran la camioneta frente a la casa.)"

    "(Bajan de la camioneta .)"

    señ "¡Gracias a Dios que vinieron! Estamos desesperadas, no sabemos qué llevar ni qué hacer..."

    abu "Tranquila vecina, hagamos esto con calma. Nietecito, ayúdanos a cargar las cosas importantes."

    scene comeve

    "(Ayudas a cargar bolsas con comida enlatada, ropa, documentos y agua. El ambiente está lleno de tensión.)"

    "(Una mujer de unos corre de un lado a otro, visiblemente nerviosa.)"

    hija "¡Mamá, no encontramos los documentos! ¿Dónde los pusiste?"

    "(En un rincón, la nieta de 18 años intenta calmar a su abuela. Es ella: la misma chica que viste en el bus el primer día.)"

    "(Te mira por un segundo. Reconocimiento mutuo.)"

    tu "(nervioso, acercándote) Hola… soy el nieto del abuelo. Te vi en el bus cuando llegué..."

    chic "(sorprendida pero aliviada) Sí… te reconocí. Pensé que no querías hablar con nadie."

    tu "(sonrojado) Es que… no soy muy bueno socializando. Pero vine a ayudar."

    chic "(sonriendo débilmente a pesar del miedo) Bueno… gracias por venir. De verdad."

    "(Por un breve instante, a pesar del caos, sientes un pequeño alivio en medio del pánico.)"

    señ "(desde el fondo) ¡Apúrense!el volcan ya va explotar ."

    "(Sigues ayudando: cargas bolsas pesadas, ayudas a la hija de 46 años a cerrar las ventanas con tablas improvisadas y tranquilizas un poco a la anciana.)"

    abu "(apremiando) ¡Ya está bueno! Hay que salir ahora mismo antes de que sea peor."

    "(Todos terminan de cargar las cosas. La chica de 18 años te pasa una mochila pesada. Sus manos se rozan por un segundo.)"

    chic "(en voz baja) Gracias… en serio."

    tu "(asintiendo, aún nervioso) Vamos a salir de esta juntos."

    scene povnoche

    "(Suben todos a la camioneta lo más rápido posible.)"

    abu "(manejando con dificultad) ¡Agárrate nieto!"

    "(La camioneta avanza entre barro  el camino es difícil, pero logran llegar a la zona segura.)"

    scene alberg2

    "(en el albergue de evacuados.)"

    "(Estás exhausto, pero vivo.)"

    abu "(sentado a tu lado, cansado pero sonriendo) Lo logramos, cabro..."

    tu "(mirándolo) Gracias por todo, abuelo."

    abu "No me las des. Tú fuiste el que decidió quedarse y ayudar. Eso dice mucho de ti."

    "(Te das cuenta de que ya no eres la misma persona que llegó hace unas semanas desde Santiago. Saliste de tu pieza oscura y enfrentaste algo mucho más grande.)"
     
    scene final2

    #final decidiste ayudar a tus vecinos no estaras solo

    "Has sobrevivido… por el momento y además ayudaste a otros."

    "Final: Sobreviviste y creciste."

    return


    # la historia quedo abierta en un continuara...  
    #se pudo obtener un mejor desarrollo en general pero no fue posible .
    #El trabajo le faltan sonidos musica efectos visuales y que cada vez que hable un personaje su sprit sea visible.
   

   
    

    