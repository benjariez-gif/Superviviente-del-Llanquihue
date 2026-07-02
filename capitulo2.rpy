# CAPÍTULO 2: 
label capitulo2:
    #escena del bus
    scene interb3
    "CAPÍTULO 2: CONOCIENDO EL LUGAR Y A MI ABUELO"
   
    "(Sigues en el bus)"
    
    "Luego de un largo viaje, despiertas lentamente. La luz del sol te da directamente en la cara."
    
    "Quedas asombrado. El Lago Llanquihue refleja el brillo del sol como un espejo gigante. A lo lejos, imponente y nevado, se alza el Volcán Osorno."
    
    tu "¡Guau!"

    scene interb4
    
    "El bus sigue su trayecto. Pasan bosques nativos, ríos cristalinos y casas humildes dispersas."
    
    scene interb2
    
    "En una de las paradas suben y bajan pasajeros. Una chica de tu edad llama especialmente tu atención: cabello oscuro, mirada tranquila, típica de la zona."
  
    tu "(pensando) Es hermosa… como el paisaje."
    
    "(Apartas la mirada rápidamente.)"
    
    tu "(pensando) Ya pasé por esto… Mejor trato de ignorar su belleza."
    
    "(Pasan unos minutos más.)"

    scene bia

    "A lo lejos ves tu destino. Un cartel de madera aparece en el camino:"
    
    "«Villa Santa María de las Cenizas — Población: 1250 habitantes»"
   
    "(Observas el pequeño pueblo.)"
   
    tu "Es chiquito… pero tiene su encanto."


    #escena termnial de buses Villa santa maria de las cenizas
    scene esta2
    
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


        #CUARTA DECISION decides seguir con tu abuelo o no
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

    #Final te atropellaron
    "Te atropella."
    scene atropello
    "Fin de la historia. final arrebatamiento"
    return

    #continua la historia
label decision_si_comer:


    tu "Sí, sería piola."
    
    abu "¡Así me gusta mi nieto! Así agarrai algo de cuerpo. Vamos a un lugar donde venden las cazuelas ricaaaas!!!"
    
    abu "Esa vieja uta que tiene buena mano, ya verás nieto."
    
    scene rest
    "(Te vas caminando junto a tu abuelo hacia el restaurante.)"
    
    tu "Sí, se ve piola."


    # Escena resntaurante
    scene cazue
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
    scene cea
    abu "Por acá está la iglesia, con la estatua de la virgen… Por acá la gente que ayuda con los cultivos, una carnicería, de acá sacaron los pollos pa’ la cazuela."
    
    "(De repente la camioneta se frena en seco.)"
    
    abu "¡Chutaaaa! Otra vez con problemas el cacharro este."
    
    tu "¿Otra vez?"
    
    abu "Tengo de que años esta camioneta, antes de que nacieras tú pues. Si esta camioneta tiene menos brillo que campana de goma."


    "(El abuelo maneja hasta el museo sin dejar de hablar. Pareciera que se había guardado años de palabras y ahora las está sacando todas para su nieto)"

    scene muse
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

