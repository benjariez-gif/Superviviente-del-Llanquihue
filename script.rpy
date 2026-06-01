
#inicio de la novela
scene Sueño
label start:
    " Superviviente del llanquihue"
    "esto es un version no terminada "


    "CAPITULO1:INTRODUCCION"

    "En un vasto entorno donde la tierra es blanca y pura, un río cristalino la atraviesa."
    "El cielo dorado brilla con una calidez que nunca habías sentido."
    "Te encuentras en la cima de una colina. Abajo puedes ver a tu familia, mascotas y amigos más queridos."
    "Entre la multitud, ella destaca como un ser luminoso. Alguien que te transmite paz y amor."
    "Cruzan miradas… y sientes una conexión profunda, no solo física, sino también espiritualmente."
    "Se acerca y te susurra al oído con una dulce melodía:"
    "¿Cómo estás, amor mío?"
    "Detrás de ella aparecen unos niños hermosos como flores en primavera."
    "Tu corazón palpita con fuerza. Miles de recuerdos invaden tu mente: abrazos, risas, besos, caricias… toda una vida llena de amor y éxitos."
    #sonido pum
    "¡PUM!"
    "Algo golpea tu techo con fuerza."
    
    #scene pieza

    "(Son las 7 de la mañana)"
    tu "(bostezo largo y cansado) Ahhh… ¿Qué hora es…?"
    "(Revisas tu teléfono. El brillo de la pantalla te ciega por un momento.)"
    tu "Mmm… parece que son las 7 de la mañana."
    "(Abres Instagram casi por instinto. Ves fotos de ella en fiestas, comiendo con amigos y con otro chico…)"
    tu "(pensando) Es tan hermosa… Lástima que ni siquiera me conoce. Además, yo soy un desastre."
    "(Miras tu habitación: está oscura, desordenada y sucia.)"
    "(Te levantas lentamente y te miras en un pequeño espejo.)"
    tu "(pensando) ¿Quién eres? No tienes claras tus metas, no sabes qué estudiar, no tienes amigos, no tienes novia… ni siquiera fuiste capaz de hablarle. No eres nadie." 
    "(Regresas a tu cama con tristeza.)"
    tu "(con lágrimas en los ojos) Mejor duermo hasta tarde… ¿Qué sentido tiene levantarse?"
    tu "Lo único que hago es jugar o ver algo para olvidarme de todo esto…"
    "(Te escondes como una oruga entre las sábanas y duermes llorando.)"
    "(Son las 3 de la tarde y todavía no te has levantado.)"
    ma "Buenos días, mi hijo querido."
    "(Silencio)"
    ma "¿Hijo?"
    "(Toca suavemente la puerta)"
    ma "Hijo, despierta por favor… o al menos dime algo."
    "(Toca más fuerte)"
    ma "¡Levántate! Ya es tarde."
    tu "¡No quiero!"
    ma "Hijo… si sigues encerrado todo el día en esta pieza no vas a llegar a ninguna parte. Déjame entrar."
    "(Te levantas lentamente y abres la puerta.)"
    ma "(mirando el desastre de la habitación) ¿Qué te pasa? Te la pasas todo el día aquí metido… videojuegos, TikTok, series… ¿Eso es todo lo que quieres hacer con tu vida?"
    tu "…No quiero hacer nada. Además, soy feliz así."
    ma "(suspira con tristeza) ¿Feliz? Hijo… alguien quiere verte. Tu abuelo, el que vive en el sur, te está invitando a pasar un tiempo con él."
    tu "¿Está enfermo?"
    ma "No. Solo quiere conocerte mejor. Además, eres su único nieto y no te ha visto desde que eras niño."
    tu "¿Y para qué tengo que ir yo allá? Ni siquiera lo conozco. ¿Quién sabe qué locura me va a mandar a hacer?"
    ma "Hijo, no te va a hacer nada malo… Además, te hace falta salir de esta pieza. Te la pasas pidiendo todo a domicilio, sin ver la luz del sol… Tienes 18 años y parece que ya te rendiste."
    "(Te quedas callado.)"
    ma "Esta podría ser una buena oportunidad para cambiar un poco las cosas. ¿Qué opinas? ¿Quieres ir?"

    label discucion_madre:
    $ intentos = 0   
    ma"Entonces, ¿vas a ir con tu abuelo"
    label repetir_decision:

        if intentos >= 5:
            jump ma_se_rinde

        menu:
            tu "Mmm…"

            "No voy a ir":
                $ intentos += 1

                if intentos == 1:
                    tu "No voy a ir a ningún lado."
                elif intentos == 2:
                    tu "Ya te dije que no quiero ir.!"
                elif intentos == 3:
                    tu "Mamá, no insistas de verdad..."
                elif intentos == 4:
                    tu "No voy a ir y punto."
                else:
                    tu "¡Que no voy!"
                if intentos == 1:
                    ma "Claro que vas a ir, porque yo te lo digo."
                elif intentos == 2:
                    ma "No me contestes así. Soy tu madre y vas a obedecer."
                elif intentos == 3:
                    ma "¡Estás siendo muy terco! ¿Qué te cuesta ir unos días?"
                elif intentos == 4:
                    ma "Me estás sacando de quicio... Te advierto que no voy a tolerar esto."
                elif intentos == 5:
                    ma"¡Ya basta! Estoy harta de tu actitud."
                jump repetir_decision
            "Sí voy a ir":
                $ intentos = 0  

                jump ruta_si_va
        label ma_se_rinde:
        ma "Está bien, no te insisto más."
        ma "Te quedas en la casa, pero vamos a hablar de esto cuando venga tu padre."
        "Fin de la novela (Final malo rapido) ERES UN VAGO"
        
        return   

        label ruta_si_va:
        ma "¡Qué bien, hijo mío! Empaca tus cosas, te vas mañana mismo."
        ma "Recuerda que te vas a la Región de Los Lagos."
        tu "Ya mamá, voy a hacerlo… pero primero voy a comer."
        ma"Está bien, hijo."
        #SEGUNDA DECISION
        #(Equipamiento básico que puedes llevar)
        #Tu: A ver qué puedo meter en mi maleta…
        #Ropa: ¿Cálida y ligera o impermeable?(Cl/I)
        #¿Linterna? (Sí/No)
        #¿Mochila? (Sí/No)
        #¿Mapa de la zona? (Sí/No)
        #¿Botiquín básico? (Sí/No)

        "Después de comer y pasar unas horas, empacas tus cosas..."
        "Cierras tu maleta."
        tu "Nada más creo…"
        ma "¿Estás listo? ¿Tienes tus documentos?"
        tu "Oh, mis documentos y el dinero en efectivo… cómo me olvidé de eso."
        "(Buscas en tu habitación y los encuentras.)"
        ma "Si tienes todo, duerme bien. Mañana por la tarde nos vamos al terminal de buses."
        tu "Sí, será mejor que me duerma y descanse…"
        "(Observas tu maleta. Sientes intriga por lo que te espera en los próximos días.)"

        #scene estacion de buses

        "( Al día siguiente)" 
    "El terminal está lleno de gente y es muy ruidoso."
    ma "Ya hijo, hemos llegado. ¿Te despediste bien de tu padre?"
    tu "(bostezo) …Sí mamá… Me despedí de él."
    ma "¿Y de tu habitación… y de tus juegos? ¿Seguro que no los vas a extrañar?"
    tu "Mamá, si empiezas a preguntarme esas cosas, mejor no lo hagas por favor…"
    ma "(sonriendo con ternura) Solo estaba bromeando contigo…"
    "(Se queda mirándote un momento en silencio. Sus ojos reflejan una mezcla de orgullo y preocupación. Luego mira hacia el fondo.)"
    ma "¡Mira! Ya llegó tu bus."
    tu "Será mejor que me vaya."
    ma "¿No te olvides de darme un abrazo, sí? Aunque sé que no te gustan mucho…"
    "(Observas sus ojos, que reflejan un amor maternal profundo.)"
        #TERCERA DECISION (no afecta la historia)
        #Abrazo rápido
        #Abrazo intenso y prolongado
    ma "Gracias, hijo."
    tu "Chao mamá… hasta pronto."
    ma "¿Me llamas cuando llegues, sí?"
    tu "Sí, obvio que lo voy a hacer."
    "(Subes al bus y tomas tu asiento junto a la ventana.)"
    "Los nervios y las náuseas recorren tu cuerpo. Sientes un nudo en el estómago."
    tu "(pensando) Dios… ¿en qué me metí?"
    "(Dudas por unos momentos, mirando por la ventana. Finalmente aceptas que ya no puedes echarte atrás.)"
    tu "(pensando) Mejor me pongo a jugar con el teléfono hasta que me duerma…"
    "(Te pones los audífonos y te recuestas en el asiento. Poco a poco, el movimiento del bus te va adormeciendo.)"  
    

   
    "CAPÍTULO 2: CONOCIENDO EL LUGAR Y A MI ABUELO"
    #scene bus 
    "(Sigues en el bus)"
    "Luego de un largo viaje, despiertas lentamente. La luz del sol te da directamente en la cara."
    "Quedas asombrado. El Lago Llanquihue refleja el brillo del sol como un espejo gigante. A lo lejos, imponente y nevado, se alza el Volcán Osorno."
    tu "¡Guau!"
    "El bus sigue su trayecto. Pasan bosques nativos, ríos cristalinos y casas humildes dispersas."
    "En una de las paradas suben y bajan pasajeros. Una chica de tu edad llama especialmente tu atención: cabello oscuro, mirada tranquila, típica de la zona."
    tu "(pensando) Es hermosa… como el paisaje."
    "(Apartas la mirada rápidamente.)"
    tu "(pensando) Ya pasé por esto… Mejor trato de ignorar su belleza."
    "(Pasan unos minutos más.)"
    "A lo lejos ves tu destino. Un cartel de madera aparece en el camino:"
    "«Villa Santa María de las Cenizas — Población: 1250 habitantes»"
    "(Observas el pequeño pueblo.)"
    tu "Es chiquito… pero tiene su encanto."

    #scene termnial de buses
    "El bus se detiene. Te bajas con tu maleta. El aire frío y limpio te golpea la cara."
    tu "No veo a nadie… ¿Mi abuelo sabía que venía hoy?"
    "(Te quedas parado con intriga.)"
    tu "Será mejor que haga una llamada rápida a mi mamá, como le prometí."
    tu "Hola mamá, te llamo porque el abuelo todavía no aparece…"
    "(De repente, alguien te toca la espalda.)"
    abu "¡Hola campeón!"
    tu "(sorprendido) Disculpe… ¿lo conozco?"
    abu "Lo siento, te confundí con mi nieto. Te pareces mucho… No te veo desde hace más de 10 años."
    tu "…¿Abuelo?"
    abu "(con una gran sonrisa) ¡Sabía que erai tú, cabro e’ mierda! ¿Cómo estai? ¡Estás más grande que yo, oiga!"
    "(Te quedas callado. No sabes bien qué decir. Estar tanto tiempo aislado ha hecho que incluso hablar con tu familia te cueste.)"
    abu "¡Dame un abrazo oye! ¿Desayunaste? ¿Te pinta si vamo’ a comer algo?"
    "(Te armás de valor y respondes con la frente en alto.)"

        #CUARTA DECISION
    menu:
        "¿Qué respondes?"

        "No gracias, quiero ir a un lugar donde no haga frío":
            jump decision_no_comer

        "Sí, sería piola":
            jump decision_si_comer
    label decision_no_comer:
    tu "No gracias, quiero ir a un lugar donde no haga frío." 
    abu "Uta la lesera, si estai terrible flaco cabro."
    "(Decides cruzar la calle por tu cuenta. No ves bien un auto que venía...)" 
    #sonido de choque
    "Te atropella."
    "Fin de la historia. final arrebatamiento"
    return
