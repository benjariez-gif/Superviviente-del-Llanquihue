# CAPÍTULO 3: 
label capitulo3:

    scene Campoia
    #CAMPO del abuelo
   
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
    
    "(De pronto, la tierra tiembla bajo tus pies. Es breve, pero lo suficientemente fuerte como para que se te erice la piel.)"
    
    tu "¿Qué fue eso, abuelo?"
    
    abu "(secándose el sudor con un pañuelo viejo, mirando hacia el volcán) Mmm… a veces tiembla lo típico de este país…"
    
    tu "¿Estás seguro?"
    
    abu "Sehh… tú calmado nomás. ¿Qué hora es esta cuestión?"
    
    tu "Como un poco pasado las 2."
    
    abu "Naaa… bueno… Vamo’ pa’ la casa mejor. Además estoy con la tripa seca, no he comido nada en todo el día."
    
    tu "Ya, vamos entonces."



    # CASA DEL ABUELO
    scene casaabuia
    "(Llegan a la casa. El abuelo se deja caer pesadamente en su silla de madera.)"


    abu "(agotado) Ahhh… jue uta que tengo hambre y frío."


    abu "Porque no te hacís el fuego o pelai las verduras pa’ ayudarme un poco."


    # QUINTA DECISION
    menu:
        "¿Qué haces para ayudar?"


        "Pelar las verduras":
            $ tarea = "verduras"
            "(Buscas unas papas, cebollas y zanahorias y empiezas a pelarlas en la mesa.)"


        "Hacer el fuego":
            $ tarea = "fuego"
            "(Vas a la cocina y revisas el cajón de leña para prender el fuego.)"
    
    "(Mientras haces tu trabajo, sucede otro temblor… esta vez más fuerte. Los muebles se sacuden"
    
    tu "¡Abuelo! Volvió de nuevo… y fue más fuerte esta vez."
    
    abu "(serio) Sí… lo sentí. Esto ya no me gusta ná."
    "(Silencio )"
    
    scene alerta
    
    "De repente, suena fuerte la alarma del SERNAPRED  en los celulares:"
    
    ser "¡Atención! Alerta Amarilla en su zona. Posible erupción del Volcán Osorno. Prepáre plan de emergencia."
    
    scene casaabuia
    
    tu "¡Abuelo! ¡Abuelo! ¡Están diciendo que el volcán puede explotar!"
    
    "(El abuelo se levanta rápidamente y mira por la ventana hacia el volcán. Su expresión cambia por completo.)"
    
    abu "Por la cresta…"
    
    "Pasan unos segundos"
    
    abu "eh analiazado esto"
    
    abu "Sera mejor que te mande a tu casa"
    
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
       
        abu "Ya po... anda."
       
        abu "Antes de que sea demasiado tarde."
       
        "(Tomas tu mochila.)"
       
        "(Miras por última vez la casa, el campo y a tu abuelo.)"
       
        "(Luego caminas hacia la camioneta con el corazón apretado.)"  
       
        abu "regresemos a la villa"
       
        "El ambiente se siente raro. Ninguno de los dos quiere hablar, pero al mismo tiempo parece que ambos tienen muchas cosas que decir."
       
        "Solo puedes observar amargamente el paisaje."
       
        "Llegan a la villa."
       
        "Se despiden amargamente en el terminal."
       
        tu "Cuídate, abuelo."
       
        abu "Tú también, nieto."
       
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
       
        "FIN DE LA HISTORIA"
       
        "Final: Has sobrevivido, pero dejaste solo a tu abuelo"
    return
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

    # =============================================
    # SUB-ESCENAS CON TUS DIÁLOGOS ORIGINALES
    # =============================================

    label prep_personal:
        tu "regresemos a la cocina a buscar la comida"
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
        #dentro de la bodega
        abu "aca tenemos las tablas recojas las que puedas"
        tu "si igual me llevo el martillo con los clavos"
        "(caminan rapido de regreso a la casa)"
        "(empiezan uno por una a tapar las ventanas)"
        "(de abajo hacia arriba y de derecha a izquierda)"
        tu "(Sudando) uff ya estamos"
        return

    label prep_animales:
        abu "vamos pa los animales"
        "(corren juntos al establo)"
        "(los animales estan inquietos)"
        "(las gallinas cacarean las vacas mugen)"
        abu "(desesperado) mi animales mi animales diosito"
        "tu abuelo las trata de calmar"
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


    