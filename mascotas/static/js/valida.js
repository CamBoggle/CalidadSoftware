$(function(){

    $("#datos").validate({
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            pass:{
                required:true
            },
            fono:{
                required:true,
                number:true
            },           
            valor:{
                required:true,
                
            },
        },//rules
        messages:{
            nom:{
                required:'Ingrese nombre de usuario',
                minlength:' caracteres insuficientes(5)'
            },
            correo:{
                required:'Ingrese correo electronico',
                email:'formato de correo no valido'
            },
            pass:{
                required:'ingrese contraseña',
                minlength:'Caracteres insuficientes(8)'
            },
            fono:{
                required:'ingrese numero de telefono',
                minlength:'cantidad de digitos insuficientes(9)'

            },           
            valor:{
                required:'Ingrese monto',
                min:'Por favor ingrese un monto'
               
                
            },
        }
    })

})