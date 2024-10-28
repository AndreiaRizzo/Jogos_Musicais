function verificarResposta(resposta) {
    const respostaCorreta = "Trompete";
    if (resposta === respostaCorreta) {
        // Toca o som de acerto
        document.getElementById("audioAcerto").play();
        document.getElementById("gifAcerto").style.display = "block";

    } else {
        alert("Ops! Tente novamente.");
    }
}