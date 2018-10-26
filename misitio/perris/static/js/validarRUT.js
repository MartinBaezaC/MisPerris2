function checkRut() {

        var letters = 
                [   "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                    "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", 
                    "v", "w", "x", "y", "z", ",", ".", "!", "'", "$", "%", "&",
                    "/", "(", ")", "=", "?", "¿", "¡", ".", ","
                ]
    var txtRun = document.getElementById("txtRun")
    txtRun.value = txtRun.value.toLowerCase()
    for(let i in letters){
        txtRun.value = txtRun.value.replace(letters[i], "")
    }
    if(txtRun.value.includes("-")) {
        txtRun.value = txtRun.value.replace(/-/g, "")
        txtRun.value = txtRun.value.slice(0, txtRun.value.length - 1) + "-" + txtRun.value.slice(txtRun.value.length - 1)
    }else
    {
        txtRun.value = txtRun.value.slice(0, txtRun.value.length - 1) + "-" + txtRun.value.slice(txtRun.value.length - 1)
    }
    if(txtRun.value.includes("k")) {
        txtRun.value = txtRun.value.replace(/k/g, "")
        txtRun.value += "k"
    }
}
function solonumeros(e) {
    key=e.keyCode || e.which;

    teclado=String.fromCharCode(key).toLowerCase();

    letras="1234567890 ";

    especiales="";

    teclado_especial=false;

    for(var i in especiales){
        if(key==especiales[i]){
            teclado_especial=true;7
            break;
        }
    }

    if(letras.indexOf(teclado)==-1 && !teclado_especial){
        return false;
    }
}

