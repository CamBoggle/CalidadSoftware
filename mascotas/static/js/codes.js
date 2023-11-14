/*CODIGO VER MAS*/
let btn_ver_mas = document.getElementById("btn_ver_mas");
let span_text = document.getElementById("span_text");
let btn_ver_menos = document.getElementById("btn_ver_menos");

btn_ver_mas.addEventListener("click", act_style);

function act_style(){
    span_text.classList.add("mostrar");
    btn_ver_mas.classList.add("ocultar");
}

btn_ver_menos.addEventListener("click", ocultarTexto);

function ocultarTexto(){
    span_text.classList.remove("mostrar");

    if(span_text.classList.contains("mostrar")){
        btn_ver_mas.classList.add("mostrar");
    }
    else{
        btn_ver_mas.classList.remove("ocultar");
    }
}
/*COLORES*/
function colorFondo(obj) 
{
    obj.style.backgroundColor= "#757575"; 
}

function colorBlanco(obj)
{
    obj.style.backgroundColor='#353535';
}

/*MAYUSCULA EN EL NOMBRE*/
function upperText(texto)
{
    const x = texto;
    x.value= x.value.toUpperCase();
}

