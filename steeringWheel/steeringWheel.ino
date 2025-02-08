void setup() {
    Serial.begin(9600);
}

void loop() {
    int volante = analogRead(A0);  // Potenciómetro del volante
    Serial.println(volante);  // Enviar solo el valor del volante
    delay(10);
}