label decision_si_comer:

    tu "Sí, sería piola."
    abu "¡Así me gusta mi nieto! Así agarrai algo de cuerpo. Vamos a un lugar donde venden las cazuelas ricaaaas!!!"
    abu "Esa vieja uta que tiene buena mano, ya verás nieto."
    "(Te vas caminando junto a tu abuelo hacia el restaurante.)"
    tu "Sí, sería piola."

    #resntaurante
    "(En el restaurante, te sirven un plato de cazuela humeante.)"
    tu "(pensando) ¿Quién come cazuela como desayuno?"
    "(Recuerdas que tu abuelo ni te dejó elegir, solo le dijo a la mesera que trajera dos platos.)"
    abu "Te dije que la vieja de acá tenía buena mano o no?"
    "(A pesar de que te parece rica, el sabor es muy distinto a la comida a domicilio que sueles pedir.)"
    tu "Oye abuelo, ¿queda muy lejos tu casa? Está empezando a hacer frío."
    abu "No, pero vamos en mi camioneta. Quería llevarte a dar una vuelta por el pueblito pa’ que conozcas cómo es acá en el sur po."
    tu "Bueno abuelo, a ver qué tan distinto de Santiago es aquí."

    # Continúa el recorrido
    "(Después de comer, te subes con tu abuelo a su vieja camioneta.)"
    abu "Por acá está la iglesia, con la estatua de la virgen… Por acá la gente que ayuda con los cultivos, una carnicería, de acá sacaron los pollos pa’ la cazuela."
    "(De repente la camioneta se frena en seco.)"
    abu "¡Chutaaaa! Otra vez con problemas el cacharro este."
    tu "¿Otra vez?"
    abu "Tengo de que años esta camioneta, antes de que nacieras tú pues. Si esta camioneta tiene menos brillo que campana de goma."

    "(El abuelo maneja hasta el museo sin dejar de hablar. Pareciera que se había guardado años de palabras y ahora las está sacando todas para su nieto)"

    abu "Este es el museo, nietecito. Acá en el pueblito tenemos cualquier historia…"
    abu "Hubo una vez hace años que creímos que iba a explotar el Volcán Osorno… quedó la caga’ ese día. Y cuando fue el terremoto del 60, jue fuerte aquí poh."
    tu "¿Cómo fue vivir ese terremoto?"
    abu "(mirando al suelo, con voz más baja) Con mucho miedo, mi nieto… Si afectó a casi todo Chile esa cuestión. A tu abuelita casi le da un infarto ese día."
    tu "Es verdad… no me acuerdo casi nada de la abuela."
    abu "(se queda en silencio un momento) …Falleció hace como 15 años ya. De esos años que ya no te veía."
    "(Te quedas en blanco. Un vacío extraño te invade al darte cuenta de que no recordabas la muerte de tu propia abuela, alguien tan importante.)"
    tu "Lo siento mucho, abuelo…"
    abu "(poniéndote una mano en el hombro) Fue doloroso, chiquillo… pero hay que seguirle pa’ lante nomás."
    "(Después de un par de historias más sobre el pueblito, el abuelo te lleva de vuelta a la camioneta.)"
    abu "Ya está haciéndose tarde, vamonos pa’ la casa."
    tu "Sí… ojalá esté calentito allá."
    abu "Vay a sacar calor, cabro. Vamos a tener que picar leña."
    tu "Abuelo, yo no sé picar leña…"
    abu "¡Cómo no vay a saber! Si por algo erí hombre pues. Allá yo te enseño…"
    "(Quedas cabizbajo, sintiendo una fuerte añoranza por tu vida sedentaria en Santiago. La comodidad de tu pieza, tus juegos, tu rutina… todo eso parece tan lejos ahora.)"
   
    "CAPITULO 3 El volcán"
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

    #SCENE CASA DEL ABUELO
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
    "De repente, suena fuerte la alarma del SERNAPRED  en los celulares:"
    ser "¡Atención! Alerta Amarilla en su zona. Posible erupción del Volcán Osorno. Prepárese para evacuar."
    tu "¡Abuelo! ¡Abuelo! ¡Están diciendo que el volcán va a explotar!"
    "(El abuelo se levanta rápidamente y mira por la ventana hacia el volcán. Su expresión cambia por completo.)"
    abu "Por la cresta…"
    abu "Será mejor que empaquemos algunas cosas…"
   