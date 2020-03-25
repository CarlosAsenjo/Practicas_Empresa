document.getElementById("calculadora").addEventListener("click", calculadora);

function calculadora(e) {

    var select = e.target.innerHTML;
    var result = document.getElementsByClassName('result');

    switch (e.target.className) {

        case "reset":

            result[0].innerHTML = "0";
            break;

        case "button":

            if (result[0].innerHTML != "0") {
                result[0].innerHTML += select;

            } else {
                result[0].innerHTML = select;
            }
            break;

        case "calculate":

            var calcular = result[0].innerHTML.split("=");
            console.log(calcular)
            result[0].innerHTML = eval(calcular[0]);
            break;

        default:
            alert("Ha habido un error");
            break;
    }
}