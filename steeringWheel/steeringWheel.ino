void setup() {
    Serial.begin(9600);
    pinMode(A2, INPUT_PULLUP);  // Botón 1
    pinMode(A4, INPUT_PULLUP);  // Botón 2
}

void loop() {
    int volante = analogRead(A0);  // Potenciómetro del volante
    int boton1 = digitalRead(A2);   // Leer Botón 1
    int boton2 = digitalRead(A4);   // Leer Botón 2

    // Enviar los datos en formato "volante,boton1,boton2"
    Serial.print(volante);
    Serial.print(",");
    Serial.print(boton1);
    Serial.print(",");
    Serial.println(boton2);

    delay(10);
}
