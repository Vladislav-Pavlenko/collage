function calculate() {
  const eta1 = parseFloat(document.getElementById("eta1").value);
  const eta2 = parseFloat(document.getElementById("eta2").value);
  const N1 = parseFloat(document.getElementById("N1").value);
  const N2 = parseFloat(document.getElementById("N2").value);
  const Vstar = parseFloat(document.getElementById("Vstar").value);
  const S = parseFloat(document.getElementById("S").value);
  const Ncom = parseFloat(document.getElementById("Ncom").value);

  if ([eta1, eta2, N1, N2, Vstar, S, Ncom].some(isNaN)) {
    alert("Будь ласка, заповніть усі поля коректно!");
    return;
  }

  const eta = eta1 + eta2;
  const N = N1 + N2;
  const V = N * Math.log2(eta);
  const L = Vstar / V;
  const I = L * V;
  const T = V / (S * L);
  const lambda = Vstar * L;
  const B = Vstar ** 2 / (3000 * lambda);
  const F = Ncom / N1;

  const output = `
η = ${eta}
N = ${N}
Об'єм програми (V) = ${V.toFixed(2)}
Рівень якості програмування (L) = ${L.toFixed(4)}
Інтелектуальний зміст (I) = ${I.toFixed(2)}
Час програмування (T) = ${T.toFixed(2)} сек (~${(T / 60).toFixed(2)} хв)
Рівень мови програмування (λ) = ${lambda.toFixed(2)}
Очікувана кількість помилок (B) = ${B.toFixed(2)}
Рівень коментованості (F) = ${F.toFixed(4)} (${(F * 100).toFixed(2)}%)
`;

  document.getElementById("result").textContent = output;
}
