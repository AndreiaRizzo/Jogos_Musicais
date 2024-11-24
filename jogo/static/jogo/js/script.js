function verificarResposta(resposta, respostaCorreta) {
    
    if (resposta === respostaCorreta) {
        // Toca o som de acerto
        
        
        document.getElementById("gifAcerto").style.display = "block";

    } else {
        alert("Ops! Tente novamente.");
    }
}