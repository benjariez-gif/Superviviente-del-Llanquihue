# CAPÍTULO 1: INTRODUCCIÓN
label capitulo1:
    
    scene sue with fade
    " Superviviente del llanquihue"
    
    "CAPITULO1:INTRODUCCION"
    #Escena inical sueño del protagonista
    play music sssueño
    scene sue
    "En un vasto entorno donde la tierra es blanca y pura, un río cristalino la atraviesa."

    "El cielo dorado brilla con una calidez que nunca habías sentido."

    "Te encuentras en la cima de una colina. Abajo puedes ver a tu familia, mascotas y amigos más queridos."

    "Entre la multitud, ella destaca como un ser luminoso. Alguien que te transmite paz y amor."
    
    "Cruzan miradas… y sientes una conexión profunda, no solo física, sino también espiritualmente."
    
    "Se acerca y te susurra al oído con una dulce melodía:"
    
    "¿Cómo estás, amor mío?"
   
    "Detrás de ella aparecen unos niños hermosos como flores en primavera."
    
   
    "Tu corazón palpita con fuerza. Miles de recuerdos invaden tu mente: abrazos, risas, besos, caricias… toda una vida llena de amor y éxitos."
    
    #Despertar brusco mañana
    stop music
    play sound glata
    "¡PUM!"

    
    scene piezaos with vpunch
    with flash        
    
    pause 0.3
    with flash          

    "Algo golpea tu techo con fuerza."
     
    #dialogo interno
    "(Son las 7 de la mañana)"
    
    tu "(bostezo largo y cansado) Ahhh… ¿Qué hora es…?"
   
    "(Revisas tu teléfono. El brillo de la pantalla te ciega por un momento.)"
    
    tu "Mmm… parece que son las 7 de la mañana."
   
    "(Abres Instagram casi por instinto. Ves fotos de ella en fiestas, comiendo con amigos y con otro chico…)"
    
    tu "(pensando) Es tan hermosa… Lástima que ni siquiera me conoce. Además, yo soy un desastre."

    scene piezaos with dissolve
    
    
    "(Miras tu habitación: está oscura, desordenada y sucia.)"
    
    "(Te levantas lentamente y te miras en un pequeño espejo.)"
    
    tu "(pensando) ¿Quién eres? No tienes claras tus metas, no sabes qué estudiar, no tienes amigos, no tienes novia… ni siquiera fuiste capaz de hablarle. No eres nadie."
    
    "(Regresas a tu cama con tristeza.)"
    
    tu "(con lágrimas en los ojos) Mejor duermo hasta tarde… ¿Qué sentido tiene levantarse?"
   
    tu "Lo único que hago es jugar o ver algo para olvidarme de todo esto…"
   
    "(Te escondes como una oruga entre las sábanas y duermes llorando.)"
     
    #Tarde dialogo con la madre
    scene piezalu with fade
    "(Son las 3 de la tarde y todavía no te has levantado.)"
    
    ma "Buenos días, mi hijo querido."
    
    "(Silencio)"
    
    ma "¿Hijo?"
    
    play sound puerta1
    "(Toca suavemente la puerta)"
    
    ma "Hijo, despierta por favor… o al menos dime algo."

    play sound puerta2

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

    #Primera decision/ ir o no ir /con el abuelo
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
        
        #Final rapido decides no ir
        ma "Está bien, no te insisto más."
        scene vago with fade
        ma "Te quedas en la casa, pero vamos a hablar de esto cuando venga tu padre."
        "Fin de la novela (Final malo rapido) ERES UN VAGO"
       
        return  

        #continua la historia
        label ruta_si_va:
        ma "¡Qué bien, hijo mío! Empaca tus cosas, te vas mañana mismo."
        ma "Recuerda que te vas a la Región de Los Lagos."
        tu "Ya mamá, voy a hacerlo… pero primero voy a comer."
        ma"Está bien, hijo."
        #SEGUNDA DECISION decartada

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

    #Estacion  de buses santiago
    scene estacion with fade
   
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
    menu:
        "Que abrazo le daras a tu madre?"


        "Abrazo rápido":
            $ abrazo = "Rapido"
            "(Le das un abrazo rapido parece que no le gusto a tu madre...)"


        "Abrazo intenso y prolongado":
            $ abrazo = "Intenso y prolongado"
            "(Le das un abrazo amoroso a tu madre se siente feliz y menos preocupada)"
    ma "Gracias, hijo."
    
    tu "Chao mamá… hasta pronto."
    
    ma "¿Me llamas cuando llegues, sí?"
    
    tu "Sí, obvio que lo voy a hacer."

    scene interb1
    "(Subes al bus y tomas tu asiento junto a la ventana.)"
    
    "Los nervios y las náuseas recorren tu cuerpo. Sientes un nudo en el estómago."
    
    tu "(pensando) Dios… ¿en qué me metí?"
    
    "(Dudas por unos momentos, mirando por la ventana. Finalmente aceptas que ya no puedes echarte atrás.)"
    
    tu "(pensando) Mejor me pongo a jugar con el teléfono hasta que me duerma…"
    
    "(Te pones los audífonos y te recuestas en el asiento. Poco a poco, el movimiento del bus te va adormeciendo.)"  
   
    